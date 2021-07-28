# Clone and run an existing model (Hello World)

## Prerequisite
1. You have a GitHub repository that you can push to and is set to private. For many the quickest path to this is by createing a repository under your GitHub username (just remember to keep it private).
2. You'll need a *GitHub Personal Access Token* that can be used on McK-Private and McK-Internal (if the repository you intend to push to is under your GitHub username)

For more information specific around this model, read the [README_Hello_World.md](README_Hello_World.md)

## Tutorial steps
1. Navigate to Platform McKinsey [MEW Sandbox VM](https://linuxvm-c0a9409a-943c-42b5-89d9-0d551f144411.ncod.mckinsey.com/jupyterhub/lab?)
2. Access or create a personal folder under "/work/RD_Team"
```
cd work/RD_team/[your_name]
```

3. If you haven't already, clone the Hello World repo (you'll use your McKinsey email and *GitHub Personal Access Token* for your password)
```
git clone https://github.com/McK-Private/MEW_inv_model_helloworld.git
```

4. CD into the directory
```
cd hello_world_model
```

5. The project/model you've cloned down includes it's own configuration files for Git and DVC (S3). Since the DVC configuration is setup for the Sandbox VM you won't need to edit it for this tutorial, but you would if using it on any other VM than Sandbox. As for Git configuration, you'll want to edit that to point to your own repository. 

```
git config user.name "Your Name"
git config user.email "your_name@mckinsey.com"
git remote set-url origin https://github.com/your_name-mck/your-repository.git
```

6. As we know, models work in coordination with a host of libraries and to better manage them we encourage everyone to use Conda Environments (Note Platform McKinsey supplies you with a couple Conda Environments but it will also update those periodically so to have full control it is best to clone those and establish your own). Ideally any model you clone will include a list of required librarires and/or point you to a Conda Environment that has already been setup for the given model. For this tutorial we can use mew-v1.
```
conda activate mew-v1
```

You should also see the (defaul) at the head of the line prompt switch to (mew-v1).

7. Not required but always fun, you can view the project DAG which displays all the states of all the pipelines in the project.

```
dvc dag
```

If your terminal doesn't automatically exit you can aways type *q*.

8. So now we can get back to our fun and run all pipelines
```
dvc repro --all-pipelines
```

You'll see an error that /development/data/raw could not be found. That's because what we've done to this point is only copy the code and related files but not the data. GitHub is not designed to track derived output nor data and will simply block large data files. Luckily MEW with the help of DVC captures project data and stores it on S3. So what we need to do now is populate the data (This process actually looks to any .dvc files and dvc.lock files in the project and tracked in GitHub and follows the links to S3 to pull down the appropriate data). To pull data from S3 we run:
```
dvc pull
```

9. You'll see the various data files downloaded to the project (you'll also notice that the development/data/raw.dvc file has been replaced with a raw folder with various data files)

10. You can now run all your pipelines
```
dvc repro --all-pipelines
```

You'll notice that many of the stages are skipped as nothing has changed since this model was run and committed to GitHub

11. To make it more exciting, let's force all the pipelines to run

```
dvc repro --all-pipelines -f
```

12. This time you won't see any stages were skipped and you'll be prompted to push your data to remote storage. Since Sandbox is already setup in cordination with S3 for this particular VM you can simply run:
```
dvc push
```

13. Now lets make a real change to the model by changing a paramater. But before we do that we should practice good Git Flow and make a branch to do our work
```
git checkout -b [new branch name]
```

14. Not that this is necesary but it is reassuring to see which branch you're on:
```
git branch
```

15. Happy, let's make a minor change by navigating to the params.yaml file:
```
cd development/code/hello_world/
```
16. Open the params.yaml file and take a zero off the "size_cutoff: 100000"

17. Save the file

18. Instead of giving the command to run all pipelines, let's select just one (which also happens to be the only one in this project).

Since we're already in the same directory with the dvc.yaml file we can simply run:
```
dvc repro
```

Or if we navigate back to the project root we just need to add the path to the dvc.yaml file:
```
dvc repro /development/code/hello_world/dvc.yaml
```

19. After the pipeline has run you'll see onscreen prompts to track the updated dvc.lock file and push your data to remote storage.
```
git add development/code/hello_world/dvc.lock
dvc push
```

20. You have now made a minor change to the model that has effected the data as well as the code (params.yaml) and you want to save that work. We've already pushed the data to remote storage, so let's now push the code and namely the params.yaml file and dvc.lock file (which has references to all the changed data on S3).

Check in changes (the period means you'll be checking in all the changes)
```
git add .
```

Commit the change with a comment provided
```
git commit -m "user-input-comment"
```

Can now push to the repository
```
git push
```

Being this is the first time you've pushed your new branch you'll be asked to use a longer command:
```
git push --set-upstream origin master
```

You'll likely be prompted for your username and password (make sure to use a *GitHub Personal Access Token* that works with the GitHub repro you're pushing to)

21. Congratulations you've just run through the basics of MEW. Now try cloning your version of Hello World from your repository to Sandbox.