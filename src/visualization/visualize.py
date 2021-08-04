# -*- coding: utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import click
import logging
from pathlib import Path
from os.path import join
from dotenv import find_dotenv, load_dotenv
import pickle
from sklearn.linear_model import LogisticRegression


def load_pickle(filename):
    filehandler = open(filename, 'rb')
    return pickle.load(filehandler)


def save_pickle(filename, object):
    filehandler = open(filename, 'ab')
    pickle.dump(object, filehandler)


@click.command()
@click.argument('input_filepath', type=click.Path())
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ visualsl
    """
    logger = logging.getLogger(__name__)
    logger.info('visuals model')

    iris = pd.read_csv(join(input_filepath, "IRIS.csv"))

    # Pairwise joint plot (scatter matrix)
    sns.pairplot(iris, hue='species', height=3, diag_kind="kde")
    plt.savefig(join(output_filepath, "figure.pdf"))

    # create and save latex table
    df = iris.head(10)
    df.to_latex(join(output_filepath, "my_table.tex"))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
