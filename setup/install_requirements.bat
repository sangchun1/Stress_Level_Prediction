@echo off
echo ========================================
echo Stress Level Prediction Project
echo Requirements Installation Script
echo ========================================
echo.

echo Checking if conda is available...
conda --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Conda is not installed or not in PATH
    echo Please install Anaconda or Miniconda first
    pause
    exit /b 1
)

echo.
echo Creating conda environment 'stress_prediction'...
conda create -n stress_prediction python=3.9 -y

echo.
echo Activating conda environment...
call conda activate stress_prediction

echo.
echo Installing packages from requirements.txt...
pip install -r requirements.txt

echo.
echo Installing additional conda packages for better performance...
conda install -c conda-forge mkl mkl-include intel-openmp -y

echo.
echo ========================================
echo Installation completed successfully!
echo ========================================
echo.
echo To activate the environment, run:
echo conda activate stress_prediction
echo.
echo To start Jupyter Notebook, run:
echo jupyter notebook
echo.
pause 