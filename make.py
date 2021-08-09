import os
import sys
import platform
import subprocess

#################################################################################
# GLOBALS                                                                       #
#################################################################################

ROOT = os.getcwd() # complete  path
PROJECT_NAME = "iris-cookiecutter" # this is also then name of the conda environment
PYTHON = "python3" # Python interpreter.

# PROJECT_NAME = {{cookiecutter.repo_name}}
# PYTHON = {{cookiecutter.python_interpreter}}

# Platform specific settiting
PLATFORM = platform.system()
if PLATFORM == "Windows":
    # check local and server (Stata1)
    PDFLATEX = "/Library/TeX/texbin/pdflatex"
    STATA = "/usr/local/stata/stata-mp -b do"
    R = "/usr/local/bin/Rscript"
    WHICH = "where"
    CONDA_ACTIVATE = "conda activate"
    CMD_SEP = "&&"
    PATH =  'set PATH="%PATH%;C:\path\to\directory\"'
elif PLATFORM == "Darwin":  # Macos
    PDFLATEX = "/Library/TeX/texbin/pdflatex"
    R = "/usr/local/bin/Rscript"
    WHICH = "which"
    CONDA_ACTIVATE = "source activate"
    CMD_SEP = ";"
else:  # Linxu/Stata-3
    WHICH = "which"
    STATA = "/usr/local/stata/stata-mp -b do"
    R = "/usr/bin/Rscript"
    CONDA_ACTIVATE = "source activate"
    CMD_SEP = ";"
    

if subprocess.check_output([WHICH, "conda"]):
    HAS_CONDA = True
else:
    HAS_CONDA = False
    print("Conda has to be installed")
    exit()


def run(command, activate_conda=True, change_dir = True):
    """
    Run an external command.
    activate_conda will make sure the correct conda environment is used
    change dir will cd into the ROOT directory
    """
    conda = ""
    if activate_conda == True:
        conda = f"{CONDA_ACTIVATE} {PROJECT_NAME} {CMD_SEP} "

    if change_dir == True:
        os.chdir(ROOT)

    command = conda + command
    print(f"Running: {command} in {ROOT}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    s = ''.join(map(chr, proc_stdout))
    print(s)
    return(proc_stdout)

def test_environment():
    """
    Test if the correct version of Python is found
    """
    system_major = sys.version_info.major
    if PYTHON == "python":
        required_major = 2
    elif PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("Unrecognized python interpreter: {}".format(
            PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))
    else:
        print(">>> Development environment passes all tests!")


def install_requirements():
    """
    Install requirments
    """
    run(f"{PYTHON} -m pip install -U pip setuptools wheel")
    run(f"{PYTHON} -m pip install -r requirements.txt")


def data():
    """Make Dataset"""
    run(f"{PYTHON} src/data/make_dataset.py data/external data/orig data/intermediate")


def features():
    """Make Features"""
    run(f"{PYTHON} src/features/build_features.py data/intermediate data/final")


def model():
    """Build Models and Predict"""
    run(f"{PYTHON} src/models/train_model.py data/final data/final")
    run(f"{PYTHON} src/models/predict_model.py data/final data/final")


def visualizations():
    """Make Data Visualizations and tables"""
    run(f"{PYTHON} src/visualization/visualize.py  data/orig results/figures results/tables")


def report():
    """Generate PDF from LateX sources"""
    run(f"cd {ROOT}/publication; {PDFLATEX} LaTeX-template.tex")


def stata():
    """Sample for running stata script"""
    try:
        STATA
        run(f"{STATA} src/stata/main.do")
    except NameError:
        print("STATA not defined")


def r():
    """Sample for running R script"""
    try:
        R
        run(f"{R} src/r/main.r {ROOT}")
    except NameError:
        print("R is not defined")





def delete_files(name):
    """Cross platform function to delete file with extension"""
    # Delete compiled Python and other temporary files
    if PLATFORM =="Windows":
        run(f"del /s {name}")
    else:
        run(f"find . -type f -name '{name}' -delete", activate_conda=False)

def clean():
    """Delete temporary files"""
    files = ["*.pyc", "__pycache__", "*.pdf", "*.pkl",
             "*.csv", "*.data", "*.names", "*.log", "*.aux", "*.bbl", "*.blg",
             "*.nav", "*.out", "*run.xml", "*.snm", "*.synctex.gz", "*.toc"]
    for f in files:
        delete_files(f)

# Lint using Flake8 for code checking
def lint():
    """Check python code for layour errors"""
    run("flake8 src")


# Set up python interpreter environment
def create_environment():
    """Create an conda-environment with PROJECT_NAME"""
    print(f"Creating environment {PROJECT_NAME}")
    version = "3"
    print(">>> Detected conda, creating conda environment.")
    run(f"conda create -n {PROJECT_NAME}--yes", activate_conda=False)  # python={version} 
    print(f">>> New conda env created. Activate with:\nsource activate {PROJECT_NAME}")


# TODO: Add specific data download/upload scripts


def show_help():
    """Show help instructions"""
    print("TODO: Instructions")

def build():
    """Build everything from scratch"""
    clean()
    test_environment()
    install_requirements()
    data()
    features()
    model()
    visualizations()
    report()


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
        elif(arg == "test_environment"):
            test_environment()
        else:
            print(f"Error in options: {arg}")
            break
