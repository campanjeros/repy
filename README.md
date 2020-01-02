# REPY - Tool for tagging a Python/Erlang/Elixir/JavaScript release

![REPY](https://images-na.ssl-images-amazon.com/images/I/61LEygTkpZL._SY355_.jpg)

## What is it
repy is a tool for a more standardized release behaviour.\
It generates the next version that should be used with regard to the previous
version and depending on the new release type.\
It supports versioning in the form of Major.Minor.Patch, e.g. 1.4.2 and v1.4.2\
The tool will update any file in your project which contains this version and
also create a git tag and push it to the remote repository.

### Examples
 - current version: 1.3.2 `repy patch` will generate the new version 1.3.3
 - current version: 1.3.2 `repy minor` will generate the new version 1.4.0
 - current version: 1.3.2 `repy major` will generate the new version 2.0.0

### Requirements
 - The current branch needs to be `master`
 - There can't be any uncommited or non added changes in the repository
 - `python3` and `git` needs to be installed


## Usage

### Major release
`repy Major`

### Minor release
`repy Minor`

### Patch release
`repy Patch`

### Force a specific version
`repy 3.5.1`

### Help
`repy -h`

There are other parameters to skip various checks, get more detailed output,
just perform a dry run, don't push any changes to remote etc.

## Installation
There are a few different options on how to install the tool
 - `pip install repy`, the easiest way,
   will install the tool in your current active python environment
 - Manually `clone` the repo and then either add the entire repo to the `PATH`
   or use `ln` to create a link from some user/bin dir to the repy script,
   e.g. `ln -s ~/YOUR_REPO_PATH/repy/repy ~/bin/repy`
 - `pip install ./REPY_DIR_NAME` in whatever python environment you like
   (after cloning the repo)
 - You can also skip pip and use `python setup.py install` after cloning the
   repo

### Update
How to update the tool depends on how you installed it,
if you just cloned the repo and added the repo script to your `PATH` you just
need to run `git pull`.

Otherwise you might need to run e.g. `pip install` again with
the `--upgrade` flag
