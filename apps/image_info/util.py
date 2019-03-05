# -*- coding: utf-8 -*-
__author__ = 'Bai XIA'

import os
import datetime
import dill
import numpy as np
import tensorflow as tf
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from keras.applications import vgg16, inception_v3
from collections import Counter
from sympy.utilities.iterables import multiset_permutations
from vis.visualization import visualize_cam
from PIL import Image


root_path = os.path.dirname(os.path.abspath(__file__)).replace('/apps', '').replace('/image_info', '')

CLASSES_3 = ["Nahaufnahme", "Außenaufnahme", "Innenaufnahme"]
CLASSES_DMG = ["Unbeschädigt", "Beschädigt"]

dmg_classifier = load_model(root_path + '/media/models/model-dense.h5')
feature_extractor = load_model(root_path + '/media/models/vgg16_notop.h5')
graph = tf.get_default_graph()
classifier = dill.load(open(root_path + '/media/models/pca_svc_tuned.pk', 'rb'))


def get_image_widths(f_list, to_height):
    rtn = []
    for f in f_list:
        with Image.open(f) as img:
            w, h = img.size
            rtn.append(w / h * to_height)
    return rtn


def prepare_image_direct(img, net):
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    if net == 'vgg16':
        x = vgg16.preprocess_input(x)
    elif net == 'xception':
        x = inception_v3.preprocess_input(x)
    else:
        raise ValueError("Unknown net architecture, don't know how to preprocess image!")
    return x


def prepare_image(img_path, target_size=(224, 224), net='vgg16'):
    img = load_img(img_path, target_size=target_size)
    return prepare_image_direct(img, net)


# TODO: (optional, only for speed) first check if taking max confidence for each sample already gives good distribution
def predict_set(prob_mtx, n_per_cat, labels=None):
    """
    Predict the classes of a set of samples using knowledge about the number of samples belonging to each class
    :param prob_mtx: matrix specifying all class probabilities for every sample
    :param n_per_cat: list of number of samples belonging to each class
    :param labels: optional: give label strings
    :return: class predictions
    """
    if not labels:
        labels = [i for i in range(len(n_per_cat))]
    labels = np.array(labels)
    if prob_mtx.shape[0] != sum(n_per_cat):
        print("total number of assigneld labels must match number of elements")
        return
    if prob_mtx.shape[1] != len(n_per_cat):
        print("probabilities must match the number of categories!")
        return
    label_counts = Counter({l_idx: n for l_idx, n in enumerate(n_per_cat)})
    best_so_far = -np.inf
    best_perm = []
    # go over all possible permutations. multiset_permutations skips the duplicates due to repeated occurrences
    for permutation in multiset_permutations(list(label_counts.elements())):
        current_sum = sum(prob_mtx[np.arange(len(prob_mtx)), permutation])
        if current_sum > best_so_far:
            best_so_far = current_sum
            best_perm = permutation

    return best_perm, labels[best_perm]


def get_classification(file_paths):
    with graph.as_default():
        im_list = []
        for file_path in file_paths:
            prepared = prepare_image(file_path)
            im_list.append(prepared)
        vgg_features = feature_extractor.predict(np.vstack(im_list))
        vgg_features = np.reshape(vgg_features, (len(im_list), 7 * 7 * 512))
        predictions = classifier.predict_proba(vgg_features)
        if len(file_paths) == 8:
            highest, _ = predict_set(predictions, [2, 4, 2])
        else:
            highest = np.argmax(predictions, axis=1)
        results = [CLASSES_3[h] + ": %2.0f" % (p[h] * 100) + '%' for p, h in zip(predictions, highest)]
        return results


def get_classification_single(file):
    '''
    this part should be overwritten!

    :param file: image which should be estimated
    :return: str of classification
    '''
    with graph.as_default():
        im_list = []

        prepared = prepare_image(file)
        im_list.append(prepared)

        vgg_features = feature_extractor.predict(np.vstack(im_list))
        vgg_features = np.reshape(vgg_features, (len(im_list), 7 * 7 * 512))

        predictions = classifier.predict_proba(vgg_features)
        highest = np.argmax(predictions, axis=1)
        results = [CLASSES_3[h] + ": %2.0f" % (p[h] * 100) + '%' for p, h in zip(predictions, highest)]
        return results[0]


def normalize_tf_image(image):  # from [-1. ... 1.] to [0. ... 1.]
    return (image + 1.) / 2.


def make_gradcam_image(image, prediction, model):
    prediction = prediction.squeeze()
    if prediction >= 0.5:
        # highlight the regions contributing towards '1-damaged' classification
        grad_modifier = None
    else:
        # highlight the regions contributing towards '0-non-damaged' classification
        grad_modifier = 'negate'

    # squeeze out the 'batch' dimension for keras-vis
    image = image.squeeze()

    gradient = visualize_cam(model, layer_idx=-1, filter_indices=0,
                             seed_input=image, backprop_modifier=None, grad_modifier=grad_modifier)

    image = normalize_tf_image(image)
    gradient_tmp = np.expand_dims(gradient, axis=2)
    # print(image.shape, gradient_tmp.shape)
    image_gradient = np.concatenate((image, gradient_tmp), axis=2)
    # print(image_gradient.shape)
    figure, ax = plt.subplots(1, 1)
    # figure.suptitle('Prediction: {:.2f}'.format(prediction), y=0.8, horizontalalignment='center')
    ax.imshow(image_gradient)
    ax.contour(gradient, 3, colors='k')
    plt.axis('off')
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    return figure


def get_dmg_classification_single(file, dmg_type, user_id, uploadtimestamp):

    with graph.as_default():
        im_list = []

        prepared = prepare_image(file, target_size=(299, 299), net='xception')
        im_list.append(prepared)
        im_list = np.vstack(im_list)
        predictions = dmg_classifier.predict(im_list)

        # return a estimated image
        grad_fig = make_gradcam_image(im_list, predictions, dmg_classifier)

        # prepare a path for persistence storing
        d = datetime.date.today()
        year = '{:04d}'.format(d.year)
        month = '{:02d}'.format(d.month)
        curr = year + month + "/"
        directroy = root_path + '/media/ml_estimated/' + curr

        # checking whether this dir already exists. if not create a new one with year+month
        if not os.path.exists(directroy):
            os.makedirs(directroy)

        dmg_class = [1 if p[0] > 0.5 else 0 for p in predictions]
        file_prefix = [CLASSES_DMG[dc] + "_%2.0f" % (abs(1 - dc - p[0]) * 100) + '%' for dc, p in zip(dmg_class, predictions)][0]

        # define a relative path for django database
        img_relativ_path = str("ml_estimated/" + curr + user_id +'_'+dmg_type + '_' + file_prefix + '_'+uploadtimestamp.strftime("%Y-%m-%d %H:%M:%S") + '.png').replace(": ", "_")
        # define image name and absolute path on project sys
        img_abs_path = str(root_path + '/media/ml_estimated/' + curr + user_id + '_' + dmg_type + '_' + file_prefix + '_'+uploadtimestamp.strftime("%Y-%m-%d %H:%M:%S")).replace(": ", "_")

        grad_fig.savefig(img_abs_path, bbox_inches='tight', pad_inches=0)

        # this part should be overwritten ! We have only one image instead of a image list
        # results = [CLASSES_DMG[dc] + ": %2.0f" % (abs(1 - dc - p[0]) * 100) + '%' for dc, p in zip(dmg_class, predictions)]

        return str(file_prefix).replace("_", ": "), img_relativ_path
