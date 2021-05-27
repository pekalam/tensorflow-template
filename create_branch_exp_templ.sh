#!/bin/bash

set -e

if ! [ -d "experiments" ]; then
    mkdir "experiments"
fi

exp_folder="experiments/$(git branch --show-current)"

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

