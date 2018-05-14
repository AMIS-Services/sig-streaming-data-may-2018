from flask import Flask, request
from app.traffic.controllers import traffic

# the all-important app variable:
application = app = Flask(__name__, static_url_path='/static')

# API Version
api_version = '1.1'

app.register_blueprint(traffic, url_prefix='/{}/traffic'.format(api_version))
