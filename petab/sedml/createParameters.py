# create the parameter file in the PEtab format

import pandas as pd
import os
import libsedml
import libsbml
import numpy as np
import sys


def parameterPETAB(new_sbml_save_path, sedml_file_name, measdatafile_save_path):

    # create new folder
    if not os.path.exists('./sedml2petab/' + sedml_file_name + '/parameters'):
        os.makedirs('./sedml2petab/' + sedml_file_name + '/parameters')

    # save path
    correct_petab_name = 'parameters_' + sedml_file_name + '.tsv'
    parameter_save_path = './sedml2petab/' + sedml_file_name + '/parameters/' + correct_petab_name

    # create new data frame
    ParFile = pd.DataFrame(columns=['parameterId', 'parameterName', 'parameterScale', 'lowerBound',
                                    'upperBound', 'nominalValue', 'estimate', 'priorType',
                                    'priorParameters', 'HierarchicalOptimization (optional)'], data=[])

    # open sbml model and measurement_data file to collect data about all parameters
    sbml_model = libsbml.readSBML(new_sbml_save_path)
    MesDataFile = pd.read_csv(measdatafile_save_path, sep='\t')
    par_list = []
    par_value = []
    lin_log_list = []
    for iPar in range(0, sbml_model.getModel().getNumParameters()):
        if sbml_model.getModel().getParameter(iPar).getMetaId() != '':
            par_list.append(sbml_model.getModel().getParameter(iPar).getId())
            if sbml_model.getModel().getParameter(iPar).getValue() > 0:
                par_value.append(np.log10(sbml_model.getModel().getParameter(iPar).getValue()))
                lin_log_list.append('log10')
            elif sbml_model.getModel().getParameter(iPar).getValue() <= 0:
                par_value.append(sbml_model.getModel().getParameter(iPar).getValue())
                lin_log_list.append('lin')

    # get sigma names from MesDataFile only once
    sigma_name = []
    for iElement in range(0, len(MesDataFile['observableId'])):
        if iElement == 0:
            sigma_name.append('sigma_' + MesDataFile['observableId'][0])
        else:
            if MesDataFile['observableId'][iElement] != MesDataFile['observableId'][iElement - 1]:
                sigma_name.append('sigma_' + MesDataFile['observableId'][iElement])

    # use new data to fill in the new data frame
    # unused columns can simply remain empty
    ParFile['parameterId'] = pd.concat([pd.Series(par_list), pd.Series(sigma_name)], ignore_index=True)
    ParFile['parameterName'] = ParFile['parameterId']
    ParFile['nominalValue'] = pd.concat([pd.Series(par_value), pd.Series([4] * len(sigma_name))], ignore_index=True)

    # possibly it has to be user defined
    ParFile['parameterScale'] = pd.concat([pd.Series(lin_log_list), pd.Series(['log10'] * len(sigma_name))], ignore_index=True)
    ParFile['lowerBound'] = pd.Series(['-8'] * len(ParFile['parameterId']))
    ParFile['upperBound'] = pd.Series(['8'] * len(ParFile['parameterId']))
    ParFile['estimate'] = pd.Series(['1'] * len(ParFile['parameterId']))

    # save data frame as .tsv
    ParFile.to_csv(parameter_save_path, sep='\t', index=False)

    return parameter_save_path