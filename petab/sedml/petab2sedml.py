import libsedml
import libsbml
import pandas
import os
from .recreateExperimental import *

def petab2sedml(petab_folder_path):                                                                                     #exp_save_path, meas_save_path, par_save_path, sbml_save_path):

    # create the basic experimental data file
    new_exp_save_path, new_meas_save_path, new_par_save_path, new_sbml_save_path = recreateExpDataFile(petab_folder_path)                                                                              #exp_save_path, meas_save_path, par_save_path, sbml_save_path)