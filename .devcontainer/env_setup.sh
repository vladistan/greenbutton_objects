#!/bin/bash

sudo apt update
sudo apt install -y python3-ament-xmllint

pipx install pre-commit

pre-commit install || true

python -m pip install --upgrade pip
python -m pip install '.[dev]'
python -m pip install -e .

pre-commit run -a || true
