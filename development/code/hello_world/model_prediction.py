# -*- coding: utf-8 -*-
import os
import sys
import yaml
import json
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# read from command line
data_path = sys.argv[1]
model_path = sys.argv[2]
mapping_path = sys.argv[3]

# load train-test size parameter
params = yaml.safe_load(open('params.yaml'))['model_development']
numerical_columns_as_features = [item+'_transformed' for item in params['numerical_columns_as_features']]
#categorical_columns_as_features = [item+'_transformed' for item in params['categorical_columns_as_features']]

# load data
X_train = pd.read_csv(os.path.join(data_path, 'X_train.csv'))
y_train = pd.read_csv(os.path.join(data_path, 'y_train.csv'))
X_test = pd.read_csv(os.path.join(data_path, 'X_test.csv'))
y_test = pd.read_csv(os.path.join(data_path, 'y_test.csv'))

# read model
with open(os.path.join(model_path, 'linear-regression-model.pkl'),'rb') as f:
    results = pickle.load(f)

def get_prediction(X):
    prediction = results.predict(X)
    return prediction

# calculate rating for X_train and save csv
pd.merge(X_train, pd.DataFrame(get_prediction(X_train)),right_index=True, left_index=True).to_csv(os.path.join(model_path, 'prediction_train.csv'), index=False)
pd.merge(X_test, pd.DataFrame(get_prediction(X_test)),right_index=True, left_index=True).to_csv(os.path.join(model_path, 'prediction_test.csv'), index=False)