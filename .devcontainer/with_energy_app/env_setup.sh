#!/bin/bash

# Clone home energy app
git clone https://github.com/vladistan/home-energy-analysis-tool.git ../home-energy-analysis-tool

# Set up the environment for the home energy app
cd ../home-energy-analysis-tool/rules-engine
pip install -e .
pip install -r requirements-dev.txt

Run the setup script from default container
echo "----------------- Setting up Greenbutton library envrionment -------"
.devcontainer/env_setup.sh
