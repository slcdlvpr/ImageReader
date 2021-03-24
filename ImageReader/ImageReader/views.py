"""
Routes and views for the flask application.
"""
import os
from datetime import datetime
from ImageReader import app
from werkzeug.datastructures import FileStorage
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory,send_file,json
from werkzeug.utils import secure_filename
from ImageReader.cognitiveservices.ocrImageService import ocrImageService
from ImageReader.cognitiveservices.ImageMetadataService import imageMetadataService
from ImageReader.model.coordinates import coordinates
from ImageReader.services.imageProcessService import imageProcessService
from base64 import b64encode


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Image analytics powered by Azure Cognitive Services'
    )

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploads/<path:filename>')
def download_file(filename):
    path = 'static/' +  app.config['UPLOAD_PATH']
    return send_from_directory(path, filename, as_attachment=False)



@app.route('/pullfile', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    
    
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        folder = 'ImageReader/static/' +  app.config['UPLOAD_PATH']
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        if not os.path.exists(folder):
            os.makedirs(folder)
           
        uploaded_file.save(os.path.join(folder, filename))
        full_filename = os.path.join(folder, filename)
        
        processService =  imageProcessService(app.config["subscription_key"],app.config["endpoint"])
        imageobj, imagetag, imgcordinates, textresult, imgDescription = processService.process_image(uploaded_file)
               
        img = request.host_url + folder + '/' + filename
        return render_template('analysis.html', results=textresult, imagetag = imagetag, imageobj=imageobj,imgcoordinates =  imgcordinates ,image = filename, imgDescription = imgDescription.captions[0].text.capitalize())
   

