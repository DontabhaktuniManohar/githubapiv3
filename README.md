# Support and Maintenance Pipeline scrpts
This repo contains scripts and/or pipelines for the EPIC DevOps Maintenance Pipelines

A Pull Request references two branches. The base branch is the merge target. Usually this is the master branch of the repository.

base.label is github:master, meaning it's the master branch for > github/gitignore.
base.ref is the branch name "master".
base.sha is the current SHA of that branch.
The head branch is what you're merging into the base.

head.label is fidelski:add-obvious-autotools-files, meaning it's the add-obvious-autotools-files branch for fidelski/gitignore.
head.ref is the branch name add-obvious-autotools-files.
head.sha is the current SHA of that branch..
