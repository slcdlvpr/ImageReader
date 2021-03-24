"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', ".jpeg"]
app.config['UPLOAD_PATH'] = 'uploads'
app.config['mediafolder'] = '/uploads'
app.config["subscription_key"] = "{Your Key}"
app.config["endpoint"] = "{Your Endpoint}"

import ImageReader.views
