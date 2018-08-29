#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest, datetime, json
from bson.objectid import ObjectId
from flask import url_for
from report.db import ConnectCompany, ConnectComplains
from report import models
from mongoengine.context_managers import switch_db

class TestReportService:
    """
    Class to Test Integration with Report Service
    """

    def before_action(self):
        ConnectCompany()
        ConnectComplains()
        company_id = []
        with switch_db(models.Companies, 'db_company') as Companies:
            company = Companies(name = 'CAEMA - Companhia de Águas e Esgotos', mail = 'caema@email.com',cnpj = '29545078000173').save()
            company_id = company.id

        complain_id = []
        with switch_db(models.Complains, 'default') as Complains:
            locale = models.Locale(city = 'São Luís',uf = 'MA',state = 'Maranhão')
            Complains(title = 'Corte de Água Indevido',description = 'Fizeram o corte sem comunicar o habitante'.encode('utf-8'), locale = locale,company_id = str(company_id), date_created=datetime.datetime.utcnow()).save()
            complain_id = Complains.id

        return {
            'clns_id': complain_id,
            'cpn_id':company_id
        }
        
    def after_action(self):
        ConnectCompany()
        ConnectComplains()
        with switch_db(models.Companies, 'db_company') as Companies:
            Companies.objects({}).delete()

        with switch_db(models.Complains, 'default') as Complains:
            Complains.objects({}).delete()


    def test_index(self, client):
        """
        Test default route /
        Should return title and version
        """
        res = client.get(url_for('index'))
        assert res.status == '200 OK'
        assert res.json == {
            'title': 'Report Service',
            'version': '1.0.0'
        }

    def test_report(self, client):
        """
        Test report route /report
        Should return list in json object that contains city, uf, company_id, company_name, total_complains
        """
        data_expected = self.before_action()
        res = client.get(url_for('report', city='São Luís', uf='MA', company=data_expected['cpn_id']))
        self.after_action()
        assert res.json == {
            'city': 'São Luís',
            'uf': 'MA',
            'company_id': str(data_expected['cpn_id']),
            'company': 'CAEMA - Companhia de Águas e Esgotos',
            'total_complains': 1
        }
        assert res.status == '200 OK'