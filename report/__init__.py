#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from flask import Flask,request, abort, jsonify, Response
from config import app_config
from report.controllers import ReportController


def service(env_name):
    app = Flask('report-service') # instace flask

    app.config.from_object(app_config[env_name]) # settings app

    @app.route('/',methods=['GET'])
    def index():
        """
        route / to info service
        """
        info = {
            'title': 'Report Service',
            'version': '1.0.0'
        }
        return Response(json.dumps(info),status=200,mimetype="application/json; charset=utf-8")

    @app.route('/report',methods=['GET'])
    def report():
        """
            Route /report
        Returns data model of reponse to controller request
        Send :params city, uf, company
        Reiceve :objects city, uf, company_id, company_name, total_complains
        """
        objs = {
            'city': request.args.get('city', type=str),
            'uf': request.args.get('uf', type=str).upper(),
            'company': request.args.get('company', type=str),
        } ### GET PARAMS FROM REQUEST
        response = ReportController.build_report(objs)
        return Response(response,status=200,mimetype="application/json; charset=utf-8")
        

    return app
