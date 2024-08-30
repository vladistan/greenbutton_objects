#!/bin/bash

pipx install pre-commit

cd /workspaces/greenbutton_objects
git status && pre-commit install

python -m pip install '.[dev]'
python -m pip install -e .

git status && pre-commit run -a
