#!/bin/bash

# Add all changes to the staging area
git add .

# Commit changes with a default commit message
git commit -m "Automated commit"

# Push changes to the remote repository (assuming the remote is named 'origin' and the branch is 'main')
git push origin master
