import os
from flask import Flask
app = Flask('report-service')

@app.route('/')
def gelReport():
    return 'Hello server!'


if __name__ == '__main__':
    app.run(debug=True, host=os.environ.get('URL_SERVICE_REPORT'), port=os.environ.get('PORT_SERVICE_REPORT'))
