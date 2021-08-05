# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from os.path import join
from dotenv import find_dotenv, load_dotenv
from sklearn.model_selection import train_test_split
import pandas as pd
from src.utilities.utilities import save_pickle


@click.command()
@click.argument('input_filepath', type=click.Path())
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ makes features
    """
    logger = logging.getLogger(__name__)
    logger.info('making features')

    # Creating features
    iris = pd.read_csv(join(input_filepath, "iris_processed.csv"))

    array = iris.values

    X = array[:, 0:4]
    Y = array[:, 4]
    validation_size = 0.20
    seed = 7

    X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=validation_size,
                                                                    random_state=seed)

    save_pickle(join(output_filepath, "X_train.pkl"), X_train)
    save_pickle(join(output_filepath, "X_validation.pkl"), X_validation)
    save_pickle(join(output_filepath, "Y_train.pkl"), Y_train)
    save_pickle(join(output_filepath, "Y_validation.pkl"), Y_validation)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
