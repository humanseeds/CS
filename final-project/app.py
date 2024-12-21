from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import os
from helpers import helper

# configure app
app= Flask(__name__)

# folder config for image uploads
UPLOAD_FOLDER = 'saved-uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# check if the upload folder exsists
os.makedirs(UPLOAD_FOLDER, exists_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# determine if proper file type is used
def proper_file(filename):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))


# render the file upload
@app.route('/')
def index():
    return render_template('upload.html')



# handle image uploading
@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['file']
    if file and proper_file(file.filename):
       filename =secure_filename(file.filename)
       file.svce(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       return redirect(url_for('show_image', filename=filename))


# display the uploaded or the converted image
@app.route('/image/<filename>')
def show_image(filename):
    return render_template('results.html', filename=filename)

