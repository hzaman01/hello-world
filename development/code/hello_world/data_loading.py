# import the required libraries
import os, sys, yaml
import pandas as pd

# read from command line
data_path = sys.argv[1]
output_path = sys.argv[2]

# create output path
os.makedirs(output_path, exist_ok=True)

# load size parameter for length of sample dataset
params = yaml.safe_load(open('params.yaml'))['data_raw']
size_cutoff = params['size_cutoff']

# alternative by inference from small sample:
df_raw = pd.read_csv(os.path.join(data_path, 'sample_dataset.csv'), nrows=2*size_cutoff, low_memory=False)

# take certain length of full dataset as sample
if size_cutoff<0:
    df_sample = df_raw
else:
    df_sample = df_raw.sample(n=min(len(df_raw),size_cutoff), random_state=7)
    del df_raw # free up memory

# save sample dataset
df_sample.to_csv(os.path.join(output_path, 'sample_dataset_saved.csv'))
