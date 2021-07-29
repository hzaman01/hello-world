import os
import sys
import yaml
import psutil
import pandas as pd
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold

# read from command line
data_path = sys.argv[1]
output_path = sys.argv[2]

# create output path
os.makedirs(output_path, exist_ok=True)

# load train-test size parameter
params = yaml.safe_load(open('params.yaml'))['sampling']
test_size = params['test_size']

# import data
temp = pd.read_csv(os.path.join(data_path, 'sample_dataset_saved.csv'), iterator=True, low_memory=False, chunksize=100000)
df_raw = pd.concat(temp, ignore_index=True)

X = df_raw['X']
y = df_raw['y']

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=7)

#free up memory
del temp, X, y

# convert y_train and y_test to dataframes
y_train = y_train.to_frame()
y_test = y_test.to_frame()
X_train = X_train.to_frame()
X_test = X_test.to_frame()

# save data
X_train.to_csv(os.path.join(output_path, 'X_train.csv'), index=False)
X_test.to_csv(os.path.join(output_path, 'X_test.csv'), index=False)
y_train.to_csv(os.path.join(output_path, 'y_train.csv'), index=False)
y_test.to_csv(os.path.join(output_path, 'y_test.csv'), index=False)