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


if %1%==test_environment (
	@echo test_environment
	%PYTHON_INTERPRETER% test_environment.py
)

@REM ## Set up python interpreter environment
if %1%==create_environment (

	IF %HAS_CONDA%==True (
		@echo ">>> Detected conda, creating conda environment."
		conda create --name %PROJECT_NAME%
		@echo ">> New conda env created. Activate with: conda activate %PROJECT_NAME%"
	)
	@REM ELSE (

	@REM 	%PYTHON_INTERPRETER% -m pip install -q virtualenv virtualenvwrapper
	@REM 	@echo ">>> Installing virtualenvwrapper if not already installed.\nMake sure the following lines are in shell startup file\n\
	@REM 	export WORKON_HOME=$$HOME/.virtualenvs\nexport PROJECT_HOME=$$HOME/Devel\nsource /usr/local/bin/virtualenvwrapper.sh\n"
	@REM 	@bash -c "source `which virtualenvwrapper.sh`;mkvirtualenv $(PROJECT_NAME) --python=%PYTHON_INTERPRETER%"
	@REM 	@echo ">>> New virtualenv created. Activate with:\nworkon $(PROJECT_NAME)"
	@REM )

)

if %1%==data (

	@echo %PYTHON_INTERPRETER%
	%PYTHON_INTERPRETER% src/data/make_dataset.py data/external data/raw data/interim
)

@REM requirments
if %1%==requirements (
	@echo requirements
	conda update -n base -c defaults conda
	conda activate %PROJECT_NAME%
	%PYTHON_INTERPRETER% test_environment.py
	%PYTHON_INTERPRETER% -m pip install --user -U pip setuptools wheel
	pip install --user -r ./requirements.txt
)



@REM @REM ## Make Features
if %1%==features (
	%PYTHON_INTERPRETER% src/features/build_features.py data/interim data/processed
)

@REM @REM ## Build Models and Predict

if %1%==model (
	%PYTHON_INTERPRETER% src/models/train_model.py data/processed models
	%PYTHON_INTERPRETER% src/models/predict_model.py data/processed models
)

@REM @REM ## Make Data Visualizations
if %1%==visualizations (
	%PYTHON_INTERPRETER% src/visualization/visualize.py  data/raw reports/figures
)

@REM @REM ## Generate Report:
if %1%==report (
	cd reports
	%PDFLATEX% main.tex\
	cd ..
)

@REM @REM ## Build all
@REM build: clean requirements data features model visualizations report

@REM @REM ## Delete all compiled Python files
@REM clean:
@REM 	find . -type f -name "*.py[co]" -delete
@REM 	find . -type d -name "__pycache__" -delete
@REM 	find . -name "*.pdf" -delete
@REM 	find . -name "*.pkl" -delete
@REM 	find . -name "*.csv" -delete
@REM 	find . -name "*.data" -delete
@REM 	find . -name "*.names" -delete
@REM 	find . -name "*.log" -delete
@REM 	find . -name "*.aux" -delete



@REM @REM ## Lint using flake8
@REM lint:
@REM 	flake8 src

@REM @REM ## Upload Data to S3
@REM sync_data_to_s3:
@REM ifeq (default,$(PROFILE))
@REM 	aws s3 sync data/ s3://$(BUCKET)/data/
@REM else
@REM 	aws s3 sync data/ s3://$(BUCKET)/data/ --profile $(PROFILE)
@REM endif

@REM @REM ## Download Data from S3
@REM sync_data_from_s3:
@REM ifeq (default,$(PROFILE))
@REM 	aws s3 sync s3://$(BUCKET)/data/ data/
@REM else
@REM 	aws s3 sync s3://$(BUCKET)/data/ data/ --profile $(PROFILE)
@REM endif



@REM @REM ## Test python environment is setup correctly
@REM test_environment:
@REM 	%PYTHON_INTERPRETER% test_environment.py