# python-simulation
Creating a forest fire model in Python, investigating the properties of the simulation and carrying out relevant analyses.
------------

In this repository you will find all the files needed to explore the forest fire simulation model.

# List of files

- simulation_script.py : The python code written to run the simulation 
- animation.ipynb : The python code to animate and visualise the forest fire model
- plots.ipynb : The python code to extract, analyse and visualise data from the forest fire model

- [tests](/tests) : folder containing tests of the simulation code for rules 1, 2 and 4 (3 and 4 work by the same function)

- [figures](/figures) : folder of images (time series plots) used in the report 

- [additional_feature](/additional_feature) : folder containing all code to investigate the additional feature
  - add_simulation_script.py : The python code written to run the simulation with the additional model feature
  - add_plots.ipynb : The python code to visualise data from the additional feature forest fire model
  - add_animation.ipynb: The python code to animate and visualise the additional feature forest fire model

# Getting started

1. Install Anaconda Python from here: https://www.anaconda.com/products/distribution#Downloads
2. Open Anaconda and launch JupyterLab
3. In JupyterLab create a new folder by right clicking the files tab --> new folder --> name it "forest" and click to enter
4. In JupyterLab open a terminal window and type `cd forest` to change directory
   - open the folder location by entering `explorer.exe .`
   - copy and paste the contents of this archive into the folder
5. You can now open any .py (python script) or .ipynb (notebook) file in JupyterLab
   - In the scripts you can modify the values of: the seed, initial_state, f, p, r, fraction of trees and num_steps
6. Run the script in the terminal window by typing `python simulation_script.py`
7. With animation.ipynb open you can run the code to visualise the animation, or the plots with plot.ipynb
8. To look at plots or animation for the addtional model feature:
   - in terminal window enter `cd additional_feature` to change to this folder
   - run the script with `python add_simulation_script.py`
   - visualise plots by opening and running code in add_plots.ipynb and animations in add_animation.ipynb
9 (optional). Run tests of the code by entering "cd tests" into the terminal and then entering `pytest"

-------------------------------------------------
*Originally compiled 07/02/23*
