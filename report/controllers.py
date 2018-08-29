#!/usr/bin/env python
# -*- coding: utf-8 -*-

from report import models

class ReportController:
    """
    Class to Controller Report actions
    """
    
    def build_report(objs, model=models.SearchComplainsByCity):
        response = model.find_report(objs)
        return response