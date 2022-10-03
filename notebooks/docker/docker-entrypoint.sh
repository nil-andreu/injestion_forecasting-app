#!/bin/bash

# Script to install Linux System Tools and Basic Python Components
apt-get update   # updates the package index cache
apt-get upgrade -y    # updates packages

# Installation of system tools
apt-get install -y bzip2 gcc git
apt-get install -y htop screen vim wget
apt-get upgrade -y bash
apt-get clean   # cleans up package index cache

# Installation of miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh -O Miniconda.sh   # download of miniconda
bash Miniconda.sh -b    # installation of miniconda
rm -rf Miniconda.sh
export PATH="/root/miniconda3/bin:$PATH"  # pre-pends the path

# Install the packages needed with conda
# conda create -n environment python=3.8
# conda activate environment
# conda init bash

# conda run -n environment /bin/bash -c

conda install -y jupyter
conda install -y jupyterlab
conda install -y numpy
conda install -y pytables
conda install -y pandas
conda install -y scipy
conda install -y matplotlib
conda install -y seaborn
conda install -y quandl    # wrapped for Quandl data API
conda install -y scikit-learn
conda install -y openpyxl
conda install -y xlrd xlwt   # for excel interaction
conda install -y statsmodels
conda install -y pystan=2.17.1.0 convertdate holidays
# conda install -c conda-forge -y fbprophet
conda install -c conda-forge -y dtale


# Install packages with pip
pip install --upgrade pip
pip install q    # for logging and debugging
pip install plotly
pip install cufflinks   # combining plotly with pandas
pip install tensorflow
pip install keras
pip install eikon    # Python wrapper for Refinitiv Eikon Data API
pip install yahoo_fin
pip install pmdarima
pip install prophet
pip install neuralprophet
pip install yahoofinancials
pip install pandas-datareader
pip install requests_cache
pip install quandl
pip install iexfinance
pip install openai

# And special installation for scrapping Twitter
pip install --user --upgrade \
    'git+https://github.com/twintproject/twint.git@origin/master#egg=twint'

# pip install git+git://github.com/yhilpisch/tpqoa    # Python wraper for Oanda API
