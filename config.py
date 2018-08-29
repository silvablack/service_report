#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

__author__ = "Paulo Silva"
__version__ = "1.0.0"
__email__ = "paulosilvadev3@gmail.com"

class Config(object):
    """Class contain a general settings"""
    DEBUG = False

class DevelopmentConfig(Config):
    """Development settings"""
    DEBUG = True

class TestingConfig(Config):
    """Test settings"""
    DEBUG = True
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': Config
}