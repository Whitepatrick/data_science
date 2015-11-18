#!/bin/bash


conda config --set always_yes true
#conda create -n data_science python

export PATH="~/anaconda/envs:$PATH"
source $HOME/anaconda/bin/activate data_science
conda install pandas
conda install matplotlib
conda install scipy
conda install scikit-learn
conda install numpy
conda install ipython
