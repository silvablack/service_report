#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, pytest

from context import report

@pytest.fixture()
def app():
    app = report.service(os.environ.get('API_ENV'))
    app.debug=True
    return app
