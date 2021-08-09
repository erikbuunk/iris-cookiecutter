
REM ###################################
REM Handle commandline arguments
REM ###################################
@REM conda create -n %1%
@REM conda activate %1%
python3 -m pip install -U pip setuptools wheel --cache-dir C:\Temp
python3 -m pip install -r requirements.txt --cache-dir C:\Temp