#!/bin/bash


STARTUP_DIR=$(pwd)

python -m pip install -U pip

# Clone home energy app
if [ ! -d "../home-energy-analysis-tool" ]; then
  git clone https://github.com/vladistan/home-energy-analysis-tool.git ../home-energy-analysis-tool
fi

# Set up the environment for the home energy app
cd ../home-energy-analysis-tool/rules-engine
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
python -m pip install -e .

# Run the setup script from default container
echo "----------------- Setting up Greenbutton library envrionment -------"
cd $STARTUP_DIR
.devcontainer/env_setup.sh
