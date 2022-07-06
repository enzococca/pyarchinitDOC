# -*- coding: utf-8 -*-

from pyarchinitDockWidget import PyarchinitPluginDialog
from tabs.Archeozoology import pyarchinit_Archeozoology
from tabs.Campioni import pyarchinit_Campioni
from tabs.Deteta import pyarchinit_Deteta
from tabs.Detsesso import pyarchinit_Detsesso
from tabs.Documentazione import pyarchinit_Documentazione
from tabs.Gis_Time_controller import pyarchinit_Gis_Time_Controller
from tabs.Image_viewer import Main
from tabs.Images_comparison import Comparision
from tabs.Images_directory_export import pyarchinit_Images_directory_export
from tabs.Inv_Materiali import pyarchinit_Inventario_reperti
from tabs.Pdf_export import pyarchinit_pdf_export
from tabs.Excel_export import pyarchinit_excel_export
from tabs.Periodizzazione import pyarchinit_Periodizzazione
from tabs.Schedaind import pyarchinit_Schedaind
from tabs.Site import pyarchinit_Site
from tabs.Struttura import pyarchinit_Struttura
from tabs.Tomba import pyarchinit_Tomba
from tabs.Thesaurus import pyarchinit_Thesaurus
from tabs.US_USM import pyarchinit_US
from tabs.UT import pyarchinit_UT
from tabs.PRINTMAP import pyarchinit_PRINTMAP
from tabs.gpkg_export import pyarchinit_GPKG
from tabs.tops_pyarchinit import pyarchinit_TOPS
from gui.pyarchinitConfigDialog import pyArchInitDialog_Config
from gui.dbmanagment import pyarchinit_dbmanagment
from gui.pyarchinitInfoDialog import pyArchInitDialog_Info

from modules.utility.pyarchinit_OS_utility import Pyarchinit_OS_Utility
from modules.utility.pyarchinit_folder_installation import pyarchinit_Folder_installation





def classFactory(iface):


    from .pyarchinitPlugin import PyArchInitPlugin
    return PyArchInitPlugin(iface)
