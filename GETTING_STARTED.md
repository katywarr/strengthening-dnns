# Getting Started

These instructions have not been fully tested. They will be more robust when the book goes live in August.

## Clone this repository

Navigate to the folder that you would like to store this repository in and clone the repository.

```
git clone git@github.com:katywarr/strengthening-dnns.git
```
To keep up-to-date with any changes to the repository:

```
cd strengthening-dnns
git pull
```

# Setting up your environment with Anaconda

The Anaconda package contains python and many of the required dependencies for this project.
Instructions for downloading it are [here](https://docs.anaconda.com/anaconda/install/)

In recent versions of Anaconda, it is recommended that you do *not* select the option to add 
the Anaconda bin folder to your PATH during installation but use the Anaconda Prompt.

## Using the Anaconda Prompt 

On windows: Click start and start typing "Anaconda" to get the prompt.


## Create a virtual Python environment (one-time)

From within an Anaconda command prompt, navigate to the `strengthening-dnns` folder and
create a virtual environment using the following command: 

*You only need to do this once.*

```
conda env create -f strengthening-dnns.yml 
```

If you have a GPU on your machine, use: 

*TODO: The GPU environment is not available yet*
```
conda create -n strengthening-dnns-gpu 
```

Whenever you want to use this environment, invoke:

```
conda activate strengthening-dnns
```

or, if you selected the gpu option:

```
conda activate strengthening-dnns-gpu
```
For all the following commands, replace `strengthening-dnns` with `strengthening-dnns-gpu` if you are using the 
gpu option.

Your prompt should now look like this:

```
(strengthening-dnns) C:\current_dir>
```

## Create an IPython kernel for the Conda environment (one time) 

From within an Anaconda Command Prompt, ensure that you are within the correct environment. 

```
conda activate strengthening-dnns
```

Create the Kernel
```
pip install jupyter
python -m ipykernel install --user --name strengthening-dnns --display-name "Python (strengthening-dnns)"
```

# Running the code


## Create an IPython kernel for the Conda environment (one time) 

From within an Anaconda Command Prompt, ensure that you are within the correct environment 

```
conda activate strengthening-dnns
```

Navigate to the folder containing the clone of this repository and type:

```
jupyter notebook
```

Here's a good [introduction to Jupyter notebooks](https://jupyter-notebook-beginner-guide.readthedocs.io)



