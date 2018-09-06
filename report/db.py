#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mongoengine
from mongoengine import register_connection
from mongoengine.connection import disconnect

class ConnectCompany:

    def __init__(self):
        """
        Instance of Collections from MongoDB
        The collections is instance of Company Service
        URL_DATA_COMPANY,PORT_DATA_COMPANY is defined in .env
        """
        self.connection_company = register_connection('db_company',db='db_challenge', host='mongodb://'+os.environ.get('URI_DATA_COMPANY'))

class ConnectComplains:
    
    def __init__(self):
        """
        Instance of Collections from MongoDB
        The collections is instance of Complains Service
        URL_DATA_COMPLAINS/PORT_DATA_COMPLAINS is defined in .env
        """
        self.connection_complains = register_connection('default',db='db_challenge',host='mongodb://'+os.environ.get('URI_DATA_COMPLAINS'))