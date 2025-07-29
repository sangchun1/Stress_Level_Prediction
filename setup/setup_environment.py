#!/usr/bin/env python3
"""
Stress Level Prediction Project - Environment Setup Script
This script automatically sets up the conda environment and installs all required packages.
"""

import subprocess
import sys
import os
import platform

def run_command(command, check=True):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout, e.stderr

def check_conda():
    """Check if conda is available."""
    print("Checking if conda is available...")
    success, stdout, stderr = run_command("conda --version", check=False)
    if not success:
        print("ERROR: Conda is not installed or not in PATH")
        print("Please install Anaconda or Miniconda first")
        return False
    print(f"✓ Conda found: {stdout.strip()}")
    return True

def create_environment():
    """Create conda environment."""
    print("\nCreating conda environment 'stress_prediction'...")
    success, stdout, stderr = run_command("conda create -n stress_prediction python=3.9 -y")
    if not success:
        print(f"ERROR: Failed to create environment: {stderr}")
        return False
    print("✓ Environment created successfully")
    return True

def install_requirements():
    """Install packages from requirements.txt."""
    print("\nInstalling packages from requirements.txt...")
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("ERROR: requirements.txt not found")
        return False
    
    # Install packages
    success, stdout, stderr = run_command("conda run -n stress_prediction pip install -r requirements.txt")
    if not success:
        print(f"ERROR: Failed to install requirements: {stderr}")
        return False
    print("✓ Requirements installed successfully")
    return True

def install_conda_packages():
    """Install additional conda packages for better performance."""
    print("\nInstalling additional conda packages for better performance...")
    success, stdout, stderr = run_command("conda install -n stress_prediction -c conda-forge mkl mkl-include intel-openmp -y")
    if not success:
        print(f"WARNING: Failed to install conda packages: {stderr}")
        print("Continuing anyway...")
    else:
        print("✓ Conda packages installed successfully")
    return True

def install_jupyter_kernel():
    """Install Jupyter kernel for the new environment."""
    print("\nInstalling Jupyter kernel...")
    success, stdout, stderr = run_command("conda run -n stress_prediction python -m ipykernel install --user --name stress_prediction --display-name 'Stress Prediction'")
    if not success:
        print(f"WARNING: Failed to install Jupyter kernel: {stderr}")
        print("You can install it manually later with:")
        print("conda activate stress_prediction")
        print("python -m ipykernel install --user --name stress_prediction --display-name 'Stress Prediction'")
    else:
        print("✓ Jupyter kernel installed successfully")
    return True

def main():
    """Main setup function."""
    print("=" * 50)
    print("Stress Level Prediction Project")
    print("Environment Setup Script")
    print("=" * 50)
    print()
    
    # Check system
    system = platform.system()
    print(f"Detected system: {system}")
    
    # Check conda
    if not check_conda():
        sys.exit(1)
    
    # Create environment
    if not create_environment():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Install conda packages
    install_conda_packages()
    
    # Install Jupyter kernel
    install_jupyter_kernel()
    
    print("\n" + "=" * 50)
    print("Setup completed successfully!")
    print("=" * 50)
    print()
    print("Next steps:")
    print("1. Activate the environment:")
    print("   conda activate stress_prediction")
    print()
    print("2. Start Jupyter Notebook:")
    print("   jupyter notebook")
    print()
    print("3. Or start Jupyter Lab:")
    print("   jupyter lab")
    print()
    print("4. Available notebooks:")
    print("   - preprocess/preprocess.ipynb")
    print("   - model/lightgbm.ipynb")
    print("   - model/catboost.ipynb")
    print("   - model/xgboost.ipynb")
    print("   - model/randomforest.ipynb")
    print("   - model/ensemble.ipynb")
    print()

if __name__ == "__main__":
    main() 