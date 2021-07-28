# Forking a Project (Hello World)

Typically when working on a study you will be invited to a Project McKinsey VM where MEW has already been installed and to honor the separation of study data when you clone a model from the MEW Model Inventory you will actually be creating a fork. This tutorial covers the steps you will take to quickly create a fork.

## Prerequisite
1. You have a Platform McKinsey VM that is seperate to [MEW Sandbox VM](https://linuxvm-c0a9409a-943c-42b5-89d9-0d551f144411.ncod.mckinsey.com/jupyterhub/lab?)
2. You have a GitHub repository that you can push to and is set to private. For many the quickest path to this is by createing a repository under your GitHub username (just remember to keep it private).
3. You'll need a *GitHub Personal Access Token* that can be used on McK-Private and McK-Internal (if the repository you intend to push to is under your GitHub username)

For more information specific around this model, read the [README_Hello_World.md](README_Hello_World.md)

## Tutorial steps
1. Navigate to to the GitHub page for [MEW Hello World](https://github.com/McK-Private/MEW_inv_model_helloworld) or whichever model you would like to clone
2. Click on the **Code** button to copy the repository URL
3. Navigate to a terminal in your non Sandbox VM and the folder location you would like to clone the model
4. Clone the model clone the Hello World repo (you'll use your McKinsey email and *GitHub Personal Access Token* for your password)
```
git clone https://github.com/McK-Private/MEW_inv_model_helloworld.git
```
5. Now that you have a clone of the Hellow World repository on your VM you can pull the model data down as you did in the tutorial for [Clone and run an existing model](TUTORIAL_HELLO_WORLD.md)
```
dvc pull
```

6. This time however you get an error as this VM on Platform McKinsey has its own S3 bucket and the project we cloned is configured to look to the S3 bucket for Sandbox.

The expectation is when using a model from the MEW Model Inventory, that the CST is supplying their own raw data to feed the model so there is actually no need to pull the original raw data. If the expectation that the model includes some unique raw data that should be integrated with future forks of the model, the ReadMe file should supply a link to pull that file from GitHub or Box to then be uploaded to the CST's Platform McKinsey VM. 

For this tutorial we've made it easy and included the raw data file rquired for Hello World in the [/tutorial-assets/sample_dataset.csv](/tutorial-assets)

7. Copy the S3 bucket location for the new VM by navigating to [Platform McKinsey](https://platform.mckinsey.com/) and selecting the VM from the **Teams** menu

8. Click **DATA** in underneath VM name and then **Show S3 Bucket name**

9. Copy this name to your clipboard

10. In the terminal open the .dvc/config file in the vi editor
```
vi .dvc/config
```

Use the error keys to navigate to position the cursor at the end of the current S3 location. Type i to enter vi's insert mode.

![Screenshot](tutorial_assets/images/vi_position.png)

11. Enter vi's edit mode

Type **i** for inert:

```
i
```

Use back or delete key to remove current S3 location (leave "s3://") and paste in the new location.

12. Save and exit vi
```
:wq
```
Hit return key to have vi save and exit the file.

13. If you have not already, you should also edit the .git/config file by running the following commands
```
git config user.name "Your Name"
git config user.email "your_name@mckinsey.com"
git remote set-url origin https://github.com/your_name-mck/your-repository.git
```

14. Add your raw data to the project by creating a **raw** folder under **/developer/data/raw**. You can also choose to remove the raw.dvc file that is present as it is an old reference to the S3 bucket on Sandbox.

Once you have a new **/developer/data/raw** and you can run the model (if the data aligns with the model's requirements). For the tutorial you can move the [/tutorial-assets/input.xlsx](/tutorial-assets) file in the Hello World model over (either by moving it or simply downloading to your desktop and uploading).

15. Run the model
```
dvc repro development/dvc.yaml
```

16. Once the pipeline has executed you can follow the onscreen instructions to push your data, now going to the new S3 bucket
```
dvc push
```

17. You can also commit the code to GitHub

## Contributing back to MEW Model Inventory
In the course of a study if you were to improve on a model from the MEW Model Inventory we encourage you to contribute back. To maintain the seperation between a study and the MEW Model Inventory you would need to ask the MEW team for contributor rights on the model in the inventory and contribute sanitized code, then submitting a pull-request for review by the model's owner. This way we as a Firm are continually improving on our core assets.