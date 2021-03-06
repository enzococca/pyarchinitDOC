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

from __future__ import absolute_import

import os
import subprocess

import sys
import time
import shutil

from builtins import range
from builtins import str
from ..modules.utility.pyarchinit_OS_utility import Pyarchinit_OS_Utility
from ..modules.utility.settings import Settings
from ..modules.db.pyarchinit_conn_strings import Connection
from qgis.core import *
from qgis.PyQt import QtCore
from qgis.PyQt.QtCore import QRectF, pyqtSignal, QObject,pyqtSlot,Qt
from qgis.PyQt.QtWidgets import QApplication, QDialog, QMessageBox,  QProgressDialog, QProgressBar,QWidget,QLabel,QVBoxLayout, QFileDialog
from qgis.PyQt.uic import loadUiType

MAIN_DIALOG_CLASS, _ = loadUiType(os.path.join(os.path.dirname(__file__), 'ui', 'dbmanagment.ui'))


class pyarchinit_dbmanagment(QDialog, MAIN_DIALOG_CLASS):
    
    MSG_BOX_TITLE = \
        'PyArchInit - pyarchinit_version 0.4 - Scheda gestione DB'
    HOME = os.environ['PYARCHINIT_HOME']
    BK = '{}{}{}'.format(HOME, os.sep, "pyarchinit_db_backup")
    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.setupUi(self)
        
        # self.customize_GUI() #call for GUI customizations

        self.currentLayerId = None
        
    def enable_button(self, n):

        self.backup.setEnabled(n)

    def enable_button_search(self, n):

        self.backup.setEnabled(n)

    
    
    
    
    def on_backupsqlite_pressed(self):
        conn = Connection()
        conn_str = conn.conn_str()
        
        a = conn_str.lstrip('sqlite:///')
        home = os.environ['PYARCHINIT_HOME']
        # conn_import = '%s%s%s' % (home, os.sep,
                                  # 'pyarchinit_DB_folder/pyarchinit_db.sqlite'
                                  # )
        
        
        
        #conn_export = '%s%s%s' % (home, os.sep,
                                  #'pyarchinit_db_backup/pyarchinit_db_'
                                  #+ time.strftime('%Y%m%d_%H_%M_%S_')
                                  #+ '.sqlite')
       
        
        PDF_path = '%s%s%s' % (home, os.sep, 'pyarchinit_db_backup/')
        
        cfg_rel_path = os.path.join(os.sep, 'pyarchinit_DB_folder', 'config.cfg')
        file_path = '{}{}'.format(home, cfg_rel_path)
        conf = open(file_path, "r")

        data = conf.read()
        settings = Settings(data)
        settings.set_configuration()
        conf.close()    
        
        dump_dir = PDF_path
        db_username = settings.USER
        host = settings.HOST
        port = settings.PORT
        database_password=settings.PASSWORD
        
        db_names = settings.DATABASE
        conn_export = '%s' % (dump_dir+'backup_'+db_names)
                                 
        b=shutil.copy(a,conn_export)
    
        i = 0
    
        for c in b:
            
            if i==0:
                self.progress = self.progressBar_db#("Please Wait!", "Cancel", 0, 100, MainWindow)
                
                self.progress.setWindowModality(Qt.WindowModal)
                
                self.progress.setWindowTitle("Loading, Please Wait! (Cloudflare Protection)")
                
                self.progress.setMinimum(0)

                self.progress.setMaximum(100)

                self.progress.resize(1000,100)

                self.progress.show()

                self.progress.setValue(0)

                self.progress.setValue(100) 
                self.setLayout(QVBoxLayout())
                self.layout().addWidget(self.progress)
                
                
            else:
                self.image = QLabel('Backup Falied')
                self.image.setAlignment(Qt.AlignCenter)
                self.layout().addWidget(self.image)
            
    def on_backup_pressed(self):

        home = os.environ['PYARCHINIT_HOME']

        PDF_path = '%s%s%s' % (home, os.sep, 'pyarchinit_db_backup/')
        
        cfg_rel_path = os.path.join(os.sep, 'pyarchinit_DB_folder', 'config.cfg')
        file_path = '{}{}'.format(home, cfg_rel_path)
        conf = open(file_path, "r")

        data = conf.read()
        settings = Settings(data)
        settings.set_configuration()
        conf.close()    
        
        dump_dir = PDF_path
        db_username = settings.USER
        host = settings.HOST
        port = settings.PORT
        database_password=settings.PASSWORD
        
        db_names = settings.DATABASE

        
        dumper = '-U %s -h %s -p %s -Z 9 -f %s -Fc %s'

        bkp_file = '%s_%s.backup' % (db_names,
                                  time.strftime('%Y%m%d_%H_%M'))

        file_path = os.path.join(dump_dir, bkp_file)
        command = 'pg_dump ' + dumper % (db_username, host, port, file_path,db_names)
        try:
            p=subprocess.Popen(command, shell=False)
        except Exception as e :
            QMessageBox.warning(self, "INFO", str(e), QMessageBox.Ok)
        #subprocess.call('gzip ' + file_path, shell=False)
        
        i = 0
    
        for c in command:
            if i==0:
                self.progress = self.progressBar_db#("Please Wait!", "Cancel", 0, 100, MainWindow)
                    
                self.progress.setWindowModality(Qt.WindowModal)
              
                self.progress.setMinimum(0)

                self.progress.setMaximum(100)

                self.progress.setWindowTitle("Loading, Please Wait! (Cloudflare Protection)")
                
                self.progress.resize(1000,100)

                self.progress.show()

                self.progress.setValue(0)

                self.progress.setValue(100) 
                self.setLayout(QVBoxLayout())
                self.layout().addWidget(self.progress)
            
            
            else:
                self.image = QLabel('Backup Falied')
                self.image.setAlignment(Qt.AlignCenter)
                self.layout().addWidget(self.image)
    # def on_backup_total_pressed(self):

        # home = os.environ['PYARCHINIT_HOME']
        # PDF_path = '%s%s%s' % (home, os.sep, 'pyarchinit_db_backup/')
        # filename = '%s%s%s' % (PDF_path, os.sep, 'semivariogramma.png')

        # username = 'postgres'

        # defaultdb = 'postgres'

        # port = '5432'

        # backupdir = PDF_path

        # date = time.strftime('%Y-%m-%d-%H-%M-%S')

        # GET DB NAMES

        # get_db_names = \
            # "psql -U%s -d%s -p%s --tuples-only -c '\l' | awk -F\| '{ print $1 }' | grep -E -v '(template0|template1|^$)'" \
            # % (username, defaultdb, port)

        # MAKE BACKUP OF SYSTEMGRANTS

        # os.popen('pg_dumpall -p%s -g|gzip -9 -c > %s/system.%s.gz'
                 # % (port, backupdir, date))

        # MAKING DB BACKUP

        # for base in os.popen(get_db_names).readlines():
            # try:

                # app = QtGui.QApplication(sys.argv)

                # barra = QProgressBar(self)
                # barra.show()
                # barra.setMinimum(0)
                # barra.setMaximum(9)
                # for a in range(10):
                    # time.sleep(1)
                    # barra.setValue(a)

                # app.exec_()....

                # base = base.strip()
                # fulldir = backupdir + base
                # if not os.path.exists(fulldir):
                    # os.mkdir(fulldir)
                # filename = '%s/%s-%s.sql' % (fulldir, base, date)
                # os.popen('nice -n 19 pg_dump -C -F c -U%s -p%s %s > %s'
                         # % (username, port, base, filename))
                # QMessageBox.warning(self, 'Messaggio',
                                    # 'Backup completato', QMessageBox.Ok)
            # except Exception as e:
                # QMessageBox.warning(self, 'Messaggio',
                                    # 'Backup fallito!!' + str(e),
                                    # QMessageBox.Ok)

    
    def on_upload_pressed(self):
        s = QgsSettings()
        dbpath = QFileDialog.getOpenFileName(
            self,
            "Set file name",
            self.BK,
            " backup (*.backup)"
        )[0]
        #filename=dbpath.split("/")[-1]
        if dbpath:
            self.lineEdit_bk_path.setText(dbpath)
            s.setValue('',dbpath)
        
    def on_restore_pressed(self):
        try:

            # barra = QProgressBar(self)
            # barra.show()
            # barra.setMinimum(0)
            # barra.setMaximum(9)
            # for a in range(10):
                # time.sleep(1)
                # barra.setValue(a)

            path = self.lineEdit_bk_path.text()
            
            home = os.environ['PYARCHINIT_HOME']

            BK_path = '%s%s%s' % (home, os.sep, 'pyarchinit_db_backup/')
            
            cfg_rel_path = os.path.join(os.sep, 'pyarchinit_DB_folder', 'config.cfg')
            file_path = '{}{}'.format(home, cfg_rel_path)
            conf = open(file_path, "r")

            data = conf.read()
            settings = Settings(data)
            settings.set_configuration()
            conf.close()    
            
            dump_dir = BK_path
            db_username = self.lineEdit_username_wt.text()
            host = self.lineEdit_host_wt.text()
            port = self.lineEdit_port_wt.text()
            database_password=self.lineEdit_pass_wt.text()
            
            db_names = self.lineEdit_database_wt.text()
            #os.popen('dropdb -U postgres pyarchinit')
            drop = '-h %s -p %s -U %s %s'
            command1 ='dropdb ' + drop%(host,port,db_username,db_names)
            try:
                subprocess.call(command1, shell=False)
            except:
                pass
            create = '-h %s -p %s -U %s -e %s -E UTF8 -T template_postgis'
            command2 = 'createdb ' + create%(host,port,db_username,db_names)
            subprocess.call(command2, shell=False)
            
            #os.popen('createdb -U postgres -p 5432 -h localhost -E UTF8  -T template_postgis_20 -e pyarchinit')
            restore='--host %s --port %s --username %s --dbname %s --role postgres  %s'
            command= 'pg_restore ' + restore %(host,port,db_username,db_names, path)
            
            
            subprocess.call(command, shell=False)
                
            QMessageBox.warning(self, 'Messaggio',
                                'Ripristino completato', QMessageBox.Ok)
        except Exception as e:
            QMessageBox.warning(self, 'Messaggio',
                                'Ripristino fallito!!' + str(e),
                                QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = pyarchinit_dbmanagment()
    ui.show()
    sys.exit(app.exec_())
