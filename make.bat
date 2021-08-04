@REM #################################################################################
@REM # GLOBALS                                                                       #
@REM #################################################################################

@SET PROJECT_DIR=.\
@REM @SET BUCKET=[OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')
@SET PROFILE=default
@SET PROJECT_NAME=iris_cookiecutter
@SET PYTHON_INTERPRETER=C:\Users\buue\Anaconda3\python.exe
@SET PDFLATEX=C:\Users\buue\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe
@SET CONDA=C:\Users\buue\Anaconda3\condabin\conda.bat
@SET HAS_CONDA=True

@REM #################################################################################
@REM # COMMANDS                                                                      #
@REM #################################################################################

@REM ## Set up python interpreter environment
:create_environment
IF %HAS_CONDA%==True (
	@echo ">>> Detected conda, creating conda environment."
	conda create --name %PROJECT_NAME%
	@echo ">> New conda env created. Activate with: conda activate %PROJECT_NAME%"
)
EXIT /B 0

@REM requirements
:requirements
@echo requirements
conda update -n base -c defaults conda
conda activate %PROJECT_NAME%
%PYTHON_INTERPRETER% test_environment.py
%PYTHON_INTERPRETER% -m pip install --user -U pip setuptools wheel
pip install --user -r ./requirements.txt
EXIT /B 0

@REM Download Data
:data
@echo %PYTHON_INTERPRETER%
%PYTHON_INTERPRETER% src/data/make_dataset.py data/external data/raw data/interim
EXIT /B 0

@REM Make Features
:features
	%PYTHON_INTERPRETER% src/features/build_features.py data/interim data/processed
EXIT /B 0

@REM Test environment
:test_environment
@echo test_environment
	%PYTHON_INTERPRETER% test_environment.py
EXIT /B 0

@REM @REM ## Generate Report:
:report
	cd reports
	%PDFLATEX% main.tex\
	cd ..
EXIT /B 0

@REM Delete temporary files
:clean
	@echo Removing files
exit /b 0

@REM Build Models and Predict
:model
	%PYTHON_INTERPRETER% src/models/train_model.py data/processed models
	%PYTHON_INTERPRETER% src/models/predict_model.py data/processed models
exit /b 0

@REM Make Data Visualizations
:visualizations
	%PYTHON_INTERPRETER% src/visualization/visualize.py  data/raw reports/figures
exit /b 0

@REM Build all
:build
	CALL clean
	CALL requirements
	CALL data
	CALL features
	CALL model
	CALL visualizations
	CALL report
EXIT /B 0


@REM ###################################
@REM Handle commandline arguments
@REM ###################################

if %1%==test_environment CALL :test_environment

if %1%==create_environment CALL :create_environment

if %1%==requirements CALL :requirements

if %1%==data CALL :data
if %1%==features CALL :features
if %1%==model call :model
if %1%==visualizations call :visualizations
if %1%==report call :report
if %1%==build CALL :build



@REM Delete all compiled Python files
if %1%==clean (
	@REM 	find . -type f -name "*.py[co]" -delete
	@REM 	find . -type d -name "__pycache__" -delete
	@REM 	find . -name "*.pdf" -delete
	@REM 	find . -name "*.pkl" -delete
	@REM 	find . -name "*.csv" -delete
	@REM 	find . -name "*.data" -delete
	@REM 	find . -name "*.names" -delete
	@REM 	find . -name "*.log" -delete
	@REM 	find . -name "*.aux" -delete
)
