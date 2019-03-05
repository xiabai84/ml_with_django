# use this script to download ml-model and store it under .media/models


import requests


def download_file_from_google_drive(file_id, destination):
    url = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(url, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(url, params=params, stream=True)

    save_response_content(response, destination)


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


if __name__ == "__main__":
    print("Please be patient, this may take a few moments...")
    file_ids = ['1yEQQxiFpmqc0wAE2rc_fDcIrGUoDF-nJ',
                '1HLAjghVXZsreVrFg02rT4Dn9w35aOMqJ',
                '1K0CyCN7YQucVxfV5eL00XBqu3-8G5p2Z']
    file_names = ['model-dense.h5',
                  'pca_svc_tuned.pk',
                  'vgg16_notop.h5']
    destination_folder = 'models/'
    destinations = [destination_folder + fn for fn in file_names]
    for f_id, dst in zip(file_ids, destinations):
        print("Downloading to {}".format(dst))
        download_file_from_google_drive(f_id, dst)
