# ECSE 541: Thermal Modeling & Evaluation in 3D MPSoCs using 3D-ICE v4.0

## Project Title
**Thermal Modeling and Evaluation in 3D MPSoCs Using the 3D-ICE Simulator**

**Group Members:**: Abhishree Abhishree, Jacob St-Germain, Lucero Fuentes Ramos, Maninder Bir Singh Gulshan

## Overview
This repository contains all materials required for the project:
- Reproduction of baseline results from the 3D-ICE paper
- Extension to a custom 4-tier liquid-cooled 3D MPSoC
- Simulation outputs and visualization scripts

## Folder Structure

3d-ice/
│
├── bin/
│   └── 3D-ICE-Emulator        # Simulator executable (this can accessed from git clone https://github.com/esl-epfl/3d-ice.git)
│
├── test/
│   ├── mc4rm/
│   │   └── transient/         # Baseline (2-tier) configurations
│   │
│   ├── my_4tier.stk           # Custom 4-tier stack definition
│   ├── background_node*.txt   # Baseline temperature outputs
│   ├── my_4tier_node*.txt     # 4-tier simulation outputs
│   └── plot_thermal.py        # Plotting script
│
├── figs/
│   ├── baseline_2tier_temperature.png
│   ├── custom_4tier_temperature.png
│   └── max_temp_comparison.png
│
└── README.md                  # Project documentation

## How to Run Simulations

Re-running simulations is optional since outputs are already generated, but in case you wish to do then follow the following steps:

[update your system]
sudo apt update && sudo apt upgrade -y
[Install required dependencies]
sudo apt install build-essential bison flex libblas-dev csh python3-dev pkg-config libpugixml-dev -y
[Download & Install 3D-ICE 4.0]
git clone https://github.com/esl-epfl/3d-ice.git
cd 3d-ice
[Compile SuperLU_MT (multi-threaded version — included in repo)]
./install-superlumt.sh
[Build 3D-ICE]
make

[Baseline simulations (paper replication)]
../bin/3D-ICE-Emulator mc4rm/transient/2dies_background.stk
../bin/3D-ICE-Emulator mc4rm/transient/2dies_four_elements.stk

[Custom 4-tier simulation]
../bin/3D-ICE-Emulator my_4tier.stk


## How to Generate Plots

cd ~/Desktop/ecse541/project/3d-ice/test
python3 plot_thermal.py

## How to access the plots

cd ~/test/figs/
