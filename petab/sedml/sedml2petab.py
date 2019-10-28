from .sedml_import import *
import libsedml
import libsbml
import shutil
from .downloadSBML import *
from .downloadSEDML import *
from .getObservables import *
from .getExperimentalData import *
from .rearrangeExperimentalData import *
from .createExperimental import *
from .createMeasurement import *
from .createParameters import *


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
    sbml_save_path, sbml_id = downloadAllSBML(sedml_save_path, sbml_save_path)

    # download experimental data
    getAllExperimentalDataFiles(sedml_path, sedml_file_name)

    # rearrange experimental data file into petab format
    exp_rearrange_save_path = rearrange2PEtab(sedml_path, sedml_file_name)

    # create experimental_condition file
    expconfile_save_path = experimentalPETAB(sedml_save_path, sedml_file_name)

    # create measurement_date file
    measdatafile_save_path = measurementPETAB(exp_rearrange_save_path, sedml_file_name)

    # create parameters file
    parfile_save_path = parameterPETAB(sbml_save_path, sedml_file_name, measdatafile_save_path)                         # new_sbml_save_path!

    # add observables to sbml file
    new_sbml_save_path = getAllObservables(sedml_save_path, sbml_save_path, sedml_file_name, sbml_id)

    ####

    ####

    ####

    # extend the sbml_file_with_observables by 'noise_', 'sigma_', 'observable_' as [parameters] and [assignment_rules]

    # create petab folder with all ingredients
    a = 4