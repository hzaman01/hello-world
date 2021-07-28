# Starting a new project from scratch

## Introduction
MEW relies on Git for tracking code and DVC for tracking of data (dvc.lock). You can run into issues if GitHub is tracking large data files and will block you from from pushing to GitHub if files are over the size limit. By properly constructing your dvc.yaml files and following a standard procedure you can rely on MEW to properly track all your files as we will demonstrate in this tutorial.

## Prerequisite
1. You have a GitHub repository that you can push to and is set to private. For many the quickest path to this is by createing a repository under your GitHub username (just remember to keep it private).
2. You'll need a *GitHub Personal Access Token* that can be used on McK-Private and McK-Internal (if the repository you intend to push to is under your GitHub username)

## Tutorial steps
### 1. 

## 3b. Set up access to the repository you have just cloned / created, to ensure future commits are GitHub are attributed to you (substituting your information)
```
git config user.name "FirstName LastName"
git config user.email "FirstName_LastName@mckinsey.com"
```
## 3c. Get familiar with GitFlow

To follow best Git practices, you need to utilize GitFlow (https://nvie.com/posts/a-successful-git-branching-model/). Utilizing GitFlow means downloading the repository onto a McKinsey Platform virtual machine, creating a separate branch to save any of your modifications, and sharing ("committing") your changes to the remote repository under a branch that you have created. This approach allows a repository administrator to review the changes you have made and choose to merge them into a "master" branch, once they are approved / discussed. <br>

If you create your own repository, it is still advisable to follow the GitFlow methods and update the repo through a non-master branch. This will help ensure easier fixes if one of your code changes accidentally breaks the code and will help you get accustomed to the Git Flow approach for your future projects, when you are collaborating with multiple people on the team.

<br>

The following steps can be taken to follow GitFlow, once you are in the folder you have just downloaded / created:

1. Create new branch:
```
git checkout -b [new branch name]
```

To check which branch you are on, you can utilize the "git branch" command:
```
git branch
```
![Screenshot](tutorial_assets/images/git_branch.png)

2. Make changes you need

3. Upload the amended code from your local version of the repository onto the shared link on GitHub:

```
git add .
git commit -m "add meaningful message explaining what changes you made"
git push
```

Note: if you are sending the changes to the new branch for the first time, "git push" command above will error out. You would need to use the following command instead:
```
git push --set-upstream origin master
```

![Screenshot](tutorial_assets/images/git_commit.png)
![Screenshot](tutorial_assets/images/git_push.png)

4. (For existing models that you have downloaded) Alternatively, if you don't want to share your changes to the the repository where other users may pull from, you may choose to link your repository to a different remote GitHub repo (that you or someone else have created). Such process is called forking a model. You would do that using the following command: 
```
git remote set-url origin https://github.com/your-repository.git
```

5. If you chose to create a repository from scratch instead, it would already be linked to the needed remote repository. To check which repository your local folder is linked to, you can use the following command: 
```
git remote -v
```
![Screenshot](tutorial_assets/images/git_remote_v.png)