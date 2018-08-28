#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json
from bson.dbref import DBRef
from bson.objectid import ObjectId
from mongoengine import Document, EmbeddedDocument, fields
from mongoengine.context_managers import switch_db
from report.db import ConnectCompany, ConnectComplains

class Companies(Document):
    name = fields.StringField(required=True)
    mail = fields.EmailField()
    cnpj = fields.StringField()

    meta = {'Companies': 'db_company'}

class Locale(EmbeddedDocument):
    city = fields.StringField(required=True)
    uf = fields.StringField(required=True)
    state = fields.StringField(required=True)

class Complains(Document):
    title = fields.StringField(required=True)
    description = fields.StringField(required=True)
    locale = fields.EmbeddedDocumentField(Locale)
    company_id = fields.StringField()
    date_created = fields.DateTimeField(required=True)
    date_updated = fields.DateTimeField()

    meta = {'Complains': 'default'}


class SearchComplainsByCity(object):

    def find_report(objs):
        ConnectComplains()
        ConnectCompany()

        with switch_db(Companies, 'db_company') as Ca:
            company = Ca.objects(id=ObjectId(objs['company']))

        with switch_db(Complains, 'default') as Co:
            complains = Co.objects.filter(company_id=objs['company'],locale__city=objs['city'], locale__uf=objs['uf']).all()
        
        for x in company:
            company_name = x.name

        data = {
            'company': company_name,
            'city': objs['city'],
            'uf': objs['uf'],
            'company_id': objs['company'],
            'total_complains': complains.count()
        }

        return json.dumps(data)

