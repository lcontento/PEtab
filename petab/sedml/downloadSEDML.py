from .sedml_import import *
import os

def downloadAllSEDML(sedml_path, sedml_file_name):

    ########### create folder for all sedml and sbml files ##############
    if not os.path.exists('./sedml_files'):
        os.makedirs('./sedml_files')
    if not os.path.exists('./sedml_files/' + sedml_file_name):
        os.makedirs('./sedml_files/' + sedml_file_name)
    if not os.path.exists('./sedml_files/' + sedml_file_name + '/sbml_models'):
        os.makedirs('./sedml_files/' + sedml_file_name + '/sbml_models')

    sedml_save_path = './sedml_files'
    sbml_save_path = './sedml_files/' + sedml_file_name + '/sbml_models'

    if not os.path.isfile(sedml_path):
        ############## download sedml + open sedml + download sbml + open sbml ################
        try:
            download_sedml_model(sedml_path, sedml_save_path)
        except:
            raise ValueError('The sedml path is not a file nor a valid URL!')

    else:
        ############## copy sedml + download sbml + open sbml #################
        shutil.copyfile(sedml_path, sedml_save_path + '/' + sedml_file_name)
        sedml_save_path = sedml_save_path + '/' + sedml_file_name
        sedml_file = libsedml.readSedML(sedml_save_path)


    return sedml_save_path, sbml_save_path
