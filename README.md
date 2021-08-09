# iris_cookiecutter

Demo project of cookiecutter for iris project

## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

---

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

# Steps

## Prerequisites

1. python3
2. Anaconda or conda
3. update conda (`conda update -n base -c defaults conda`)

<!-- ## Project initialization
(For cookiecutter)
```
cookiecutter https://github.com/drivendata/cookiecutter-data-science
cd iris_cookiecutter
``` -->

                                                    ## make.py

make.py is the equivalent of Make on Unix and is the starting point of running all the processes within the project

in the directory run

```bash
python make.py <commmand>
```

## Creating the python environment

Create a conda environment and installing requirements

```bash
python make.py test_environment # Test if python is installed
python make.py create_environment # Create the conda environment
```

We have to switch to the new envirnment. <project-name> will be
```bash
conda activate <project-name>
```




```bash
python make.py requirements # install the required libraries and the local module (in the `src` directory)
```

Or run it from the commandline:

```
conda create -n iris-cookiecutter
conda activate iris-cookiecutter
pip install -r requirements.txt
```

## running replication


```bash
python make.py build # runs all the jobs necessary for replication
```


## running separate jobs


Use `python make.py <rule>`

```
Available rules:
build               Build all (runs multiple command for replicatation)
clean               Delete all compiled temporary files
create_environment  Set up python interpreter environment
data                Make Dataset
features            Make Features
lint                Lint using flake8
model               Build Models and Predict
requirements        Install Python Dependencies
test_environment    Test python environment is setup correctly
visualizations      Make Data Visualizations
report              Create PDF from Latex Sources
```


## Changes:

Markdown support
https://www.sphinx-doc.org/en/master/usage/markdown.html?highlight=markdown

