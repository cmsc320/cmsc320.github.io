# CMSC 320 Assignment 1: Introduction to Git and GitHub (Credit to Kobe Wang (kwwwv))

Welcome to your first 320 assignment!! This portion will introduce you to the basic functionalities of Git and GitHub. 


Here are some useful links that might be good to read through first
- https://towardsdatascience.com/get-git-a-primer-on-git-aa2cd1d9436f
- https://git-scm.com/docs

## Part 1: Installation

Before we begin though, make sure you have Git is installed on your system. If it isn't, follow the instructions below 

### Git Installation

- **Windows:** Download Git from [git-scm.com](https://git-scm.com/) and follow the installation instructions.
- **MacOS:** You can install Git using Homebrew by running `brew install git` in your terminal.
- **Linux:** Use your package manager to install Git, e.g., `sudo apt-get install git` for Debian/Ubuntu.

After installation, verify that Git is installed correctly by running:

```bash
git --version
```

This should display the version of Git installed on your system.

## Part 2: Creating a Local Repository

1. **Fork this repository**: Click on the "Fork" button at the top-right corner of this page. This will create a copy of the repository under your own account. 


2. **Clone your forked repository** to your local machine:

   Make sure your SSH key is set up for this step. If you don't have one set up, generate a new one with this step by step.
   https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

   ```bash
   git clone git@github.com:USERNAME/REPOSITORY_NAME.git
   ```

3. **Navigate to the repository**

   ```bash
   cd REPOSITORY_NAME
   ```
4. **Set remote for moving changes to the remote repository**

   The remote serves as an alias for where your changes are uploaded pushes and pulls.
   ```bash 
   git remote set-url origin git@github.com:USERNAME/REPOSITORY_NAME.git

   ```


## Part 3: Working with Another Branch

### Step 1: Create a New File

1. **Create a new file called `answers.txt`**: 

   ```bash
   touch answers.txt
   ```


### Step 2: Create and Switch to a New Branch

1. **Create a new branch named `q1`** and switch to it:
   ```bash
   git branch q1
   ```

2. **Switch to the new branch**:
   checkout is an old way of doing it. The more modern command you can also use it `switch`.
   ```bash 
   git checkout q1
   ```

3. **Add your answer to the first question** in `answers.txt`:
    you can use any command line text editor, if you're unsure of which to use (look below)

   ```bash
   nano answers.txt
   ```

    Now copy this question into the file and answer it 
   ```text
   Q1: Why might we consider using Git?

   Answer: [Your answer here]
   ```



4. **Stage and commit your changes**:

   The status command gets users current changes
   ```bash
   git status
   ```
   You should see changes in `red` here, these changes are `unstaged`

   Then we want to "add" our changed files into the Staging area. The staging area is a place where you gather all your changes to then be committed all at once later. 

   ```bash
   git add answers.txt
   ```
   If we run `git status` here, we will see that the changes are now `green`


   Lets go ahead and finalize our changes. This will essentially "commit" all our changes to our LOCAL repository -- this does not effect the remote repository . 

   Each commit should have a quick summary of the purpose of your changes. This an be done by using the `-m` flag followed by your commit message. If you don't using it, a text editor will open for you to type in your commit message.
   ```bash
   git commit -m "answered Q1"
   ```


### Step 3: Creating another branch 

1. **Lets Switch back to the `main` branch**:

2. **Create a new branch named `q2` and switch to it**:

3. **Add your answer to the second question in** `answers.txt`:
   ```text
   Q2: What field could data science be applied to? Give an Example.

   Answer: [Your answer here]
   ```
4. **Stage and commit your changes**:


### Step 4: Merging Branches and Resolving Conflicts

1. **Switch back to the `main` branch**:

2. **Merge the `q1` branch into `main`**:
   Merging essentially applies the changes made on a certain feature branch to the current branch its on. So in this case, we will be combining `q1` to our `main` branch
   ```bash
   git merge q1
   ```

3. Then **Merge the `q2` branch into `main`**:

   Here, you should have encountered a merge conflict, Git will inform you that there are conflicts in `answers.txt`. Open the file, resolve the conflicts manually using your command line text editor

   - `<<<<< HEAD`: signifies the beginning of your changes from the branch you are in
   - `=====`: This signifies the separation between the two merges. Anything above is the content from the first branch, everything below is from the content of the merging branch 
   - `>>>>>`: This specified the end of the conflic 

   You can resolve these conflicts by removing the 3 from above^.Make sure that you have the answer and question to both problems 
   

4. **Stage the resolved file** and commit the merge:
   ```bash
   git add answers.txt
   git commit -m "resolved merge conflict"
   ```

## Part 4: Working with Rebasing

### Step 1: Open answers.txt and copy/answer this question in main 

```text

Q3: What is the difference between Merging and Rebasing?

Answer: [Your answer here]

```

stage/commit when youre done


### Step 2: Create a New Branch

1. **Create a new branch named `q3`** and switch to it:

2. **Add your answer to the fourth question** in `answers.txt`:
   ```text
   Q4: What are you looking forward to this semester?

   Answer: [Your answer here]
   ```

3. **Stage and commit your changes**:

### Step 2: Rebase the New Branch onto `main`

1. **Switch back to the `main` branch**:
   ```bash
   git checkout main
   ```

2. **Rebase the `q3` branch onto `main`**:

   `rebase` essentially "replays" the changes that we made from out feature branch `q3` on our main branch. 

   ```bash
   git rebase q3
   ```


3. **Resolve any conflicts** 

   We didn't in this case, but if we did multiple different commits during our feature branch `q3`, we can use `--continue` to move to the next commit of out feature branch.
     ```bash
     git rebase --continue
     ```
   
   If we rebase multiple commits, but we want to discard the changes in the middle of the rebase process, we can do an `--abort` to disgard these changes. 

   ```bash
   git rebase --abort

   ```

4. **View Commits**

   ```bash
   git log
   ```

   Notice that in the log enumerates all the commits we have added in order. When we first used the `merge` command an additional commit is incurred to contain our patches. When you use `rebase` for more complex changes, there is no additional commit needed here. Instead when rebasing, your git client modifies the feature commits to be merged without conflict.

   For more information, visit here 
   - https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase
5. **Push changes to remote repository** 

   `push` allows us to upload our changes from our local repository to our remote repository on github 

   ```bash
   git push origin main
   ```





## Submission Instructions

1. **Submit a link to your github forked repository on Gradescope**





