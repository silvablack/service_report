from setuptools import setup

requirements = [
    'aniso8601',
    'click',
    'Flask',
    'itsdangerous',
    'Jinja2',
    'MarkupSafe',
    'pytz',
    'six',
    'Werkzeug'
]

setup(
    name="report-service",
    author="Paulo Silva",
    author_email="paulosilvadev3@gmail.com",
    description="API - Reports to data of complains and companies",
    version="1.0",
    install_requires=requirements,
    extras_require={
        'dev':[
            'pytest',
            'pytest-pep8',
            'pytest-cov',
            'pytest-flask',
            'pytest-cache'
        ]
    }
)