# Week 1 Lab 8/23/2022   
Today's objectives will be the following
- Downloading Anaconda/Spyder 
- Making your github repo for Unmanned Systems 
- Go over why github is cool 
- Deriving the grid equation for homework  



## Downloading Anaconda/Spyder
**WINDOWS**
Follow this link to download anaconda:
https://www.anaconda.com/products/distribution

**Linux**
DO NOT DOWNLOAD Anaconda in Linux, since we will be downloading ROS in this enviornment, if you have these two together python packages become a nightmare to organize 

Instead download Spyder only by opening up a terminal and doing the following:
```sudo apt install spyder```

## Making your github repo for Unmanned Systems 
Git and github will be useful for version control of code, if we mess up or want to revert back to a previous version we can grab an older version. Github will give us the advantage of uploading the code to the cloud, so we don't have to worry about our flashdrives frying out or if our computer bricks out. 

### Get git and create Github account
If you are on Windows, you will need to install git https://gitforwindows.org/ after you have git, create a github account  
https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2Fenterprise&source=header

### Create github_repository 
Once you have created your github account, create a github repo with the name as follows :
```
your_full_name_unmanned_systems 

#example
justin_nguyen_unmanned_systems 
```
You should have a couple of commands given to you from the website that should help you for your first push, keep that webpage on 

### Create folder repo to push to github 
Go to any folder directory in your computer and create the folders:
```
your_full_name_unmanned_systems/your_full_name_unmanned_systems/week_1

#example 
justin_nguyen_unmanned_systems/justin_nguyen_unmanned_systems/week_1
```
Add a python script inside the week_1 directory, you can name it whatever 

### Initial commit 
Open up a terminal and change to the folder directory to the top level of **your_full_name_unmanned_systems** repo 

```
#this initializes your git 
git init 

#this adds any changes to your repo 
git add . 

#make your first commit with comments 
git commit -m "Initial commit" 

#establish the main branch of your repository 
git branch -M main 

#add the github repository 
git remote add origin https://github.com/your_github_account/your_full_name_unmanned_systems.git

#push this git repo to your github repository 
git push -u origin main
```

If you check the github repo, you should it updated with your python script and the folder directories. When doing your homework coding assignments and developing code, you should save your code and use git and github to update your changes. 

## Why Git and Github is Cool

### Save as checkpoints 
A commit that is pushed can be considered a checkpoint. 
When you want to save your version of your code you do the following in your terminal, first go to folder directory, then: 
```
git add .
git commit -m "put some comment here"
git push -u origin main 
```

### Go back to previous commit 
```
# Create a backup of master branch
git branch backup_master

# Point master to '56e05fce' and
# make working directory the same with '56e05fce'
git reset --hard 56e05fce

# Point master back to 'backup_master' and
# leave working directory the same with '56e05fce'.
git reset --soft backup_master

# Now working directory is the same '56e05fce' and
# master points to the original revision. Then we create a commit.
git commit -a -m "Revert to 56e05fce"

# Delete unused branch
git branch -d backup_master

```



