#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json
from bson.objectid import ObjectId
from mongoengine import Document, EmbeddedDocument, fields
from mongoengine.context_managers import switch_db
from report.db import ConnectCompany, ConnectComplains

class Companies(Document):
    """
    Schema to Document for Companies
    """
    name = fields.StringField(required=True)
    mail = fields.EmailField()
    cnpj = fields.StringField()

    meta = {'Companies': 'db_company'}

class Locale(EmbeddedDocument):
    """
    Schema to Embedded Document for Locale in Complains
    """
    city = fields.StringField(required=True)
    uf = fields.StringField(required=True)
    state = fields.StringField(required=True)

class Complains(Document):
    """
    Schema to Document for Complais
    """
    title = fields.StringField(required=True)
    description = fields.StringField(required=True)
    locale = fields.EmbeddedDocumentField(Locale)
    company_id = fields.StringField()
    date_created = fields.DateTimeField(required=True)
    date_updated = fields.DateTimeField()

    meta = {'Complains': 'default'}


class SearchComplainsByCity(object):
    """
    Class to Search Complains By City
    Builds the report from the parameters
    """

    def find_report(objs):
        ConnectComplains() #register complains connection
        ConnectCompany() #register company connection

        with switch_db(Companies, 'db_company') as Ca:
            company = Ca.objects(id=ObjectId(objs['company']))
        
        with switch_db(Complains, 'default') as Co:
            complains = Co.objects.filter(company_id=objs['company'],locale__city=objs['city'], locale__uf=objs['uf']).all()
        
        if(len(company)==1): # CHECK IF COMPANY EXISTS
            for x in company:
                company_name = x.name
            # build data json
            data = {
                'company': company_name,
                'city': objs['city'],
                'uf': objs['uf'],
                'company_id': objs['company'],
                'total_complains': complains.count()
            }
        else:
            data = {
                'info': 'NO DATA COMPANY'
            }    

        return json.dumps(data)

