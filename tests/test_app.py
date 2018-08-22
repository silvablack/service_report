import pytest

from flask import url_for

class TestReportService:
    """
    Class to Test APP
    """
    def test_index(self, client):
        res = client.get(url_for('index'))
        assert res.status_code == 200
        assert res.json == {
            'title': 'Report Service',
            'version': '1.0.0'
        }