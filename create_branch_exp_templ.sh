#!/bin/bash

set -e

custom_branch_name="$1"

if ! [ -d "experiments" ]; then
    mkdir "experiments"
fi

if git branch --show-current2 2> /dev/null; then
    branch_name=$(git branch --show-current)
elif [ -n "$custom_branch_name" ]; then
    branch_name="$custom_branch_name"
else
    echo "Enter current branch name"
    read branch_name
fi

exp_folder="experiments/$branch_name"

if ! [ -d "$exp_folder" ]; then
    mkdir "$exp_folder"
fi

#overwrite
if [ -d "$exp_folder/template" ]; then
    echo "deleting existing template"
    rm -rf "$exp_folder/template"
fi

mkdir "$exp_folder/template"
echo "copying src/conf/"
cp -r src/conf/* "$exp_folder/template"

