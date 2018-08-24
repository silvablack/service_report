#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest
from mock import Mock

from report import controllers

class TestReportController():
    """
    Class to build a tests unit to Report Controller
    """
    
    def test_build_report(self):
        """
        Test method build report
        """
        mockdb = Mock() #Build mock to DB call
        input_expected = {
            'city':'São Luís'.encode('utf8'), 
            'uf':'MA',
            'company':'5b74e44d6906800036631800'
        } # Expected call input
        controllers.ReportController.build_report(controllers.ReportController, input_expected, mockdb)
        mockdb.find_report.assert_called_with(input_expected)
