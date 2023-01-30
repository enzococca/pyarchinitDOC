#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
/***************************************************************************
        pyArchInit Plugin  - A QGIS plugin to manage archaeological dataset
                             -------------------
        begin                : 2007-12-01
        copyright            : (C) 2008 by Luca Mandolesi; Enzo Cocca <enzo.ccc@gmail.com>
        email                : mandoluca at gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from sqlalchemy.event import listen
import psycopg2
from builtins import object
from builtins import range
from builtins import str
from builtins import zip
from sqlalchemy import and_, or_
from geoalchemy2 import *
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import MetaData
from qgis.core import *
from qgis.PyQt.QtWidgets import QMessageBox


class Pyarchinit_db_management(object):
    '''This function creates a database manager which creates the database and then creates the database object .

    :param object: [description]
    :type object: [type]
    :return: [description]
    :rtype: [type]
    '''    
    metadata = ''
    engine = ''
    boolean = ''
    
    if os.name == 'posix':
        boolean = 'True'
    elif os.name == 'nt':
        boolean = 'True'

    def __init__(self, c):
        self.conn_str = c
        
    
    def load_spatialite(self,dbapi_conn, connection_record):
        '''Loads the spatialite database extension .

        :param dbapi_conn: [description]
        :type dbapi_conn: [type]
        :param connection_record: [description]
        :type connection_record: [type]
        '''        
        dbapi_conn.enable_load_extension(True)
        
        if Pyarchinit_OS_Utility.isWindows()== True:
            dbapi_conn.load_extension('mod_spatialite.dll')
        
        elif Pyarchinit_OS_Utility.isMac()== True:
            dbapi_conn.load_extension('mod_spatialite.so')
        else:
            dbapi_conn.load_extension('mod_spatialite.so')  
    def connection(self):
        '''Connect to the database .

        :return: [description]
        :rtype: [type]
        '''        
        test = True
        try:
            test_conn = self.conn_str.find("sqlite")
            if test_conn == 0:
                self.engine = create_engine(self.conn_str, echo=eval(self.boolean))
                listen(self.engine, 'connect', self.load_spatialite)
            else:
                self.engine = create_engine(self.conn_str, max_overflow=-1, echo=eval(self.boolean))
            
                
            self.metadata = MetaData(self.engine)
            conn = self.engine.connect()
            
        except Exception as e:
            QMessageBox.warning(None, "Message", "Error: "+str(e), QMessageBox.Ok)
            test = False
        finally:
            conn.close()

        try:
            db_upd = DB_update(self.conn_str)
            db_upd.update_table()
        except Exception as e:
            QMessageBox.warning(None, "Message", "Error: "+str(e), QMessageBox.Ok)
            test = False
        return test

        # insert statement

    def insert_pottery_values(self, *arg):
        '''Inserts the values of the Pottery values into the pottery dictionary .

        :return: [description]
        :rtype: [type]
        '''        
        pottery = POTTERY(arg[0],
                  arg[1],
                  arg[2],
                  arg[3],
                  arg[4],
                  arg[5],
                  arg[6],
                  arg[7],
                  arg[8],
                  arg[9],
                  arg[10],
                  arg[11],
                  arg[12],
                  arg[13],
                  arg[14],
                  arg[15],
                  arg[16],
                  arg[17],
                  arg[18],
                  arg[19],
                  arg[20],
                  arg[21],
                  arg[22],
                  arg[23],
                  arg[24],
                  arg[25],
                  arg[26],
                  arg[27],
                  arg[28],
                  arg[29],
                  arg[30],
                  arg[31])

        return pottery
    def insert_pyus(self, *arg):
        '''Insert a PyUS into the PyUS object .

        :return: [description]
        :rtype: [type]
        '''        
        pyus = PYUS(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6],
                arg[7],
                arg[8],
                arg[9],
                arg[10],
                arg[11],
                arg[12],
                arg[13])
        return pyus
    def insert_pyusm(self, *arg):
        '''
        insert_pyusm insert a pyusmtsm argument into the pyusm module

        :return: [description]
        :rtype: [type]
        '''        
        pyusm = PYUSM(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6],
                arg[7],
                arg[8],
                arg[9],
                arg[10],
                arg[11],
                arg[12],
                arg[13])
        return pyusm
    def insert_pysito_point(self, *arg):
        '''
        insert_pysito_point Inserts a Pysito point into the stack .

        :return: [description]
        :rtype: [type]
        '''        
        pysito_point = PYSITO_POINT(arg[0],
                arg[1],
                arg[2])
        return pysito_point
    
    
    def insert_pysito_polygon(self, *arg):
        '''
        insert_pysito_polygon Insert a polygon into the current board .

        :return: [description]
        :rtype: [type]
        '''        
        pysito_polygon = PYSITO_POLYGON(arg[0],
                arg[1],
                arg[2])
        return pysito_polygon
        
    def insert_pyquote(self, *arg):
        '''
        insert_pyquote Insert a PyYQUOTE into the stack .

        :return: [description]
        :rtype: [type]
        '''        
        pyquote = PYQUOTE(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6],
                arg[7],
                arg[8],
                arg[9],
                arg[10])
        return pyquote    
    def insert_pyquote_usm(self, *arg):
        '''
        insert_pyquote_usm Insert a pyquote_usm into the stack .

        :return: [description]
        :rtype: [type]
        '''        
        pyquote_usm = PYQUOTEUSM(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6],
                arg[7],
                arg[8],
                arg[9],
                arg[10])
        return pyquote_usm    
    def insert_pyus_negative(self, *arg):
        '''
        insert_pyus_negative Insert a PyUS_NEGATIVE into the PYUS_NEGATIVE argument .

        :return: [description]
        :rtype: [type]
        '''        
        pyus_negative = PYUS_NEGATIVE(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6])
        return pyus_negative
    
    def insert_pystrutture(self, *arg):
        '''
        insert_pystrutture Insert a pystrututure into the parser .

        :return: [description]
        :rtype: [type]
        '''        
        pystrutture = PYSTRUTTURE(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6],
                arg[7],
                arg[8],
                arg[9],
                arg[10],
                arg[11])
        return pystrutture
    
    def insert_pyreperti(self, *arg):
        '''
        insert_pyreperti Inserts a pyreperti argument into the list of pyreperti arguments .

        :return: [description]
        :rtype: [type]
        '''        
        pyreperti = PYREPERTI(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4])
        return pyreperti
    
    def insert_pyindividui(self, *arg):
        '''
        insert_pyindividui Inserts a Pyindividui into the list of pyindividis arguments

        :return: [description]
        :rtype: [type]
        '''        
        pyindividui = PYINDIVIDUI(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5])
        return pyindividui
    
    def insert_pycampioni(self, *arg):
        '''
        insert_pycampioni Insert a pycampionioni argument into the PYCUAMPIONI .

        :return: [description]
        :rtype: [type]
        '''        
        pycampioni = PYCAMPIONI(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6],
                arg[7],
                arg[8])
        return pycampioni
    
    def insert_pytomba(self, *arg):
        '''
        insert_pytomba Insert a Python TYTomba into a PYTomba object .

        :return: [description]
        :rtype: [type]
        '''        
        pytomba = PYTOMBA(arg[0],
                arg[1],
                arg[2],
                arg[3])
        return pytomba
    
    def insert_pydocumentazione(self, *arg):
        '''
        insert_pydocumentazione Inserts a pydocumentazioneer into the first argument .

        :return: [description]
        :rtype: [type]
        '''        
        pydocumentazione = PYDOCUMENTAZIONE(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6])
        return pydocumentazione
    
    def insert_pylineeriferimento(self, *arg):
        '''
        insert_pylineeriferimento Insert a pylineeriferimentoimentoimentoimento text into the docstring

        :return: [description]
        :rtype: [type]
        '''       
        pylineeriferimento = PYLINEERIFERIMENTO(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4])
        return pylineeriferimento
    
    def insert_pyripartizioni_spaziali(self, *arg):
        '''
        insert_pyripartizioni_spaziali Inserts a pyripartizioni_spazizioni_spazizioni into the pyripartizizioni_spazizioni_spazizioni

        :return: [description]
        :rtype: [type]
        '''
        pyripartizioni_spaziali = PYRIPARTIZIONI_SPAZIALI(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5])
        return pyripartizioni_spaziali
    
    def insert_pysezioni(self, *arg):
        '''
        insert_pysezioni Insert a PysezionI into the parser

        :return: [description]
        :rtype: [type]
        '''
        pysezioni = PYSEZIONI(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6],
                arg[7])
        return pysezioni
    
    
    
    def insert_values(self, *arg):
        '''
        insert_values Insert values into the US and US tags .

        :return: [description]
        :rtype: [type]
        '''        
        us = US(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6],
                arg[7],
                arg[8],
                arg[9],
                arg[10],
                arg[11],
                arg[12],
                arg[13],
                arg[14],
                arg[15],
                arg[16],
                arg[17],
                arg[18],
                arg[19],
                arg[20],
                arg[21],
                arg[22],
                arg[23],
                arg[24],
                arg[25],
                arg[26],
                arg[27],
                arg[28],
                arg[29],
                arg[30],
                arg[31],
                arg[32],
                arg[33],
                arg[34],
                arg[35],
                arg[36],
                arg[37],
                arg[38],
                arg[39],
                arg[40],
                arg[41],
                arg[42],
                arg[43],
                arg[44],
                arg[45],
                arg[46],
                arg[47],
                arg[48],
                arg[49],
                arg[50],
                arg[51],    
                arg[52],
                arg[53],
                arg[54],
                arg[55],
                arg[56],
                arg[57],
                arg[58],
                arg[59],
                arg[60],
                arg[61],
                arg[62],
                arg[63],
                arg[64],
                arg[65],
                arg[66],
                arg[67],
                arg[68],
                arg[69],
                arg[70],
                arg[71],
                arg[72],
                arg[73],
                arg[74],
                arg[75],
                arg[76],
                arg[77],
                arg[78],
                arg[79],
                arg[80],
                arg[81],
                arg[82],
                arg[83],
                arg[84],
                arg[85],
                arg[86],
                arg[87],
                arg[88],
                arg[89],
                arg[90],
                arg[91],
                arg[92],
                arg[93],
                arg[94],
                arg[95],
                arg[96],
                arg[97],
                arg[98],
                arg[99],
                arg[100],
                arg[101],
                arg[102],
                arg[103],
                arg[104],
                arg[105],
                arg[106],
                arg[107],
                arg[108],
                arg[109],
                arg[110],
                arg[111],
                arg[112],
                arg[113],
                arg[114],
                arg[115],
                arg[116],
                )

        return us

    def insert_ut_values(self, *arg):
        '''
        insert_ut_values Inserts values into the UT values .

        :return: [description]
        :rtype: [type]
        '''

        ut = UT(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6],
                arg[7],
                arg[8],
                arg[9],
                arg[10],
                arg[11],
                arg[12],
                arg[13],
                arg[14],
                arg[15],
                arg[16],
                arg[17],
                arg[18],
                arg[19],
                arg[20],
                arg[21],
                arg[22],
                arg[23],
                arg[24],
                arg[25],
                arg[26],
                arg[27],
                arg[28],
                arg[29],
                arg[30],
                arg[31],
                arg[32],
                arg[33],
                arg[34],
                arg[35],
                arg[36],
                arg[37],
                arg[38],
                arg[39],
                arg[40],
                arg[41])

        return ut

    def insert_site_values(self, *arg):
        '''
        insert_site_values Inserts a site values into the datapoint

        :return: [description]
        :rtype: [type]
        '''
        sito = SITE(arg[0],
                    arg[1],
                    arg[2],
                    arg[3],
                    arg[4],
                    arg[5],
                    arg[6],
                    arg[7],
                    arg[8],
                    arg[9])

        return sito

    def insert_periodizzazione_values(self, *arg):
        '''
        insert_periodizzazione_values Inserts periodizziza into the list of values .

        :return: [description]
        :rtype: [type]
        '''
        periodizzazione = PERIODIZZAZIONE(arg[0],
                                          arg[1],
                                          arg[2],
                                          arg[3],
                                          arg[4],
                                          arg[5],
                                          arg[6],
                                          arg[7],
                                          arg[8])

        return periodizzazione

    def insert_values_reperti(self, *arg):
        '''
        insert_values_reperti Inserts values in the inventory into the inventory

        :return: [description]
        :rtype: [type]
        '''
        inventario_materiali = INVENTARIO_MATERIALI(arg[0],
                                                    arg[1],
                                                    arg[2],
                                                    arg[3],
                                                    arg[4],
                                                    arg[5],
                                                    arg[6],
                                                    arg[7],
                                                    arg[8],
                                                    arg[9],
                                                    arg[10],
                                                    arg[11],
                                                    arg[12],
                                                    arg[13],
                                                    arg[14],
                                                    arg[15],
                                                    arg[16],
                                                    arg[17],
                                                    arg[18],
                                                    arg[19],
                                                    arg[20],
                                                    arg[21],
                                                    arg[22],
                                                    arg[23],
                                                    arg[24],
                                                    arg[25],
                                                    arg[26],
                                                    arg[27],
                                                    arg[28],
                                                    arg[29],
                                                    arg[30],
                                                    arg[31])

        return inventario_materiali

    def insert_struttura_values(self, *arg):
        '''
        insert_struttura_values Inserts STRUTTUTTRA values into the parser .

        :return: [description]
        :rtype: [type]
        '''
        struttura = STRUTTURA(arg[0],
                              arg[1],
                              arg[2],
                              arg[3],
                              arg[4],
                              arg[5],
                              arg[6],
                              arg[7],
                              arg[8],
                              arg[9],
                              arg[10],
                              arg[11],
                              arg[12],
                              arg[13],
                              arg[14],
                              arg[15],
                              arg[16],
                              arg[17])

        return struttura

    def insert_values_ind(self, *arg):
        '''
        insert_values_ind insert values into scheduler

        :return: [description]
        :rtype: [type]
        '''
        schedaind = SCHEDAIND(arg[0],
                              arg[1],
                              arg[2],
                              arg[3],
                              arg[4],
                              arg[5],
                              arg[6],
                              arg[7],
                              arg[8],
                              arg[9],
                              arg[10],
                              arg[11],
                              arg[12],
                              arg[13],
                              arg[14],
                              arg[15],
                              arg[16],
                              arg[17],
                              arg[18],
                              arg[19],
                              arg[20],
                              arg[21],
                              arg[22],
                              arg[23])

        return schedaind

    def insert_values_detsesso(self, *arg):
        '''
        insert_values_detsesso Inserts values into the matrix

        :return: [description]
        :rtype: [type]
        '''
        detsesso = DETSESSO(arg[0],
                            arg[1],
                            arg[2],
                            arg[3],
                            arg[4],
                            arg[5],
                            arg[6],
                            arg[7],
                            arg[8],
                            arg[9],
                            arg[10],
                            arg[11],
                            arg[12],
                            arg[13],
                            arg[14],
                            arg[15],
                            arg[16],
                            arg[17],
                            arg[18],
                            arg[19],
                            arg[20],
                            arg[21],
                            arg[22],
                            arg[23],
                            arg[24],
                            arg[25],
                            arg[26],
                            arg[27],
                            arg[28],
                            arg[29],
                            arg[30],
                            arg[31],
                            arg[32],
                            arg[33],
                            arg[34],
                            arg[35],
                            arg[36],
                            arg[37],
                            arg[38],
                            arg[39],
                            arg[40],
                            arg[41],
                            arg[42],
                            arg[43],
                            arg[44],
                            arg[45],
                            arg[46],
                            arg[47],
                            arg[48],
                            arg[49],
                            arg[50],
                            arg[51],
                            arg[52],
                            arg[53])

        return detsesso

    def insert_values_deteta(self, *arg):
        '''
        insert_values_deteta Compute the deteta of the given arguments .

        :return: [description]
        :rtype: [type]
        '''
        deteta = DETETA(arg[0],
                        arg[1],
                        arg[2],
                        arg[3],
                        arg[4],
                        arg[5],
                        arg[6],
                        arg[7],
                        arg[8],
                        arg[9],
                        arg[10],
                        arg[11],
                        arg[12],
                        arg[13],
                        arg[14],
                        arg[15],
                        arg[16],
                        arg[17],
                        arg[18],
                        arg[19],
                        arg[20],
                        arg[21],
                        arg[22],
                        arg[23],
                        arg[24],
                        arg[25],
                        arg[26],
                        arg[27],
                        arg[28],
                        arg[29],
                        arg[30],
                        arg[31],
                        arg[32],
                        arg[33],
                        arg[34],
                        arg[35],
                        arg[36],
                        arg[37],
                        arg[38],
                        arg[39],
                        arg[40],
                        arg[41],
                        arg[42],
                        arg[43],
                        arg[44],
                        arg[45],
                        arg[46],
                        arg[47],
                        arg[48],
                        arg[49],
                        arg[50],
                        arg[51],
                        arg[52],
                        arg[53],
                        arg[54],
                        arg[55],
                        arg[56])

        return deteta

    def insert_media_values(self, *arg):
        '''
        insert_media_values Insert media values into the media object

        :return: [description]
        :rtype: [type]
        '''
        media = MEDIA(arg[0],
                      arg[1],
                      arg[2],
                      arg[3],
                      arg[4],
                      arg[5],
                      arg[6])

        return media

    def insert_mediathumb_values(self, *arg):
        '''
        insert_mediathumb_values Inserts values into the media_thumbnail argument .

        :return: [description]
        :rtype: [type]
        '''
        media_thumb = MEDIA_THUMB(arg[0],
                                  arg[1],
                                  arg[2],
                                  arg[3],
                                  arg[4],
                                  arg[5],
                                  arg[6],
                                  arg[7])

        return media_thumb

    def insert_media2entity_values(self, *arg):
        """Istanzia la classe MEDIATOENTITY da pyarchinit_db_mapper"""
        mediatoentity = MEDIATOENTITY(arg[0],
                                      arg[1],
                                      arg[2],
                                      arg[3],
                                      arg[4],
                                      arg[5],
                                      arg[6])

        return mediatoentity

    
    def insert_media2entity_view_values(self, *arg):
        '''
        insert_media2entity_view_values Inserts values into Media2entity_view

        :return: [description]
        :rtype: [type]
        '''
        mediaentity_view= MEDIAVIEW(arg[0],
                arg[1],
                arg[2],
                arg[3],
                arg[4],
                arg[5],
                arg[6])

        return mediaentity_view 
    
    def insert_values_tomba(self, *arg):
        '''
        insert_values_tomba Inserts values into TOMBA

        :return: [description]
        :rtype: [type]
        '''

        tomba = TOMBA(arg[0],
                              arg[1],
                              arg[2],
                              arg[3],
                              arg[4],
                              arg[5],
                              arg[6],
                              arg[7],
                              arg[8],
                              arg[9],
                              arg[10],
                              arg[11],
                              arg[12],
                              arg[13],
                              arg[14],
                              arg[15],
                              arg[16],
                              arg[17],
                              arg[18],
                              arg[19],
                              arg[20],
                              arg[21],
                              arg[22],
                              arg[23],
                              arg[24],
                              arg[25],)

        return tomba

    def insert_values_campioni(self, *arg):
        '''
        insert_values_campioni Inserts the given value into the campioni .

        :return: [description]
        :rtype: [type]
        '''

        campioni = CAMPIONI(arg[0],
                            arg[1],
                            arg[2],
                            arg[3],
                            arg[4],
                            arg[5],
                            arg[6],
                            arg[7],
                            arg[8],
                            arg[9])

        return campioni

    def insert_values_thesaurus(self, *arg):
        '''
        insert_values_thesaurus Inserts the given values into the saurus

        :return: [description]
        :rtype: [type]
        '''

        thesaurus = PYARCHINIT_THESAURUS_SIGLE(arg[0],
                                               arg[1],
                                               arg[2],
                                               arg[3],
                                               arg[4],
                                               arg[5],
                                               arg[6])

        return thesaurus

    def insert_values_archeozoology(self, *arg):
        '''
        insert_values_archeozoology Inserts values in the archez hierarchy into the given array

        :return: [description]
        :rtype: [type]
        '''

        archeozoology = ARCHEOZOOLOGY(arg[0],
                                        arg[1],
                                        arg[2],
                                        arg[3],
                                        arg[4],
                                        arg[5],
                                        arg[6],
                                        arg[7],
                                        arg[8],
                                        arg[9],
                                        arg[10],
                                        arg[11],
                                        arg[12],
                                        arg[13],
                                        arg[14],
                                        arg[15],
                                        arg[16],
                                        arg[17],
                                        arg[18],
                                        arg[19],
                                        arg[20],
                                        arg[21],
                                        arg[22],
                                        arg[23],
                                        arg[24],
                                        arg[25],
                                        arg[26],
                                        arg[27],
                                        arg[28],
                                        arg[29],
                                        arg[30])

        return archeozoology

    def insert_values_Lapidei(self, *arg):
        '''
        insert_values_Lapidei Inserts values into the LAPIDI_LAPPLICATION_LAPID .

        :return: [description]
        :rtype: [type]
        '''

        inventario_lapidei = INVENTARIO_LAPIDEI(arg[0],
                                                arg[1],
                                                arg[2],
                                                arg[3],
                                                arg[4],
                                                arg[5],
                                                arg[6],
                                                arg[7],
                                                arg[8],
                                                arg[9],
                                                arg[10],
                                                arg[11],
                                                arg[12],
                                                arg[13],
                                                arg[14],
                                                arg[15],
                                                arg[16],
                                                arg[17],
                                                arg[18],
                                                arg[19])

        return inventario_lapidei

    def insert_values_documentazione(self, *arg):
        '''
        insert_values_documentazione Inserts a value into the document

        :return: [description]
        :rtype: [type]
        '''

        documentazione = DOCUMENTAZIONE(arg[0],
                                        arg[1],
                                        arg[2],
                                        arg[3],
                                        arg[4],
                                        arg[5],
                                        arg[6],
                                        arg[7],
                                        arg[8])

        return documentazione

    def insert_pdf_administrator_values(self, *arg):
        '''
        insert_pdf_administrator_values Insert values into PDFAdmin object .

        :return: [description]
        :rtype: [type]
        '''
        pdf_administrator = PDF_ADMINISTRATOR(arg[0],
                                              arg[1],
                                              arg[2],
                                              arg[3],
                                              arg[4])

        return pdf_administrator

    def insert_campioni_values(self, *arg):
        '''
        insert_campioni_values Inserts the values of the given campioni values into the given list .

        :return: [description]
        :rtype: [type]
        '''
        campioni = CAMPIONI(arg[0],
                            arg[1],
                            arg[2],
                            arg[3],
                            arg[4],
                            arg[5],
                            arg[6],
                            arg[7],
                            arg[8],
                            arg[9])

        return campioni

    ##  def insert_relationship_check_values(self, *arg):
    ##      """Istanzia la classe RELATIONSHIP_CHECK da pyarchinit_db_mapper"""
    ##      relationship_check = RELATIONSHIP_CHECK(arg[0],
    ##                                              arg[1],
    ##                                              arg[2],
    ##                                              arg[3],
    ##                                              arg[4],
    ##                                              arg[5],
    ##                                              arg[6],
    ##                                              arg[7],
    ##                                              arg[8],
    ##                                              arg[9])
    ##
    ##      return relationship_check


    def execute_sql_create_db(self):
        '''
        execute_sql_create_db Execute the SQL create db
        '''
        path = os.path.dirname(__file__)
        rel_path = os.path.join(os.sep, 'query_sql', 'pyarchinit_create_db.sql')
        qyery_sql_path = '{}{}'.format(path, rel_path)
        create = open(qyery_sql_path, "r")
        stringa = create.read()
        create.close()
        self.engine.raw_connection().set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self.engine.text(stringa).execute()

    def execute_sql_create_spatialite_db(self):
        '''
        execute_sql_create_spatialite_db Execute SQL for the SQLite database
        '''
        path = os.path.dirname(__file__)
        rel_path = os.path.join(os.sep, 'query_sql', 'pyarchinit_create_spatialite_db.sql')
        qyery_sql_path = '{}{}'.format(path, rel_path)
        create = open(qyery_sql_path, "r")
        stringa = create.read()
        create.close()

        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        session.begin()
        session.execute(stringa)
        session.commit()
        session.close()

    def execute_sql_create_layers(self):
        '''
        execute_sql_create_layers Execute SQL create layer for the SQL
        '''
        path = os.path.dirname(__file__)
        rel_path = os.path.join(os.sep, 'query_sql', 'pyarchinit_layers_postgis.sql')
        qyery_sql_path = '{}{}'.format(path, rel_path)
        create = open(qyery_sql_path, "r")
        stringa = create.read()
        create.close()

        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        session.begin()
        session.execute(stringa)
        session.commit()
        session.close()

        # query statement

    def query(self, n):
        """
        Query the database for n rows of the class.
        @param n - the number of rows to query for.
        @return the rows of the class.
        """
        
        class_name = eval(n)
        # engine = self.connection()
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        query = session.query(class_name)
        res = query.all()
        session.close()
        return res

    def query_bool(self, params, table):
        """
        Given a dictionary of parameters and a table, return the result of the query.
        @param params - the dictionary of parameters           
        @param table - the table to query           
        @return the result of the query           
        """
        u = Utility()
        params = u.remove_empty_items_fr_dict(params)

        list_keys_values = list(params.items())

        field_value_string = ""

        for sing_couple_n in range(len(list_keys_values)):
            if sing_couple_n == 0:
                if type(list_keys_values[sing_couple_n][1]) != "<type 'str'>":
                    field_value_string = table + ".%s == %s" % (
                    list_keys_values[sing_couple_n][0], list_keys_values[sing_couple_n][1])
                else:
                    field_value_string = table + ".%s == u%s" % (
                    list_keys_values[sing_couple_n][0], list_keys_values[sing_couple_n][1])
            else:
                if type(list_keys_values[sing_couple_n][1]) == "<type 'str'>":
                    field_value_string = field_value_string + "," + table + ".%s == %s" % (
                    list_keys_values[sing_couple_n][0], list_keys_values[sing_couple_n][1])
                else:
                    field_value_string = field_value_string + "," + table + ".%s == %s" % (
                    list_keys_values[sing_couple_n][0], list_keys_values[sing_couple_n][1])

                    #field_value_string = ", ".join([table + ".%s == u%s" % (k, v) for k, v in params.items()])

        """
        Per poter utilizzare l'operatore LIKE è necessario fare una iterazione attraverso il dizionario per discriminare tra
        stringhe e numeri
        #field_value_string = ", ".join([table + ".%s.like(%s)" % (k, v) for k, v in params.items()])
        """
        # self.connection()
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        query_str = "session.query(" + table + ").filter(and_(" + field_value_string + ")).all()"
        res = eval(query_str)

        session.close()
        return res
    
    
    
    def query_bool_special(self, params, table):
        """
        Given a dictionary of parameters and a table, return the result of the query.
        @param params - the dictionary of parameters           
        @param table - the table to query           
        @return the result of the query           
        """
        u = Utility()
        params = u.remove_empty_items_fr_dict(params)

        list_keys_values = list(params.items())

        field_value_string = ""

        for sing_couple_n in range(len(list_keys_values)):
            if sing_couple_n == 0:
                if type(list_keys_values[sing_couple_n][1]) != "<type 'str'>":
                    field_value_string = table + ".%s == %s" % (
                    list_keys_values[sing_couple_n][0], list_keys_values[sing_couple_n][1])
                else:
                    field_value_string = table + ".%s == u%s" % (
                    list_keys_values[sing_couple_n][0], list_keys_values[sing_couple_n][1])
            else:
                if type(list_keys_values[sing_couple_n][1]) == "<type 'str'>":
                    field_value_string = field_value_string + "," + table + ".%s == %s" % (
                    list_keys_values[sing_couple_n][0], list_keys_values[sing_couple_n][1])
                else:
                    field_value_string = field_value_string + "," + table + ".%s == %s" % (
                    list_keys_values[sing_couple_n][0], list_keys_values[sing_couple_n][1])

                    # field_value_string = ", ".join([table + ".%s == u%s" % (k, v) for k, v in params.items()])

        """
        Per poter utilizzare l'operatore LIKE è necessario fare una iterazione attraverso il dizionario per discriminare tra
        stringhe e numeri
        #field_value_string = ", ".join([table + ".%s.like(%s)" % (k, v) for k, v in params.items()])
        """
        # self.connection()
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        query_str = "session.query(" + table + ").filter(and_(" + field_value_string + ")).all()"
        res = eval(query_str)

        session.close()
        return res
    def query_operator(self, params, table):
        """
         this function takes in a list of tuples and a table name and returns a list of tuples
        that match the query.
        @param params - the list of tuples that contain the field name, operator, and value.
        @param table - the table name.
        @returns a list of tuples that match the query.
        """
        u = Utility()
        #params = u.remove_empty_items_fr_dict(params)
        field_value_string = ''
        for i in params:
            if field_value_string == '':
                field_value_string = '%s.%s %s %s' % (table, i[0], i[1], i[2])
            else:
                field_value_string = field_value_string + ', %s.%s %s %s' % (table, i[0], i[1], i[2])

        query_str = "session.query(" + table + ").filter(and_(" + field_value_string + ")).all()"

        # self.connection()
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        session.close()
        return eval(query_str)

    def query_distinct(self, table, query_params, distinct_field_name_params):
        """
        Query the database for distinct values of the fields in the query_params.
        @param table - the table to query           
        @param query_params - the query parameters           
        @param distinct_field_name_params - the field names to return           
        @return The distinct values of the fields in the query_params           
        """
        
        query_string = ""
        for i in query_params:
            if query_string == '':
                query_string = '%s.%s==%s' % (table, i[0], i[1])
            else:
                query_string = query_string + ',%s.%s==%s' % (table, i[0], i[1])

        distinct_string = ""
        for i in distinct_field_name_params:
            if distinct_string == '':
                distinct_string = '%s.%s' % (table, i)
            else:
                distinct_string = distinct_string + ',%s.%s' % (table, i)

        query_cmd = "session.query(" + distinct_string + ").filter(and_(" + query_string + ")).distinct().order_by(" + distinct_string + ")"
        # self.connection()
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        session.close()
        return eval(query_cmd)

    def query_distinct_sql(self, table, query_params, distinct_field_name_params):
        """
        Given a table name, id, value, column names and values, update the table.
        @param table_class_str - the table name
        @param id_table_str - the id column name
        @param value_id_list - the id value
        @param columns_name_list - the column names
        @param values_update_list - the values to update
        """
        
        query_string = ""
        for i in query_params:
            if query_string == '':
                query_string = '%s=%s' % (i[0], i[1])
            else:
                query_string = query_string + ' AND %s=%s' % (i[0], i[1])

        distinct_string = ""
        for i in distinct_field_name_params:
            if distinct_string == '':
                distinct_string = '%s' % (i)
            else:
                distinct_string = distinct_string + ',%s' % (i)

        query_cmd = "SELECT DISTINCT " + distinct_string + " FROM " + table + ' WHERE ' + query_string
        # self.connection()
        res = self.engine.execute(query_cmd)
        return res

    
    def insert_data_session(self, data):
        """
        Insert the data into the database.
        @param data - the data to be inserted
        """
        Session = sessionmaker(bind=self.engine, autoflush=False)
        session = Session()
        session.add(data)
        session.commit()
        session.close()
    def insert_data_conflict(self, data):
        """
        Insert the data into the database.
        @param data - the data to be inserted
        """
        Session = sessionmaker(bind=self.engine, autoflush=False)
        session = Session()
        session.begin_nested()
        session.merge(data)
       
        session.commit()
        
        session.close()
    def update(self, table_class_str, id_table_str, value_id_list, columns_name_list, values_update_list):
        """
        Receives 5 values then putted in a list. The values must be passed in this order: table name->string, column_name_where->list containin' one value ('site_table', 'id_sito', [1], ['sito', 'nazione', 'regione', 'comune', 'descrizione', 'provincia'], ['Sito archeologico 1', 'Italiauiodsds', 'Emilia-Romagna', 'Riminijk', 'Sito di epoca altomedievale....23', 'Riminikljlks'])
        @param table_class_str - the table class string
        @param id
        """
       

        self.table_class_str = table_class_str
        self.id_table_str = id_table_str
        self.value_id_list = value_id_list
        self.columns_name_list = columns_name_list
        self.values_update_list = values_update_list

        changes_dict = {}
        u = Utility()
        update_value_list = u.deunicode_list(self.values_update_list)

        column_list = []
        for field in self.columns_name_list:
            column_str = ('%s.%s') % (table_class_str, field)
            column_list.append(column_str)

        u.add_item_to_dict(changes_dict, list(zip(self.columns_name_list, update_value_list)))

        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        # session.query(SITE).filter(and_(SITE.id_sito == '1')).update(values = {SITE.sito:"updatetest"})

        session_exec_str = 'session.query(%s).filter(and_(%s.%s == %s)).update(values = %s)' % (
        self.table_class_str, self.table_class_str, self.id_table_str, self.value_id_list[0], changes_dict)

        
        eval(session_exec_str)
        session.close()
    def update_find_check(self, table_class_str, id_table_str, value_id, find_check_value):
        """
        Update the find_check value for a given table class and id.
        @param table_class_str - the table class string
        @param id_table_str - the id table string
        @param value_id - the value id
        @param find_check_value - the find_check value
        """
        self.table_class_str = table_class_str
        self.id_table_str = id_table_str
        self.value_id = value_id
        self.find_check_value = find_check_value

        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()

        session_exec_str = 'session.query(%s).filter(%s.%s == %s)).update(values = {"find_check": %d})' % (
        self.table_class_str, self.table_class_str, self.id_table_str, self.value_id, find_check_value)

        eval(session_exec_str)
        session.close()
    def empty_find_check(self, table_class_str, find_check_value):
        """
        Given a table name and a find check value, update the find_check value for that table.
        @param table_class_str - the table name           
        @param find_check_value - the find check value           
        """
        self.table_class_str = table_class_str
        self.find_check_value = find_check_value

        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()

        session_exec_str = 'session.query(%s).update(values = {"find_check": %d})' % (self.table_class_str, 0)

        eval(session_exec_str)
        session.close()
    def delete_one_record(self, tn, id_col, id_rec):
        """
        Delete a record from a table.
        @param tn - the table name
        @param id_col - the id column
        @param id_rec - the id record
        """
        
        self.table_name = tn
        self.id_column = id_col
        self.id_rec = id_rec
        # self.connection()
        table = Table(self.table_name, self.metadata, autoload=True)
        exec_str = ('%s%s%s%d%s') % ('table.delete(table.c.', self.id_column, ' == ', self.id_rec, ').execute()')

        eval(exec_str)
        
    def max_num_id(self, tc, f):
        self.table_class = tc
        self.field_id = f

        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        exec_str = "session.query(func.max({}.{}))".format(self.table_class, self.field_id)
        max_id_func = eval(exec_str)
        res_all = max_id_func.all()
        res_max_num_id = res_all[0][0]
        session.close()
        if not res_max_num_id:
            return 0
        else:
            return int(res_max_num_id)
        
    # def max_num_id2(self, tc, f):
        # self.table_class = tc
        # self.field_id = f

        # Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        # session = Session()
        # exec_str = "session.query(func.max({}.{}))".format(self.table_class, self.field_id)
        # exec_str = exec_str.on_conflict_do_nothing(index_elements="{}".format( self.field_id))
        # max_id_func = eval(exec_str)
        # res_all = max_id_func.all()
        # res_max_num_id = res_all[0][0]
        # session.close()
        # if not res_max_num_id:
            # return 0
        # else:
            # return int(res_max_num_id)
    
    def dir_query(self):
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()

        # session.query(SITE).filter(SITE.id_sito == '1').update(values = {SITE.sito:"updatetest"})
        # return session.query(SITE).filter(and_(SITE.id_sito == 1)).all()
        # return os.environ['HOME']

        session.close()# managements utilities
        
    def fields_list(self, t, s=''):
        """return the list of columns in a table. If s is set a int,
        return only one column"""
        self.table_name = t
        self.sing_column = s
        table = Table(self.table_name, self.metadata, autoload=True)

        if not str(s):
            return [c.name for c in table.columns]
        else:
            return [c.name for c in table.columns][int(s)]

    def query_in_idus(self, id_list):
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        res = session.query(US).filter(US.id_us.in_(id_list)).all()

        session.close()

        return res

    def query_sort(self, id_list, op, to, tc, idn):
        self.order_params = op
        self.type_order = to
        self.table_class = tc
        self.id_name = idn

        filter_params = self.type_order + "(" + self.table_class + "." + self.order_params[0] + ")"

        for i in self.order_params[1:]:
            filter_temp = self.type_order + "(" + self.table_class + "." + i + ")"

            filter_params = filter_params + ", " + filter_temp

        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()

        cmd_str = "session.query({0}).filter({0}.{1}.in_(id_list)).order_by({2}).all()".format(self.table_class,
                                                                                               self.id_name,
                                                                                               filter_params)
        s = eval(cmd_str)
        session.close()
        return s

    def run(self, stmt):
        rs = stmt.execute()
        res_list = []
        for row in rs:
            res_list.append(row[0])
        #session.close()
        return res_list

    def update_for(self):
        """
        table = Table('us_table_toimp', self.metadata, autoload=True)
        s = table.select(table.c.id_us > 0)
        res_list = self.run(s)
        cont = 11900
        for i in res_list:
            self.update('US_toimp', 'id_us', [i], ['id_us'], [cont])
            cont = cont+1
        """
        table = Table('inventario_materiali_table_toimp', self.metadata, autoload=True)
        s = table.select(table.c.id_invmat > 0)
        res_list = self.run(s)
        cont = 900
        for i in res_list:
            self.update('INVENTARIO_MATERIALI_TOIMP', 'id_invmat', [i], ['id_invmat'], [cont])
            cont = cont + 1

    def group_by(self, tn, fn, CD):
        """Group by the values by table name - string, field name - string, table class DB from mapper - string"""
        self.table_name = tn
        self.field_name = fn
        self.table_class = CD

        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        s = eval('select([{0}.{1}]).group_by({0}.{1})'.format(self.table_class, self.field_name))
        session.close()
        return self.engine.execute(s).fetchall()

    def query_where_text(self, c, v):
        self.c = c
        self.v = v
        # self.connection()
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()

        string = ('%s%s%s%s%s') % ('session.query(PERIODIZZAZIONE).filter_by(', self.c, "='", self.v, "')")

        res = eval(string)
        session.close()
        return res

    def update_cont_per(self, s):
        self.sito = s

        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()

        string = ('%s%s%s%s%s') % ('session.query(US).filter_by(', 'sito', "='", str(self.sito), "')")
        # print string
        session.close()
        lista_us = eval(string)

        for i in lista_us:
            if not i.periodo_finale and i.periodo_iniziale:
                    periodiz = self.query_bool(
                        {'sito': "'" + str(self.sito) + "'", 'periodo': i.periodo_iniziale, 'fase': "'" +str(i.fase_iniziale)+ "'"},
                        'PERIODIZZAZIONE')
                    self.update('US', 'id_us', [int(i.id_us)], ['cont_per'], [periodiz[0].cont_per])
            
            elif not i.periodo_iniziale:
                periodiz = self.query_bool(
                        {'sito': "'" + str(self.sito) + "'", 'periodo': i.periodo_iniziale, 'fase': "'" +str(i.fase_iniziale)+ "'"},
                        'PERIODIZZAZIONE')
                self.update('US', 'id_us', [int(i.id_us)], ['cont_per'], [periodiz[0].cont_per])
                continue
            elif i.periodo_finale and i.periodo_iniziale:
                # try:
                cod_cont_iniz_temp = self.query_bool(
                    {'sito': "'" + str(self.sito) + "'", 'periodo': int(i.periodo_iniziale),
                     'fase': int(i.fase_iniziale)}, 'PERIODIZZAZIONE')

                cod_cont_fin_temp = self.query_bool(
                    {'sito': "'" + str(self.sito) + "'", 'periodo': int(i.periodo_finale), 'fase': int(i.fase_finale)},
                    'PERIODIZZAZIONE')

                cod_cont_iniz = cod_cont_iniz_temp[0].cont_per
                cod_cont_fin = cod_cont_fin_temp[0].cont_per

                cod_cont_var_n = cod_cont_iniz
                cod_cont_var_txt = str(cod_cont_iniz)
                while cod_cont_var_n != cod_cont_fin:
                    cod_cont_var_n += 1

                    cod_cont_var_txt = cod_cont_var_txt + "/" + str(cod_cont_var_n)

                self.update('US', 'id_us', [int(i.id_us)], ['cont_per'], [cod_cont_var_txt])
                #except:
                    #pass
                # else:
                #     cod_cont_iniz_temp = self.query_bool(
                #         {'sito': "'" + str(self.sito) + "'", 'periodo': int(i.periodo_iniziale),
                #          'fase': int(i.fase_iniziale)}, 'PERIODIZZAZIONE')
                #
                #     cod_cont_fin_temp = self.query_bool(
                #         {'sito': "'" + str(self.sito) + "'", 'periodo': int(i.periodo_finale), 'fase': int(i.fase_finale)},
                #         'PERIODIZZAZIONE')
                #
                #     cod_cont_iniz = cod_cont_iniz_temp[0].cont_per
                #     cod_cont_fin = cod_cont_fin_temp[0].cont_per
                #
                #     cod_cont_var_n = cod_cont_iniz
                #     cod_cont_var_txt = str(cod_cont_iniz)
                #     while cod_cont_var_n != cod_cont_fin:
                #         cod_cont_var_n += 1
                #
                #         cod_cont_var_txt = cod_cont_var_txt + "/" + str(cod_cont_var_n)
                #
                #     self.update('US', 'id_us', [int(i.id_us)], ['cont_per'], [cod_cont_var_txt])
                

    def remove_alltags_from_db_sql(self,s):
        sql_query_string = ("DELETE FROM media_to_entity_table WHERE media_name  = '%s'") % (s)
    
        res = self.engine.execute(sql_query_string)
        # rows= res.fetchall()
        return res    
    
    def remove_tags_from_db_sql(self,s):
        sql_query_string = ("DELETE FROM media_to_entity_table WHERE id_entity  = '%s'") % (s)
    
        res = self.engine.execute(sql_query_string)
        # rows= res.fetchall()
        return res    
    def delete_thumb_from_db_sql(self,s):
        sql_query_string = ("DELETE FROM media_thumb_table WHERE media_filename  = '%s'") % (s)
    
        res = self.engine.execute(sql_query_string)
        # rows= res.fetchall()
        return res    
    def select_medianame_from_st_sql(self,sito,sigla,numero):
        sql_query_string = ("SELECT c.filepath, a.media_name FROM media_to_entity_table as a,  struttura_table as b, media_thumb_table as c WHERE b.id_struttura=a.id_entity and c.id_media=a.id_media  and b.sito= '%s' and b.sigla_struttura='%s' and b.numero_struttura='%s' and entity_type='STRUTTURA'")%(sito,sigla,numero) 
        
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        return rows    
    def select_medianame_from_db_sql(self,sito,area):
        sql_query_string = ("SELECT c.filepath, b.us,a.media_name FROM media_to_entity_table as a,  us_table as b, media_thumb_table as c WHERE b.id_us=a.id_entity and c.id_media=a.id_media  and b.sito= '%s' and b.area='%s'")%(sito,area) 
        
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        return rows
    def select_medianame_tb_from_db_sql(self,sito,area):
        sql_query_string = ("SELECT c.filepath, a.media_name FROM media_to_entity_table as a,  tomba_table as b, media_thumb_table as c WHERE b.id_tomba=a.id_entity and c.id_media=a.id_media  and b.sito= '%s' and b.area='%s'and entity_type='TOMBA'")%(sito,area) 
        
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        return rows

    def select_medianame_pot_from_db_sql(self, sito, area, us):
        sql_query_string = (
                               "SELECT c.filepath, a.media_name FROM media_to_entity_table as a,  pottery_table as b, media_thumb_table as c WHERE b.id_rep=a.id_entity and c.id_media=a.id_media  and b.sito= '%s' and b.area='%s' and b.us = '%s' and entity_type='CERAMICA'") % (
                           sito, area, us)

        res = self.engine.execute(sql_query_string)
        rows = res.fetchall()
        return rows


    def select_medianame_ra_from_db_sql(self,sito,area,us):
        sql_query_string = ("SELECT c.filepath, a.media_name FROM media_to_entity_table as a,  inventario_materiali_table as b, media_thumb_table as c WHERE b.id_invmat=a.id_entity and c.id_media=a.id_media  and b.sito= '%s' and b.area='%s' and b.us = '%s' and entity_type='REPERTO'")%(sito,area,us) 
        
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        return rows
    
    def select_medianame_2_from_db_sql(self,sito,area,us):
        sql_query_string = ("SELECT c.filepath, a.media_name FROM media_to_entity_table as a,  us_table as b, media_thumb_table as c WHERE b.id_us=a.id_entity and c.id_media=a.id_media  and b.sito= '%s' and b.area='%s' and b.us = '%s' and entity_type='US'")%(sito,area,us) 
        
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        return rows
    def select_ra_from_db_sql(self,sito,area,us):
        sql_query_string = ("SELECT n_reperto from inventario_materiali_table WHERE sito = '%s' and area = '%s' and us = '%s'")%(sito,area,us) 
        
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        return rows
    def select_coord_from_db_sql(self,sito,area,us):
        sql_query_string = ("SELECT coord from pyunitastratigrafiche WHERE scavo_s = '%s' and area_s = '%s' and us_s = '%s'")%(sito,area,us) 
        
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        return rows
    
    def select_medianame_3_from_db_sql(self,sito,area,us):
        sql_query_string = ("SELECT c.filepath, b.us,a.media_name FROM media_to_entity_table as a,  inventario_materiali_table as b, media_thumb_table as c WHERE b.id_invmat=a.id_entity and c.id_media=a.id_media  and b.sito= '%s' and b.area='%s' and us = '%s'")%(sito,area,us) 
        
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        return rows
    
    def select_thumbnail_from_db_sql(self,sito):
        sql_query_string = ("SELECT c.filepath, group_concat ((select us from us_table where id_us like id_entity))as us,a.media_name,b.area,b.unita_tipo FROM  media_to_entity_table as a,  us_table as b, media_thumb_table as c WHERE b.id_us=a.id_entity and c.id_media=a.id_media and sito='%s' group by a.media_name order by a.media_name asc")%(sito)
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        return rows
    
    def select_quote_from_db_sql(self, sito, area, us):
        sql_query_string = ("SELECT * FROM pyarchinit_quote WHERE sito_q = '%s' AND area_q = '%s' AND us_q = '%s'") % (
        sito, area, us)
        res = self.engine.execute(sql_query_string)
        return res
    def select_us_from_db_sql(self, sito, area, us, stratigraph_index_us):
        sql_query_string = (
                           "SELECT * FROM pyunitastratigrafiche WHERE scavo_s = '%s' AND area_s = '%s' AND us_s = '%s' AND stratigraph_index_us = '%s'") % (
                           sito, area, us, stratigraph_index_us)
        res = self.engine.execute(sql_query_string)
        return res

    def select_us_doc_from_db_sql(self, sito, tipo_doc, nome_doc):
        sql_query_string = (
                           "SELECT * FROM pyunitastratigrafiche WHERE scavo_s = '%s' AND tipo_doc = '%s' AND nome_doc = '%s'") % (
                           sito, tipo_doc, nome_doc)
        res = self.engine.execute(sql_query_string)
        return res

    def select_usneg_doc_from_db_sql(self, sito, tipo_doc, nome_doc):
        sql_query_string = (
                           "SELECT * FROM pyarchinit_us_negative_doc WHERE sito_n = '%s' AND  tipo_doc_n = '%s' AND nome_doc_n = '%s'") % (
                           sito, tipo_doc, nome_doc)
        res = self.engine.execute(sql_query_string)
        return res

    def select_db_sql(self, table):
        sql_query_string = ("SELECT * FROM %s") % table
        res = self.engine.execute(sql_query_string)
        return res
    
    def select_db_sql_2(self, sito,area,us,d_stratigrafica):
        sql_query_string = ("SELECT * FROM us_table as a where a.sito='%s' AND a.area='%s' AND a.us='%s' AND a.d_stratigrafica='%s'") % (sito,area,us,d_stratigrafica)
        res = self.engine.execute(sql_query_string)
        rows= res.fetchall()
        
        return rows
    
    
    def test_ut_sql(self,unita_tipo):
        sql_query_string = ("SELECT %s FROM us_table")% (unita_tipo)
        res = self.engine.execute(sql_query_string)
        return res
    
    def query_in_contains(self, value_list, sitof, areaf):
        self.value_list = value_list
       
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()

        res_list = []
        n = len(self.value_list) - 1
        # QMessageBox.warning(None, "Messaggio", str(n), QMessageBox.Ok)
        while self.value_list:
            chunk = self.value_list[0:n]
            self.value_list = self.value_list[n:]
            res_list.extend(session.query(US).filter_by(sito=sitof).filter_by(area=areaf).filter(
                or_(*[US.rapporti.contains(v) for v in chunk])))
            # res_list.extend(us for us, in session.query(US.us).filter(or_(*[US.rapporti.contains(v) for v in chunk])))
        session.close()
        return res_list

    def insert_arbitrary_number_of_us_records(self, us_range, sito, area, n_us, unita_tipo):
        id_us = self.max_num_id('US', 'id_us')
        
        l=QgsSettings().value("locale/userLocale")[0:2]

        for i in range(us_range):
            id_us += 1

            data_ins = self.insert_values(id_us, sito, area, n_us, '', '', '', '', '', '', '', '', '', '', '', '', '[]',
                                          '[]', '[]', '', '', '', '', '', '', '', '', '0', '[]', unita_tipo, '', '', '', '',
                                          '', '', '', '', '', '', '', '', '', None, None, '', '[]','[]', '[]', '[]', '[]','','','','',None,None,'','','','','','','[]','[]',None,None,None,None,None,None,None,None,None,None,'','','','','','','','','','',None,None,None,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','')
                                           
            self.insert_data_session(data_ins)
            n_us += 1
        return

    
    # def insert_number_of_rapp_records(self, sito, area, us, rapp_n, unita_tipo):
        # id_us = self.max_num_id('US', 'id_us')
        
        # l=QgsSettings().value("locale/userLocale")[0:2]

        
        # id_us += 1

        # data_ins = self.insert_values(id_us, sito, area, us, '', '', '', '', '', '', '', '', '', '', '', '', '[]',
                                      # '[]', 
                                      # '[['+rapp_n+']]', '', '', '', '', '', '', '', '', '0', '[]', unita_tipo, '', '', '', '',
                                      # '', '', '', '', '', '', '', '', '', None, None, '', '[]','[]', '[]', '[]', '[]','','','','',None,None,'','','','','','','[]','[]',None,None,None,None,None,None,None,None,None,None,'','','','','','','','','','',None,None,None,'','','','','','','','','','','','','','','','','','','','','','','','','','','','','')
                                           
        # self.insert_data_session(data_ins)
        
        # return
    
    def insert_number_of_us_records(self, sito, area, n_us):
        id_us = self.max_num_id('US', 'id_us')
        #text = "SCHEDA CREATA IN AUTOMATICO"
        l=QgsSettings().value("locale/userLocale")[0:2]

        if l == 'it':
            text = "SCHEDA CREATA IN AUTOMATICO"
            unita_tipo='US'
        else:
            text = "FORM MADE AUTOMATIC"
            unita_tipo = 'SU'
        id_us += 1

        data_ins = self.insert_values(id_us, sito, area, n_us, '', '', '', '', '', '', '', '', '', '', '', '', '[]',
                                      '[]', '[]', '', '', '', '', '', '', '', '', '0', '[]', unita_tipo, '', '', '', '',
                                      '', '', '', '', '', '', '', '', '', None, None, '', '[]', '[]', '[]', '[]', '[]',
                                      '', '', '', '', None, None, '', '', '', '', '', '', '[]', '[]', None, None, None,
                                      None, None, None, None, None, None, None, '', '', '', '', '', '', '', '', '', '',
                                      None, None, None, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                                      '', '', '', '', '', '', '', '', '', '', '', '', '')

        self.insert_data_session(data_ins)

        return
    
    def insert_number_of_reperti_records(self, sito, numero_invetario):
        id_invmat = self.max_num_id('INVENTARIO_MATERIALI', 'id_invmat')
        
        l=QgsSettings().value("locale/userLocale")[0:2]

        
        id_invmat += 1

        data_ins = self.insert_values_reperti(id_invmat, sito, numero_invetario, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', None, None, '', None, '', '','0','','')
                                           
        self.insert_data_session(data_ins)
        
        
        return

    def insert_number_of_pottery_records(self,  id_number,sito, area,us):
        id_rep = self.max_num_id('POTTERY', 'id_rep')

        l = QgsSettings().value("locale/userLocale")[0:2]

        id_rep += 1

        data_ins = self.insert_pottery_values(id_rep, id_number, sito, area, us, 0, '', '', 0, '', '', '', '',
                                              '', '', '', '', '', '', '', '', '', '', None, 0, None, None, None, None, '',
                                              0,'')

        self.insert_data_session(data_ins)

        return
    
    
    
    def insert_number_of_tomba_records(self, sito, nr_scheda_taf):
        id_tomba = self.max_num_id('TOMBA', 'id_tomba')
        
        l=QgsSettings().value("locale/userLocale")[0:2]

        
        id_tomba += 1

        data_ins = self.insert_values_tomba(id_tomba, sito, '', nr_scheda_taf, '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '','')
                                           
        self.insert_data_session(data_ins)
        
        return
    def insert_struttura_records(self, sito, sigla_struttura,numero_struttura):
        id_struttura = self.max_num_id('STRUTTURA', 'id_struttura')
        
        l=QgsSettings().value("locale/userLocale")[0:2]

        
        id_struttura += 1

        data_ins = self.insert_struttura_values(id_struttura, sito, sigla_struttura, numero_struttura, '', '', '', '', '', '', '', '', '', '', '', '', '', '')
                                           
        self.insert_data_session(data_ins)
        
        return
    def select_like_from_db_sql(self, rapp_list, us_rapp_list):
        # this is a test
        pass

    ##      self.us_rapp_list = us_rapp_list
    ##      rapp_type = rapp_list
    ##      query_string_base = """session.query(US).filter(or_("""
    ##      query_list = []
    ##
    ##      #costruisce la stringa che trova i like
    ##      for sing_us_rapp in self.us_rapp_list:
    ##          for sing_rapp in rapp_type:
    ##              sql_query_string = """US.rapporti.contains("[u'%s', u'%s']")""" % (sing_rapp,sing_us_rapp) #funziona!!!
    ##              query_list.append(sql_query_string)
    ##
    ##      string_contains = ""
    ##      for sing_contains in range(len(query_list)):
    ##          if sing_contains == 0:
    ##              string_contains = query_list[sing_contains]
    ##          else:
    ##              string_contains = string_contains + "," + query_list[sing_contains]
    ##
    ##      query_string_execute = query_string_base + string_contains + '))'
    ##
    ##      Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
    ##      session = Session()
    ##      res = eval(query_string_execute)
    ##
    ##      return res

    def select_not_like_from_db_sql(self, sitof, areaf):
        # NB per funzionare con postgres è necessario che al posto di " ci sia '
        l=QgsSettings().value("locale/userLocale")[0:2]
        Session = sessionmaker(bind=self.engine, autoflush=True, autocommit=True)
        session = Session()
        
        if l=='it':
            res = session.query(US).filter_by(sito=sitof).filter_by(area=areaf).filter(
                and_(~US.rapporti.like("%'Copre'%"), ~US.rapporti.like("%'Riempie'%"),
                     ~US.rapporti.like("%'Taglia'%"), ~US.rapporti.like("%'Si appoggia a'%")))
                # MyModel.query.filter(sqlalchemy.not_(Mymodel.name.contains('a_string')))
        elif l=='en':
            res = session.query(US).filter_by(sito=sitof).filter_by(area=areaf).filter(
                and_(~US.rapporti.like("%'Cuts'%"), ~US.rapporti.like("%'Abuts'%"),
                     ~US.rapporti.like("%'Covers'%"), ~US.rapporti.like("%'Fills'%")))
            # MyModel.query.filter(sqlalchemy.not_(Mymodel.name.contains('a_string')))
        elif l=='de':
            res = session.query(US).filter_by(sito=sitof).filter_by(area=areaf).filter(
                and_(~US.rapporti.like("%'Schneidet'%"), ~US.rapporti.like("%'Stützt sich auf'%"),
                     ~US.rapporti.like("%'Liegt über'%"), ~US.rapporti.like("%'Verfüllt'%")))
            # MyModel.query.filter(sqlalchemy.not_(Mymodel.name.contains('a_string')))
        session.close()
        #QMessageBox.warning(None, "Messaggio", "DATA LIST" + str(res), QMessageBox.Ok)
        return res
        
    def query_in_idusb(self):
        pass


# def main():
    # db = Pyarchinit_db_management('sqlite:////Users//Luca//pyarchinit_DB_folder//pyarchinit_db.sqlite')
    # db.connection()

    # db.insert_arbitrary_number_of_records(10, 'Giorgio', 1, 1, 'US')  # us_range, sito, area, n_us)
    

# if __name__ == '__main__':
    # main()
class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)
  
    def style_text(code):
        return "\33[{code}m".format(code=code)
  
    def color_text(code):
        return "\33[{code}m".format(code=code)
  
  
