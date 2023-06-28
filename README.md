# TimeSeries_prediction

## Description
This repository contains the project developed as part of the Synthesis Project 1 course for the degree of Artificial Intelligence. The main objective of this project was to apply Artificial Intelligence techniques to reduce energy consumption based on occupation data and information from different faculties. In the folder docs, there is a pdf where there is a detalied explanation about the project.

##Repository Structure
The repository is structured as follows:

data/: This directory contains the raw and processed data used in the project.

utils/: This directory contains a 'utils.py' file where there are some functions that we will use in other files.

data_exploration.ipynb: This file contains the exploration of the initial data I was given.

constant_variables.py: This file stores some common and needed variables among the faculties that are needed to create our dataset in the 'dataset_creation.py'.

dataset_creation.py: This file creates the dataset we will use in th RNN Time Series prediction. The dataset is created from the initial datathe teachers gave me.

train_test_split.py: This file contains the function to split and process the dataset.

train_val.py: This file contains the functions to train and validate the model.

test.py: This file contains the function to test the model.

processing_model_science.ipynb: This file contains the RNN trained and evaluated.

README.md: The README file you are currently reading.
