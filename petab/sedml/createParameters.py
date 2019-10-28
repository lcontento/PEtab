# create the parameter file in the PEtab format

import pandas as pd
import os
import libsbml


def parameterPETAB(sbml_save_path, sedml_file_name, measdatafile_save_path):

    # create new folder
    if not os.path.exists('./sedml_files/' + sedml_file_name + '/parameters'):
        os.makedirs('./sedml_files/' + sedml_file_name + '/parameters')

    # save path
    correct_petab_name = 'parameters_' + sedml_file_name + '.tsv'
    parameter_save_path = './sedml_files/' + sedml_file_name + '/parameters/' + correct_petab_name

    # create new data frame
    ParFile = pd.DataFrame(columns=['parameterId', 'parameterName', 'parameterScale', 'lowerBound',
                                    'upperBound', 'nominalValue', 'estimate', 'priorType',
                                    'priorParameters', 'HierarchicalOptimization (optional)'], data=[])

    # open sbml model and measurement_data file to collect data about all parameters
    sbml_model = libsbml.readSBML(sbml_save_path)
    MesDataFile = pd.read_csv(measdatafile_save_path, sep='\t')
    par_list = []
    par_value = []
    for iPar in range(0, sbml_model.getModel().getNumParameters()):
        if sbml_model.getModel().getParameter(iPar).getMetaId() != '':
            par_list.append(sbml_model.getModel().getParameter(iPar).getId())
            par_value.append(sbml_model.getModel().getParameter(iPar).getValue())

    # use new data to fill in the new data frame
    # unused columns can simply remain empty
    ParFile['parameterId'] = pd.concat([pd.Series(par_list), MesDataFile['noiseParameters']], ignore_index=True)                            # each sigma only one time!
    ParFile['parameterName'] = ParFile['parameterId']
    ParFile['nominalValue'] = pd.concat([pd.Series(par_value), pd.Series([4] * len(MesDataFile['noiseParameters']))], ignore_index=True)

    # possible it has to be user defined
    ParFile['parameterScale'] = pd.Series(['log10'] * len(ParFile['parameterId']))
    ParFile['lowerBound'] = pd.Series(['-5'] * len(ParFile['parameterId']))
    ParFile['upperBound'] = pd.Series(['5'] * len(ParFile['parameterId']))
    ParFile['estimate'] = pd.Series(['1'] * len(ParFile['parameterId']))

    # save data frame as .tsv
    ParFile.to_csv(parameter_save_path, sep='\t', index=False)

    return parameter_save_path