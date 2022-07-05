#! /usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import shutil
import subprocess


class Pyarchinit_OS_Utility(object):
    """

    .. module:: argparse_actions

    Pyarchinit_OS_Utility

    """

    def create_dir(self, d):
        '''Create directory

        :param  str  - path directory

        '''
        dirname = d

        try:
            os.makedirs(dirname)
            return 1
        except OSError:
            if os.path.exists(dirname):
                # We are nearly safe
                return 0  # la cartella esiste
            else:
                # There was an error on creation, so make sure we know about it
                raise

    def copy_file_img(self, f, d):

        file_path = os.path.normpath(f)
        destination = os.path.normpath(d)
        shutil.copy(file_path, destination)
        return 0


    def copy_file(self, f, d):
        """Copy file

        :param str: - file path

        :param str: - destination file

        """
        file_path = os.path.normpath(f)
        destination = os.path.normpath(d)
        if os.access(destination, 0):
            return 0  # la cartella esiste
        else:
            try:
                shutil.copy(file_path, destination)
                return 1
            except OSError:
                if os.path.exists(destination):
                    return 0
                else:
                    raise

    @staticmethod
    def checkGraphvizInstallation():
        '''Return True if Graphviz is installed '''
        try:
            subprocess.call(['dot', '-V'])
            return True
        except Exception as e:
            return False
    
    @staticmethod
    def checkPostgresInstallation():
        '''Return True if Postgres is installed '''

        try:
            subprocess.call(['pg_dump','-V'])
            return True
        except Exception as e:
            return False
    
    
    @staticmethod
    def isWindows():
        '''Return True if platform is Windows '''
        return os.name == 'nt'

    @staticmethod
    def isMac():
        '''Return True if platform is mac '''
        return sys.platform == 'darwin'
