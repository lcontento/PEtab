from .sedml_import import *
import libsedml
import libsbml
import shutil
from .downloadSBML import *
from .downloadSEDML import *



def sedml2petab(sedml_path, sedml_file_name, output_folder=None):
    """
    [description]

    Parameters
    ----------

    [...]

    Returns
    -------

    [...]
    """

    ######## download sedml file #########
    sedml_save_path, sbml_save_path = downloadSEDML(sedml_path, sedml_file_name)

    ######## download sbml files #########
    downloadSBML(sedml_save_path, sbml_save_path)

    sbml_file = libsbml.readSBML(sbml_save_path)

    ####### add observables to sbml file #######
    a = 4

    ####### create petab folder #########
