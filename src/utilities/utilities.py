import requests
import logging
import pickle
import os


def download_external(url, path):
    logging.info('Download Starting')

    r = requests.get(url)

    # this will take only -1 splitted part of the url
    filename = url.split("/")[-1]

    with open(os.path.join(path, filename), 'wb') as output_file:
        output_file.write(r.content)

    logging.info('Download Completed')


def load_pickle(filename):
    filehandler = open(filename, 'rb')
    return pickle.load(filehandler)


def save_pickle(filename, object):
    filehandler = open(filename, 'ab')
    pickle.dump(object, filehandler)


# if __name__ == '__main__':
#     # log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#     # logging.basicConfig(level=logging.INFO, format=log_fmt)

#     # # not used in this stub but often useful for finding various files
#     # project_dir = Path(__file__).resolve().parents[2]

#     # # find .env automagically by walking up directories until it's found, then
#     # # load up the .env entries as environment variables
#     load_dotenv(find_dotenv())
