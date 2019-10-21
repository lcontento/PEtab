from .sedml_import import *
import libsedml
import libsbml
import shutil
from .downloadSBML import *
from .downloadSEDML import *
from .getObservables import *
from .getExperimentalData import *
from .rearrangeExperimentalData import *


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

    # download sedml file
    sedml_save_path, sbml_save_path = downloadAllSEDML(sedml_path, sedml_file_name)

    # download sbml files
    downloadAllSBML(sedml_save_path, sbml_save_path)

    # download experimental data
    getAllExperimentalDataFiles(sedml_path, sedml_file_name)

    # rearrange experimental data file into petab format
    rearrange2PEtab(sedml_path, sedml_file_name)

    # add observables to sbml file
    new_sbml_path = getAllObservables(sedml_save_path, sbml_save_path)


    


    # create petab folder
