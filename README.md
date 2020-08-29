# Aimeos Documentation

Everyone is invited to improve the documentation! :-)

Just fork the repository (upper right corner of the page), edit and add files, commit your changes and create
a pull request. Read on, if you want to know, how to setup a git workflow as well as a local live-reloading
server.

Thank you and enjoy!

## Setting up a git workflow

- Create a free github account, if you do not already have one
- Go to `https://github.com/aimeos/aimeos-docs` and fork the repo (click on the "Fork" button on the top right)
- In your terminal, clone the forked repo to a destination of your choice with:

  ```bash
  > git clone https://github.com/[YOUR-GITHUB-ACCOUNT]/aimeos-docs.git
  ```

  This creates a folder called `aimeos-docs`.

- Change into your newly created local `aimeos-doc` folder and add upstream links to be able to always keep your  clone up-to-date:

  ```bash
  > cd aimeos-doc
  > git remote add upstream git://github.com/aimeos/aimeos-docs.git
  ```

  You can verify your git configuration using `git remote -v`:

  ```bash
  > git remote -v

  origin https://github.com/<YOUR_GITHUB_REPO>/aimeos-docs.git (fetch)
  origin https://github.com/<YOUR_GITHUB_REPO>/aimeos-docs.git (push)
  upstream git://github.com/aimeos/aimeos-docs.git (fetch)
  upstream git://github.com/aimeos/aimeos-docs.git (push)
  ```

  Keep your local clone and yur fork up-to-date with:

  ```bash
  > git fetch upstream
  > git merge upstream/master master
  ```

  Optional:

  ```bash
  > git rebase upstream/master
  ```

- For each change you would like to commit, create and checkout a new branch, e.g.:

  ```bash
  > git checkout -b <name-of-your-current-commit-branch>
  ```

- Edit the mardown files you wish to contribute to and push them to your fork:

  ```bash
  > git push -u origin <name-of-your-current-commit-branch>
  ```

- Go to your aimeos-docs fork in your github account and create a [pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request ).

- Once your are finished with your commit, don't forget to switch back to the master branch in your local clone:

  ``` BASH
  > git checkout master
  ```

- Once your commit is merged, you can delete your local and remote branches again with:

  ```bash
  > git branch -d <branch_name>
  > git push origin --delete <branch_name>
  ```

  Then update your local clone and your github fork again with:

  ```bash
  > git fetch upstream
  > git merge upstream/master master
  ```

## Build and live reload your local clone (optional)

Contributing to `aimeos-docs` does not require anything else but editing the markdown
files. However, if you would like to run a local version of the generated docs, you
need Python 3. This enables the local generation of the complete `aimeos-docs` as well
as running a local development server that reloads automatically as soon as changes
to the repository files are detected.

### Install Python 3

Please refer to sources on the internet for explanations on how to install python 3 on
your operating system. One such resource would be [Real Python: Installing Python](https://realpython.com/installing-python/).

### Install mkdocs and required dependencies

`aimeos-docs` uses [mkdocs](https://www.mkdocs.org/) to create static html files from
markdown files. Install `mkdocs` and the dependencies required by `aimeos-docs` with `pip`:

```bash
pip install mkdocs material
```

#### Start the local server

Run `mkdocs serve` to start a local server on `http://127.0.0.1:8000`. Now, whenever
you make changes to any file, the server will automatically reload and display the new
version. (Hint: If you come from webpack or any similar setup, be aware that this process
takes quite a bit longer then you might be used to.)

#### Build the docs

To build the `aimoes-docs` locally, use `mkdocs build`. You can now open the documentation
in your browser from the newly generated `<your-aimeos-docs-clone-folder>/docs`'s index.html.
