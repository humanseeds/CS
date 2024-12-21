from flask import Flask, request, render_template, redirect, url_for, send_file, flash
from werkzeug.utils import secure_filename
from PIL import Image
import os
from helpers import helper

# configure app
app= Flask(__name__)

# folder config for image uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# check if the upload folder exsists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# determine if proper file type is used
def proper_file(filename):
    if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
        return True
    return False

# render the file upload
@app.route('/')
def index():
    return render_template('upload.html')



# handle image uploading
@app.route('/upload', methods=['POST'])
def upload_image():
    # if the user posts and image
    if request.method == 'POST':

        # get the uploaded image from the form
              

        # check if file was uploaded and has a valid name
        if file and file.filename:

            # create a secure filename
            filename = secure_filename(file.filename)

            # save the uuploaded image to uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # redirect the the results page with the filename
            return redirect(url_for('results', filename=filename))

        # handle an error in image file type and redirect
        flash("Invalid file type")
        return redirect(request.url)

    # handle GET request if user bookmarks page
    return render_template('upload.html')


# display the uploaded or the converted image
@app.route('/image/<filename>')
def show_results(image_name):
    return render_template('results.html', filename=filename)

