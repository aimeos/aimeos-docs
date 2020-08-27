Aimeos is hosted on Github which uses the "git" version control system to keep track of changes. If you would like to contribute to the Aimeos code base, this page contains a step by step description of what you have to do. For a detailed documentation about Git, please have a look at: <https://git-scm.com/doc>

# Create a Github account

First of all, you have to register yourself at Github. This is totally free of charge and is necessary to be able to create your own git repositories on Github or fork existing repositories like the Aimeos one. Please [create an account](https://github.com/join) before proceeding to the next step.

# Fork the repository

After you've signed up, login into your account at Github and go the [Aimeos page](https://github.com/aimeos/aimeos-core). You can browse the source code at this stage and the next step is to fork the Aimeos repository. Creating a fork clones the existing repository and creates a new one for you. In this repository, you will be able to make changes. To start the fork process, press the "Fork" button in the upper right corner.

# Local copy of your fork

You can edit files directly in your fork. For bigger changes, create a local version and work with your favourite editor. You can do this by creating a clone of your repository on Github using the git command line tool:

```bash
git clone https://github.com/[your-account]/aimeos-core.git aimeos-core
```

Please replace "\[your-account]" with your account name before executing the command. After the command has finished, a clone of the complete repository will be available in the "aimeos-core" directory on your local hard drive.

# Automatic builds (optional)

To be sure that your changes don't break existing tests, you can use the [Travis CI](https://travis-ci.org/) build service to automatically test them on every push to your fork.

To get started with Travis CI, sign in through GitHub by following the Sign-In link at the top of the Travis CI website. Github will ask you for granting read and write access. Travis CI needs write access for setting up service hooks for your repositories, when you request it, but it won't touch anything else.

Once you're signed in, go to your profile page on Travis CI. You'll see a list of your repositories. Flip the on/off switch for each repository that you want to hook up on Travis CI. Then visit the Github service hooks page for that project and paste your Github username and Travis token into the settings for the Travis service, if it is not already pre-filled.

That's it! Now every push to the repository will start a build on Travis CI. You can view the output of the tests on

<https://travis-ci.org/[your-account]/aimeos-core>

when you replace "[your-account]" with the name of your Github account. Before we will merge your changes to the main repository, we will wait for the result of the Travis CI build.

# Daily work with git

## Update the repository

After the steps to create a local repository, you can start changing the code or adding new features. An important thing before you do any changes is to update your local repository because in the meantime other developers may have implemented features or corrected bugs as well. If you are using an outdated code base chances are high that you will get conflicts if someone else changed the same lines of code or you are hunting a bug that was already fixed. The time for both is better spent for other things for sure :-)

To update your code base prior to every change enter the following commands on the command line:

```bash
git pull && git pull https://github.com/aimeos/aimeos-core.git
```

The line consists of two git commands: The first one fetches all updates from your fork and merges them into your local repository while the second one does the same for all changes available from the main Aimeos repository. Especially the second one is extremely important as it's very likely that someone else has integrated a change into the main repository.

## Commit changes made

Every time you've finished a change (which may consist of a series of small changes that belong together) you should commit your changes. At first, you have to tell git that it should add the changes to the next commit. This is done by using

```bash
git status
git add <file or folder with changes>
```

Afterwards, you can commit all added files by using:
```bash
git commit -m "<your commit message>"
```

on the command line. Please replace the message text with an english description of what your change set will do.

## Transfer changes to Github

All your changes are still on your local machine and you would like to get them integrated into the main repository for sure. Make sure that the tests are still working and the coding guidlines are met.  The first step to start integration is to push your changes to your own Github repository:

```bash
git push
```

This transfers all changes and you should see them in the code browser of your own repository on Github.

## Start a pull request

To get your changes into the Aimeos core, you have to tell us that you want to get your code into the main repository. You have to be logged into the Github website and be on the main page of your fork. Right of the name of your fork (below the top toolbar) there's a button named "Pull request". Follow the steps the create such a pull request and we will get notified about.

Maybe we find points to discuss about in your code. In this case we add our comments to the code in question. After we think that the code is good enough to be integrated, we will merge it into the Aimeos repository. That's it and you can start to implement your next feature :-)

# Remote branches

## Create a remote branch

First create a local branch:
```bash
git checkout -b <localbranch>
```

The, transfer the local branch to server:
```bash
git push origin <localbranch>:<remotebranch>
```

Or you can use:
```bash
git push -u <remote-name> <branch-name>
```

instead, so that a subsequent git pull will know what to do.

## Delete a remote branch

```bash
git push origin --delete <branchname>
```

## Getting a remote branch

```bash
git remote update
```

Retrieves all branches:
```bash
git checkout -b <local-branch-name> <remote-name>/<remote-branch-name>
```

Makes a new local branch, which tracks the remote branch.

# Git troubleshooting

In case you encounter the following error message:
```
fatal: You don't exist. Go away!
Please update your global config
```

Then set your name and e-mail in the git config file using:
```bash
git config --global user.name "John Doe"
git config --global user.email john.doe@metaways.de
```
