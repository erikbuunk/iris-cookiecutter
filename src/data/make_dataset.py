# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os
import pandas as pd
import requests


def download_external(url, path):
    logging.info('Download Starting')

    r = requests.get(url)

    # this will take only -1 splitted part of the url
    filename = url.split(os.path.sep)[-1]

    with open(os.path.join(path, filename), 'wb') as output_file:
        output_file.write(r.content)

    logging.info('Download Completed')


@click.command()
@click.argument('external_filepath', type=click.Path(exists=True))
@click.argument('raw_filepath', type=click.Path(exists=True))
@click.argument('interim_filepath', type=click.Path())
def main(external_filepath, raw_filepath, interim_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Downloading and processing data set')

    # download data
    base_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/'
    download_external(base_url + 'iris.data', external_filepath)
    download_external(base_url + 'iris.names', external_filepath)

    # create dataframe
    columns = ["sepal_length", "sepal_width",
               "petal_length", "petal_width", "species"]
    iris = pd.read_csv(os.path.join(
        external_filepath, "iris.data"), header=None, names=columns)
    # save raw version
    iris.to_csv(os.path.join(raw_filepath, "IRIS.csv"), index=None)

    # process data and save final dataset
    iris["petal_width"] = iris["petal_width"]*1.2
    iris.to_csv(os.path.join(interim_filepath,
                "iris_processed.csv"), index=None)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
