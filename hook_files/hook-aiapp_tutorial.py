""" https://pyinstaller.org/en/stable/hooks.html#PyInstaller.utils.hooks.copy_metadata """
from PyInstaller.utils.hooks import copy_metadata

datas = copy_metadata('aiapp_tutorial') # to solve packaing version missing problem
