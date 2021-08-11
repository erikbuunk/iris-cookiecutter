@echo off

REM Command file for Project

::#################################################################################
::# GLOBALS                                                                       #
::#################################################################################


REM LOCAL windows laptop
SET ROOT=%~dp0
SET PROJECT_NAME=iris-cookiecutter
set VENV=venv
set PYTHON_INTERPRETER=%ROOT%%VENV%\Scripts\python.exe
set STATA=/usr/local/stata/stata-mp -b do
SET PDFLATEX=C:\Users\buue\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe
set R="C:\Program Files\R\R-4.1.1\bin\RScript"

REM STATA3
REM

if "%1" == "" goto help

::#################################################################################
::# PROJECT RULES                                                                 #
::#################################################################################

if "%1" == "create_environment" (
    echo create environment %VENV%
    cd %ROOT%
    call py -m venv %VENV%
    cd %VENV%
    call Scripts\activate
    cd ..

    echo You can activate the environment by calling
    echo %VENV%\Scripts\activate
    goto end
)

if "%1" == "install" (
    call %PYTHON_INTERPRETER% -m pip install -U pip setuptools wheel
	call %PYTHON_INTERPRETER% -m pip install -r requirements.txt
    goto end
)

if "%1" == "data" (
    call %PYTHON_INTERPRETER% src/data/make_dataset.py data/external data/orig data/intermediate
    goto end
)

if "%1" == "features" (
    call %PYTHON_INTERPRETER% src/features/build_features.py data/intermediate data/final
    goto end
)

if "%1" == "model" (
    call %PYTHON_INTERPRETER% src/models/train_model.py data/final data/final
    call %PYTHON_INTERPRETER% src/models/predict_model.py data/final data/final
    goto end
)

if "%1" == "visualizations" (
    call %PYTHON_INTERPRETER% src/visualization/visualize.py  data/orig results/figures results/tables
    goto end
)

if "%1" == "report" (
    call %PYTHON_INTERPRETER% src/visualization/visualize.py  data/orig results/figures results/tables
    goto end
)

if "%1" == "r" (
    call %R% src/r/main.R
    goto end
)

if "%1" == "stata" (
    call %STATA% src/stata/main.do
    goto end
)


if "%1" == "clean" (
    del /s /q *.pyc
	del /s /q *.pkl
	del /s /q *.csv
	del /s /q *.data
	del /s /q *.names
	del /s /q *.log
	del /s /q *.aux
	del /s /q *.bbl
	del /s /q *.bcf
	del /s /q *.blg
	del /s /q *.nav
	del /s /q *.out
	del /s /q *.run.xml
	del /s /q *.snm
	del /s /q *.synctex.gz
	del /s /q *.toc
	goto end
)

if "%1" == "build" (
    echo "Not Implemented"
    goto end
)

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
    echo.  build               Build everything from scratch
    echo.  clean               Delete compiled Python and other temporary files
    echo.  create_environment  Set up python interpreter environment
    echo.  data                Make Dataset
    echo.  features            Make Features
    echo.  lint                Lint using Flake8 for code checking
    echo.  model               Build Models and Predict
    echo.  r                   Sample for running R script
    echo.  report              Generate PDF from LateX sources
    echo.  requirements        Install Python Dependencies
    echo.  stata               Sample for running stata script
    echo.  test_environment    Test if (Python) environment is setup correctly
    echo.  visualizations      Make Data Visualizations and tables
	goto end
)

:end
