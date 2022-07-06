# -*- coding: utf-8 -*-



from modules.utility.pyarchinit_OS_utility import Pyarchinit_OS_Utility
from modules.utility.pyarchinit_folder_installation import pyarchinit_Folder_installation
from modules.utility.settings import Settings





def classFactory(iface):


    from .pyarchinitPlugin import PyArchInitPlugin
    return PyArchInitPlugin(iface)
