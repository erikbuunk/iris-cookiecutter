@echo off

REM Command file for Project

REM GLOBALS
SET ROOT=%~dp0
SET PROJECT_NAME=iris-cookiecutter
set VENV=venv
set PYTHON_INTERPRETER=%ROOT%%VENV%\Scripts\python.exe
set STATA= 
set PDFLATEX=
set R="C:\Program Files\R\R-4.1.1\bin\RScript"

if "%1" == "" goto help

if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
    echo.  create_environment Create a virtual environment
    echo.  install            Install all the libraries
    echo.  data               Retrieve data
    echo.  features
    echo.  model               
    echo.  visualizations
    echo.  report
    echo.  build
    echo.  clean
    echo.  lint
	goto end
)

if "%1" == "create_environment" (
    echo create environment %VENV%
    cd %ROOT%
    call py -m venv %VENV%
    cd %VENV%
    call Scripts\activate
    cd ..

    echo You activate the environment by calling
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
    call %STATA% src/s /qtata/main.do
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
    echo "DO EVERTHING"
    echo "NOT Implemented"
    goto end
)

:end
