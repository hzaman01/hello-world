# Overview of the model
This is a sample "hello world" model to help you get started with MEW. 

This model is a basic regression model, using an input file with 2 variables: X and y only. The model can be used to learn about MEW, as well as its defining backbone of Git and DVC technologies.

The current model has been coded for the development portion of the pipeline. Validation portion of the pipeline is to be developed. 

# Development pipeline code structure

In the "development" folder, you should start with "code" sub-folder. There, you will have 2 types of files: .yaml files and Python code:
1. .yaml files
    ** "dvc.yaml" file is an essential file that supports the MEW pipeline. This file indicates the steps of the pipeline ("stages"), their order, their dependencies/ inputs, and outputs. You can utilize a file in this model as your base, before developing more advanced models. Please see below for more information on how the "dvc.yaml" is structured.
    ** "params.yaml" file is a file that stores all the parameters that are called in dvc.yaml and other code files, to have a central repository for parameter valus. This set up enables efficiency in the process, if any parameters need to be changed, as the edits will be done only in this file and will automatically flow through the rest of the code. For example, in the hello world model, one of the parameters is the % split between train and test datasets. If this parameter needs to be changed, only "params.yaml" would have to be updated.
2. Python code
    ** For each pipeline stage identified in the "dvc.yaml" file, you would have a code file that runs the commands. For example, for the "data loading" phase in this model, there is a separate code file that runs the code to read in the data.


# Spotlight on the "dvc.yaml" file that defines the pipeline
This file is composed of steps, written down in the order they are to be run
In this model, there are 5 stages:
1. "data_loading": code to load the data in
2. "data_sampling": code to split up data into train and test datasets
3. "model_development": code to fit a linear regression model to data
4. "model_testing": code to check the model fit (e.g., output r_squared values)
5. "model_prediction": code to run the fitted model for prediction

You can create as many stages as you need, based on the model you are developing. The rule of thumb is to have a separate stage for each discrete step in the pipeline, to allow for faster de-bugging and faster model pipeline run time as stages that are not changed from previous run (if the pipeline is run multiple times) don't have to be run. For example, if you want to add to the basic steps above to perform data cleaning or variable engineering, you would add those steps as separate stages in the "dvc.yaml" file and create separate code files (Python or R) for them. 

For each stage, the syntax in the "dvc.yaml" file is as follows:
```
<b>data_loading:</b>
    <b>cmd:</b> 
    - python3 data_loading.py ../../data/raw ../../data/interim
    <b>deps:</b>
    - include code file to run this step (listed in cmd above as well)
    - include any input files needed to run the code
    <b>params:</b>
    - list relevant parameters from the params.yaml file needed to run this step of the code
    <b>outs:</b>
    - include output files
```