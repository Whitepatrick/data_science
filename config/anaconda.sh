#!/bin/bash

conda config --set always_yes true
conda create -n test python
source /opt/conda/bin/activate test

conda install pandas
conda install matplotlib
conda install scipy
conda install scikit-learn
conda install numpy
conda install ipython
