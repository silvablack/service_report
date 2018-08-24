#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from flask import url_for

class TestReportService:
    """
    Class to Test Integration with Report Service
    """

    def test_index(self, client):
        """
        Test default route /
        Should return title and version
        """
        res = client.get(url_for('index'))
        assert res.status_code == 200
        assert res.json == {
            'title': 'Report Service',
            'version': '1.0.0'
        }

    def test_report(self, client):
        """
        Test report route /report
        Should return list in json object that contains city, uf, company_id, company_name, total_complains
        """
        res = client.get(url_for('report', city='São Luís', uf='MA', company='5b74e44d6906800036631800'))
        assert res.status_code == 200
        assert res.json == {
            'city': 'São Luís'.encode('utf8'),
            'uf': 'MA',
            'company_id': '5b74e44d6906800036631800',
            'company_name': 'CEMAR - Companhia Elétrica'.encode('utf8'),
            'total_complains': 1
        }