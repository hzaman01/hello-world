import os
import sys
import yaml
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# read from command line
data_path = sys.argv[1]
output_path = sys.argv[2]

# create output path
os.makedirs(output_path, exist_ok=True)

# load train-test size parameter
params = yaml.safe_load(open('params.yaml'))['model_development']
numerical_columns_as_features = [item+'_transformed' for item in params['numerical_columns_as_features']]
#categorical_columns_as_features = [item+'_transformed' for item in params['categorical_columns_as_features']]

# load data
X_train = pd.read_csv(os.path.join(data_path, 'X_train.csv'))#['X']#,header = None)
y_train = pd.read_csv(os.path.join(data_path, 'y_train.csv'))#['y']#,header = None)

# build model
#X_train = X_train[numerical_columns_as_features]#+categorical_columns_as_features]

results = LinearRegression().fit(np.array(X_train).reshape(-1, 1), np.array(y_train))
print(results)
model_int = results.intercept_
model_slope = results.coef_[0]
print("Model intercept is " + str(model_int) + " and model slope is " + str(model_slope))

# save model
with open(os.path.join(output_path, 'linear-regression-model.pkl'),'wb') as f:
    pickle.dump(results, f)
