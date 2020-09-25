# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 00:20:18 2020

@author: huyue
"""
import configparser

class config():
        
    def getconf(self,file_path):
        
        config = configparser.ConfigParser()
        config.read(file_path)
        
        return config
    

