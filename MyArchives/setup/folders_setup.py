from os.path import exists
from os import makedirs

from setup.tasks import home_directory

homepath = home_directory()


def folder_setup():
    # Creates MyArchives folder in user directory
    # Creates MyArchive folder (to store entry files)
    if not exists(f"{homepath}MyArchive"):
        makedirs(f"{homepath}MyArchive")
    # Create Textfiles folder (to store software config files)
    if not exists(f"{homepath}Textfiles"):
        makedirs(f"{homepath}Textfiles")
