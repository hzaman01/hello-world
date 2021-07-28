# Starting a new project from scratch

## Introduction
MEW relies on Git for tracking code and DVC for tracking of data (dvc.lock). You can run into issues if GitHub is tracking large data files and will block you from from pushing to GitHub if files are over the size limit. By properly constructing your dvc.yaml files and following a standard procedure you can rely on MEW to properly track all your files as we will demonstrate in this tutorial.

## Prerequisite
1. You have a GitHub repository that you can push to and is set to private. For many the quickest path to this is by createing a repository under your GitHub username (just remember to keep it private).
2. You'll need a *GitHub Personal Access Token* that can be used on McK-Private and McK-Internal (if the repository you intend to push to is under your GitHub username)

## Tutorial steps
### 1. Navigate to an appropriate directory (if on Sandbox that would be /work/RD_Team/your-name)

### 2. Run MEW Init to create a project.
This will setup a project folder with a base template alignign with modeling principles as well as setup git, mew, and dvc for the project.
```
mew-cli init
```

### 3. CD into the new project you just created

### 4. Update Git remote for the project by running the following commands (substituting your information):
```
git config user.name "Justin Gibbs"
git config user.email "justin_gibbs@mckinsey.com"
git remote add origin https://github.com/user-name-mck/test-temp.git
```

### 5. Check in changes, essentially your having run init
The period means you'll be checking in all the changes.
```
git add .
```

### 6. Commit the change with a comment provided
```
git push
```

### 7. Being the first time you've pushed to this repository, Git will prompt you to use a longer command:
```
git push --set-upstream origin main
```

### 8. You'll be asked for your username and password:
Username = McKinsey email which linked to your OneFirmGitHub
Password = GitHub personal access token 

If you need help with any of this, check [Required before getting started](README.md)

### 9. You've now created a workspace on the VM to build your model and primed it so that your work can easily be committed and pushed to GitHub. The next thing you want to do is start working from a git branch.
```
git checkout -b new-branch-name
```

You can ensure which branch you are on with:
```
git branch
```

### 10. You can now start buidling our your model

* Importing your source data into the developer/data/raw folder (following our modeling principles all source data should be located in raw)
* Build your pipeline(s) using dvc.yaml files and identifying parameters in the params.yaml file
* Incorporating documentation by following the [DOCUMENTATION_README.md](DOCUMENTATION_README.md)

### 11. After you've uploaded huge data files to developer/data/raw you'll want to ensure that they are tracked by MEW and not GitHub (which will likely reject them anyway)
You inform DVC to track all files in raw with a command similar to git.
```
dvc add development/data/raw
```

### 12. Then push the data to S3
Just like in Git, you'll need to actually push the data.
```
dvc push
```

### 13. Follow the onscreen prompt to alert git not to track this
```
git add development/data/raw.dvc development/data/.gitignore
```

The raw.dvc contains a reference to the data on S3. By tracking the raw.dvc file when anyone clones the project and pulling the data via **dvc pull** it will populate the project.

### 14. If you build your pipeline(s) according to the tips below when a pipeline is executed DVC will create a dvc.lock file to accompany every dvc.yaml file.

First see if your pipeline executes
```
dvc repro --all-pipelines
```

If successful you'll see an onscreen prompt to add dvc.lock to be tracked by Git. This dvc.lock file acts in the same way as raw.dvc, a pointer to the data on S3.

### 15. Since you've had a successful run of the pipeline you should also push the data to S3
```
dvc push
```

### 16. You should also push all the other files to GitHub

```
git add .
git commit -m "add meaningful message explaining what changes you made"
git push
```

Note: if you are sending the changes to the new branch for the first time, "git push" command above will error out. You would need to use the following command instead:
```
git push --set-upstream origin master
```


## Tips for builiding out pipelines in MEW
1. dvc.yaml > outs: Outputs need to be unique across pipelines so it's easier to identify specific files vs directories in outs (also can help project navigability)
2. dvc.yaml > outs > cache: In nearly all cases you should not include the cache: field. By default it's set to True, instructing DVC to track the output files
3. dvc.yaml > outs > persist: If outs direct to an existing folder, it is better to set persist to true; otherwise the folder will get purged before new files are saved
4. Metrics and plots should be saved in a machine-readable format. This likely means the same plots will need to also be saved as image files for documentation, but by having machine-readable format we ensure metrics and plots are accessible to the UI, Telemetry and future MEW features.
    1. dvc.yaml > outs > metrics: scalar numbers such as AUC, true positive rate, etc. can be saved as a JSON or YAML file. 
    2. dvc.yaml > outs > plots: data series such as AUC curves, loss functions, confusion matrices, etc. can be saved as  JSON, YAML, CSV, or TSV.