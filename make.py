import os
import sys
import platform
import subprocess

#################################################################################
# GLOBALS                                                                       #
#################################################################################

ROOT = os.getcwd()
PROJECT_NAME = "test-project" # this is also conda environment
PYTHON_INTERPRETER = "python3"

# PROJECT_NAME = {{cookiecutter.repo_name}}
# PYTHON_INTERPRETER = {{cookiecutter.python_interpreter}}

PLATFORM = platform.system()
if PLATFORM == "Windows":
    # check local and server (Stata1)
    PDFLATEX = "/Library/TeX/texbin/pdflatex"
    STATA = "/usr/local/stata/stata-mp -b do"
    R = "/usr/local/bin/Rscript"
    WHICH = "where"
elif PLATFORM == "Darwin":  # Macos
    PDFLATEX = "/Library/TeX/texbin/pdflatex"
    R = "/usr/local/bin/Rscript"
    WHICH = "which"
else:  # Linxu/Stata-3
    WHICH = "which"
    STATA = "/usr/local/stata/stata-mp -b do"
    R = "/usr/bin/Rscript"

if subprocess.check_output([WHICH, "conda"]):
    HAS_CONDA = True
else:
    HAS_CONDA = False
    print("Conda has to be installed")
    exit()


def run(command):
    activate_conda = f"source activate {PROJECT_NAME}; "
    os.chdir(ROOT)

    print(f"running {activate_conda + command} in {ROOT}")
    process = subprocess.Popen(activate_conda + command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout)
    return(proc_stdout)




def install_requirements():
    """Install requirments"""
    run(f"{PYTHON_INTERPRETER} -m pip install -U pip setuptools wheel")
    run(f"{PYTHON_INTERPRETER} -m pip install -r requirements.txt")


def data():
    # Make Dataset
    run(f"{PYTHON_INTERPRETER} src/data/make_dataset.py data/external data/orig data/intermediate")


def features():
    # Make Features
    run(f"{PYTHON_INTERPRETER} src/features/build_features.py data/intermediate data/final")


def model():
    """Build Models and Predict"""
    run(f"{PYTHON_INTERPRETER} src/models/train_model.py data/final data/final")
    run(f"{PYTHON_INTERPRETER} src/models/predict_model.py data/final data/final")


def visualizations():
    """Make Data Visualizations and tables"""
    run(f"{PYTHON_INTERPRETER} src/visualization/visualize.py  data/orig results/figures results/tables")


def report():
    """Generate PDF from LateX sources"""
    run(f"cd {ROOT}/publication; {PDFLATEX} LaTeX-template.tex")


def stata():
    """Sample for running stata script"""
    try: STATA
    except NameError: print("STATA not present")
    else: run(f"{STATA} src/stata/main.do")


def r():
    """Sample for running R script"""
    try: R
    except NameError: print("R is not defined")
    else: run(f"{R} src/r/main.r {ROOT}")



def build():
    """Build everything from scratch"""
    clean()
    install_requirements()
    data()
    features()
    model()
    visualizations()
    report()


def delete_files(name):
    # Delete compiled Python and other temporary files
    if PLATFORM =="Windows":
        run(f"del {name}")
    else:
        run(f"find . -type f -name '{name}' -delete")



def clean():
    files = ["*.py[co]", "__pycache__", "*.pdf", "*.pkl",
             "*.csv", "*.data", "*.names", "*.log", "*.aux", "*.bbl", "*.blg",
             "*.nav", "*.out", "*run.xml", "*.snm", "*.synctex.gz", "*.toc"]
    for f in files:
        delete_files(f)

# Lint using Flake8 for code checking
def lint():
    run("flake8 src")


# Set up python interpreter environment
def create_environment():
    print(f"Creating environment {PROJECT_NAME}")
    version = "3"
    print(">>> Detected conda, creating conda environment.")
    run(f"conda create --name {PROJECT_NAME} python={version} --yes ")
    print(f">>> New conda env created. Activate with:\nsource activate {PROJECT_NAME}")


def test_environment():
    """Test if (Python) environment is setup correctly"""
    run(f"{PYTHON_INTERPRETER} test_environment.py")
    # TODO: add R and Stata checks

# TODO: Add specific data download/upload scripts


def show_help():
    print("Hello instructions")


#################################################################################
# COMMANDS                                                                      #
#################################################################################
if __name__ == '__main__':
    if len(sys.argv) == 1:
        show_help()

    for arg in sys.argv[1:]:
        if(arg == 'requirements'):
            install_requirements()
        elif(arg == "data"):
            data()
        elif(arg == "features"):
            features()
        elif(arg == "model"):
            model()
        elif(arg == "visualizations"):
            visualizations()
        elif(arg == "report"):
            report()
        elif(arg == "r"):
            r()
        elif(arg == "stata"):
            stata()
        elif(arg == "build"):
            build()
        elif(arg == "clean"):
            clean()
        elif(arg == "lint"):
            lint()
        elif(arg == "create_environment"):
            create_environment()
        else:
            print(f"Error in options: {arg}")
            break
