   This repo contains code snippets written in python.
   Tools needed:
   1. git
   2. pytest
   3. pylint


   How to install tools:
   ---------------------
   1. Git:
   ~~~~
   TODOOOO: Need to update this ;-).
   ~~~~

   2. Pytest:
   ~~~~
   pip install -U pytest
   sudo pip install -U pytest
   ~~~~

   3. Pylint:
   ~~~~
   sudo apt-get install pylint
   python coding standards explained here: https://www.python.org/dev/peps/pep-0008/
   ~~~~


   How to run tools:
   -----------------
   1. git:
   ~~~~
   git init
   git config user.name dh****ju
   git config user.email dh*********ju@gmail.com
   git remote add origin https://github.com/dhanuhangout/python.git
   git pull origin master
   git add <filename.py>
   git commit -m "Message the reason for commit"
   git push -u origin master
   ~~~~

   2. pytest:
   ~~~~
   py.test test_factorial_v1.py
   ~~~~

   3. pylint:
   ~~~~
   pylint programs/factorial.py
   ~~~~


   How to pull this repo:
   ----------------------
   ~~~~
   mkdir dh****ju
   cd dh****ju
   ~~~~


   How to push a change to repo:
   -----------------------------
   1. Edit a file with your change and save it.
   2. Add file to staging: git add ****.py
   3. Commit the change: git commit -m "Message that explains the reason of change in file."
   4. Push change to master: git push origin master


   Some Notes:
   -----------
   1. Since, dhanraju repo is ahead of dhanuhangout; Followed below procedure to update dhanraju master branch:

   - Create a folder with dhanuhangout user and ha*******10@gmail.com email.
   ~~~~
   mkdir dhanuhangout_python
   cd dhanuhangout_python
   git init
   git config user.name dhanuhangout
   git config user.email ha********10@gmail.com
   ~~~~
   - Pull master branch of dhanraju (Remember not dhanuhangout, though the user is
   dhanuhangout).
   ~~~~
   git remote add origin https://github.com/dhanraju/python.git
   git pull origin master
   ~~~~
   - Edit file
   ~~~~
   git add Readme.txt
   ~~~~
   - login to github.com with user dhanraju and all dhanuhangout in
   settings->collaborators and then sign out.
   - login to github.com with user dhanuhangout and accept invitation from
   dhanraju.
   - Now commit the code.
   git commit -m "Sync to dhanraju master branch with dhanuhangout user and
   uploading all files to dhanuhangout master branch"
   git push -u origin master


   Some more notes:
   ----------------
   - As we know, if a file get modified; then the status of it is "modified". If
   want to revert this modified file, use command "git checkout <file name>
   - If a file get added and not commited, then to revert that modified file, run
   "git reset" and then "git checkout <file name> commands.





   Merging two master branches:
   ----------------------------
   - Both dhanuhangout/python and dhanraju/python remote names are origin and both are respective master branches. Here dhanraju/python is fork of dhanuhangout/python.
   - Permissions: dhanuhangout have collaborations permissions to dhanraju/python master (which was given permissions through github.com under dhanraju account).
   - Create a folder, initialize git with dhanuhangout credentials.
   - Now, do git remote add origin of dhanraju/python.git.
   - Pull git repo.
   - Now, remove origin "git remote rm origin"
   - Do git remote add origin of dhanuhangout/python.git.
   - Pull git repo. Observer there is some difference in Readme.txt file. Since it is the only file that has difference between both masters.
   - Add Readme file, commit it and push it to origin master.


   ~~~~
   git init
   git config user.name dhanuhangout
   git config user.email hangouttest10@gmail.com
   git remote -v
   git remote add origin https://github.com/dhanraju/python.git
   git pull origin master
   git remote rm origin
   git remote add origin https://github.com/dhanuhangout/python.git
   git pull origin master
   git add Readme.txt 
   git commit -m "Attempt to push dhanraju master to dhanuhangout master."
   git push -u origin master
   ~~~~





   Before: (@dhanuhangout github graph)
   -------
   ~~~~
   dhanuhangout    *-----*-----*-----*------------------------------*
                                     |
   dhanraju                          *-----*-----*-----*-----*
   ~~~~

   After: (@dhanuhangout github graph)
   ------
   ~~~~
   dhanuhangout    *-----*-----*-----*------------------------------*
                                     |                             /
                                     -----------------------------*

   (@dhanraju github graph)
   dhanraju    *-----*-----*-----*-----*-----*-----*-----*-----*
                                 |                             
   dhanuhangout                  -----------------------------*----->*
   ~~~~


**Pylint for Google python style**

Ref: https://google.github.io/styleguide/pyguide.html


**Install googletest**
Ref: https://github.com/google/googletest/tree/main/googletest

**cmake install**
https://askubuntu.com/questions/610291/how-to-install-cmake-3-2-on-ubuntu