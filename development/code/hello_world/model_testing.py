import os
import sys
import yaml
import json
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# read from command line
data_path = sys.argv[1]
model_path = sys.argv[2]

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

def run_model_evaluation(X_var, y_var):
    # R-squared scores
    r_squared = results.score(X_var, y_var)
    return r_squared


# Evaluate model for X_train, y_train
r_squared_train = run_model_evaluation(np.array(X_train).reshape(-1, 1), np.array(y_train))

# Evaluate model for X_test, y_test
r_squared_test = run_model_evaluation(np.array(X_test).reshape(-1, 1), np.array(y_test))

#save evaluation of models
json_scores = {}
json_scores['r_squared_train'] = r_squared_train
json_scores['r_squared_test'] = r_squared_test

# save scores
with open(os.path.join(model_path,'r_squared_values.json'), 'w') as f:
    json.dump(json_scores, f)
