import os

from report import service

__author__ = "Paulo Silva"
__version__ = "1.0.0"
__email__ = "paulosilvadev3@gmail.com"

app = service(os.environ.get('API_ENV'))

if __name__ == '__main__':
    app.run(host=os.environ.get('URL_SERVICE_REPORT'), port=os.environ.get('PORT_SERVICE_REPORT'))