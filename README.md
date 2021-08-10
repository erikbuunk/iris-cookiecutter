# iris-cookiecutter-python

Demo project of the cookiecutter-data-science for iris project and adjusted for use at our institute

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>.</small></p>

# Installation and running

## Prerequisites

1. python3
2. conda: Anaconda, miniconda
3. git
4. make sure to update conda (`conda update -n base -c defaults conda`)
5. commandline (cmd on window and Terminal with bash or zsh)

## Creating the python environment

Create a conda environment and installing requirements

```bash
python make.py test_environment # Test if python is installed
python make.py create_environment # Create the conda environment
```

We have to switch to the new environment with the PROJECT_NAME. We have to do it manually from the command line

```bash
conda activate <project-name>
```

After this install the requirements:

```bash
python make.py requirements # install the required libraries and the local module (in the `src` directory)
```

Alternatively you can run it from the commandline:

```bash
conda create -n iris-cookiecutter-python
conda activate iris-cookiecutter-python # or sourc activate ...
pip install -r requirements.txt
```

# Running jobs

## Running complete replication

```bash
python make.py build # runs all the jobs necessary for replication
```

## Running separate jobs

Use `python make.py <rule>`

```
Usage: python3 make.py <argument>

With the following value(s) for <argument> (multiple are allowed):

requirements              Install requirements
data                      Retrieve the data
clean                     Delete temporary data
test_environment          Test if the correct version of Python is found
create_environment        Create an conda-environment with PROJECT_NAME
install_requirements      Install requirements
clean                     Delete temporary files
lint                      Check python code for layout errors
data                      Download datasets
features                  Make features
model                     Build models and predict
visualizations            Make data visualizations and tables
report                    Generate PDF from LateX sources
stata                     Sample for running Stata script
r                         Sample for running R script
get_data                  Example: Get data stored somewhere into the project.
help                      Get overview of the arguments
build                     Complete build everything from scratch
partial_build             Build from preprocessed data. (copies data.zip to data directory)
```

Jobs are defined in make.yml, a file used by make.py

# Project Organization

```
├── LICENSE             <-- License file
├── Makefile            <-- original make file>
├── README.md
├── data                <- all data
│   ├── external        <- Data from third party sources.
│   ├── intermediate    <- Intermediate data that has been transformed.
│   ├── final           <-- The final, canonical data sets for modeling or report
│   └── orig            <- The original, immutable data dump. (make this read only)
├── data.zip            <-- helper file.  If it is not feasible to do calculations or data sources change
├── docs                <- A default Sphinx project; see sphinx-doc.org for detail
├── Makefile            <- Makefile with commands like `make data` (NOT USED, but kept as reference)
├── make.py             <- Main file to run the processes
├── make.yml            <- File that defines the options of `make.py`
├── notebooks           <- Exploratory notebooks
├── publication         <- Final publication (PDF or Latex)
├── requirements.txt    <- libraries to be loaded
├── results             <- Results that will be used in the final results, also logfiles
│   ├── figures
│   ├── log
│   └── tables
├── setup.py            <- script that is used so that src is a python module/package.
│                          It makes project pip installable (pip install -e .) so src can be imported
├── src                 <- all source code and scripts
    │   ├── __init__.py <- Makes src a Python module
│   ├── data            <- Scripts to download or generate data
│   ├── features        <- feature creation (data wrangling)
│   ├── models          <- training of machine learning model and predictions
│   ├── r               <- example script for running R
│   ├── stata           <- example script for running Stata
│   ├── utilities       <- helper functions. You can see how these are references in other scripts
│   └── visualization   <- visualizations and tex exports of tables
├── src.egg-info        <- module information
└── tox.ini             <- tox file with settings for running tox; see tox.readthedocs.io
```
