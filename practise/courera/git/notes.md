VCS - Version Control System
SCM - Source Control Management

$ git config
Telling the git who we are.
git config --global user.email "me@example.com"
git config --global user.name "My name"
The flag --global sets the value to all the repositories that we'd use. The user name and email will appear in public commit logs. We can modify this to private also.

Two ways to create a repo:
(1) $ git init
Creating the repo from scratch. It creates .git directory in the current directory. This is called a Git directory. It stores the changes and the change history. We don't touch them directly, we always interact with them through git commands. 

(2) $ git clone
Make a copy of repo that already exists. It copies the .git directory to your computer.

The aread outside the git directory is the working tree. The working tree is the current version of your project.

$ git add
Staging area (index) - A file maintained by Git that contains all of the information about what files and changes are going to go into your next commit.

$ git status
Gets some information about the current working directory and pending changes.

$ git commit
$ git commit -m "Commit reason description." 
Add the reason as message for the change. You can add message via editor or with the flag -m.

$ git log
Displays the history of commits. And each commit information includes; identifier, author, date and time and commit message. The first line of the output refers to the commit that points to the master branch.

Summary:
Git project contains:
* Git directory - contains the history of all the files and changes.
* Working tree - contains the current state of the project.
* Staging area - contains the changes that have been marked to be included in the next commit.

Tracking files:
Snapshot - Git records the state of your project at that moment.
These snapshots make up the history of your project and its information that gets stored in the Git directory.

How the files are tracked:
Our files can be tracked or untracked.
Tracked files are part of the snapshots. While untracked files are not a part.

Each track file can be in one of three main states:
* Modified - Changes are made to file that we haven't committed yet. The changes could be adding, modifying or deleting the contents of the file.
* Staged - The modified files will become staged files when they are ready to be committed to the project. They will be part of next snapshot.
* Committed - When the files are committed, the changes are made to it are safely stored in a snapshot in the Git directory.

Skipping the staging area (No need to run git add command):
$ git commit -a
A shortcut to stage any changes to tracked files and commit them in one step.

In staging area, we can have several changes in one commit. And if we know that there is no other changes to commit, then we can skip this staging area by passing -a flag to the git commit command. This flag automatically stages the every file that we added/modified before doing the commit letting it skip the git add step.

Git uses the HEAD alias to represent the currently checked-out snapshot of your project.


$ git log -p
p stands for patch. The flag provides additional information about the actual lines that changed in each commit.

$ git show
Will display the information about the commit and the associated patch.

$ git show --stat
This will cause git log to show some stats about the changes in the commit (like lines of code added/removed).


* Undoing changes before committing:

$ git checkout
Undoing changes before committing.

$ git reset HEAD modified_file.py
The modified_file.py will become untracked from the list of tracked (modified) files.

$ git reset -p 


* Amending Commits

git commit --ammend 
Overwrites the current modified files to the previous commit.

* Rollbacks

$ git revert HEAD
Rolls back the latest commit on HEAD to previous commit. It creates a new commit with the inverted files and we need to add the description for "Reason for Rollback".

* Identifying the commit


Branch - A pointer to a particular commit.
Master - The default branch that git creates for you when a new repository is initialized. It is commonly used to represent the known good state of a project.

# Creating New Branches
When you want to develop a feature or fixing a bug without worrying about messing up the current working state; create a new branch and do development then merge back into the master branch. 

Example commands for developing new feature and add it to the master
$ cd repo
Look for any files are modified or it is clean.
$ git branch
Terminal output: * master
The output refers to no files are modified or it is clean.
* Creating new branch for the feature to develop
$ git branch new-feature
* Look for any files or branches are modified/created.
$ git branch
Terminal output:
* master
  new-feature
From the output, the '*' symbol refers to the branch that we are currently in. We need to move to new-feature branch.
* Checkout the new-feature branch - to check out the latest snapshot for both files and for branches. Let's switch our branch to new-feature branch.
$ git checkout new-feature
Terminal output: Swithed to branch 'new-feature'
Now, list the files/branches and make sure the '*' symbol refers to new-branch.
$ git branch
Terminal output:
  master
  * new-feature
Creating a branch and switching to it is very common. So, use '-b' flag to do both at the sametime.
$ git checkout -b even-better-feature
Terminal output:
Switched to a new branch 'even-better-feature'

Deleting a branch
$ git branch -d new-feature

# Merging
The term that Git uses for combining branched data and history together.

$ git merge - lets us take the independent snapshots and history of one Git branch, and tangle them into another.

Example flow:
First check that we're in master branch, then merge the even-better-feature branch into it.
$ git branch
Terminal output:
  even-better-feature
  * master
In the above terminal output, the * confirmed that we are in master branch. Now, we need to merge even-better-feature branch into the master branch.
$ git merge even-better-feature
Terminal output:
Updating 7d1..443
Fast-forward
 new_file.py | 6 ++++++
 1 file changed, 6 insertions(+)
 create mode 100644 new_file.py

Git uses two different algorithms to perform a merge: fast-forward and three-way merge.
Above example is the fast-forward merging.
The merge occurs when all the commits in the checked out branch are also in the branch that's being merged.
* --- * --- * --- *
                  ^
                  |
                Master
                even-better-feature

A three-way merge is performed when the history of the merging branches has diverged in some way, and there isn't a nice linear path to combine them via fast-forwarding.
* --- * --- * --- *
      | --- * --- |
            ^     ^
            |     |
         even-   Master
       better-feature

# Merge Conflicts
Both the branches we're trying to merge have edits on the same part of the same file. This will result in something called a merge conflict.

Example flow:
In the master branch, update line #5 in old_file.py, save it, commit the change.
$ git commit -a -m "Add comment to function."

Checkout to even-better-feature branch, update the same line (line #5) in old_file.py, save it, commit the change.
Swith to the other branch.
$ git checkout even-better-feature
UPDATE THE FILE, then commit the change.
$ git commit -a on "Print everything ok"

Now checkout the master branch and try to merge the even-better-feature branch.
$ git checkout master
$ git merge even-better-feature
Terminal output:
Auto-merging old_file.py
CONFLICT(content): Merge conflict in old_file.py
Automatic merge failed; fix conflicts and then commit the result.

To know more about the conflict, use git status. Let's open the merge conflict file old_file.py. Git automatically shows which parts of the code are conflicting from both the branches with the meger markers. It is up to us which one to keep and which one to remove. If we want to keep both changes, then just remove merger markers and save the file.
Now commit the file.
$ git commit

The commit message will be automatically generated as
"Merge branch even-better-feature
Kept lines from both branches."

$ git log --graph --oneline