from flask import Flask, request, render_template, redirect, url_for, send_file, flash
from werkzeug.utils import secure_filename
from PIL import Image
import os
from helpers import helper

# configure app
app= Flask(__name__)
app.secret_key = os.urandom(24)

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

        # get the uploaded image from the form
        uploaded_image = request.files.get('image')

        # check if file was uploaded and has a valid name
        if uploaded_image and proper_file(uploaded_image.filename):

            # create a secure filename
            filename = secure_filename(uploaded_image.filename)

            # save the uploaded image to uploads folder
            uploaded_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # redirect the the results page with the filename
            return redirect(url_for('show_results', filename=filename))

        # handle an error in image file type and redirect
        flash("Invalid file type")


        return redirect(request.url)


@app.route('/uploads/<filename>')
def uploaded_image(filename):
     return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))



# display the uploaded or the converted image
@app.route('/image/<filename>')
def show_results(filename):
    # get the path to the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # flash error if not filename
    if not os.path.exists(image_path):
        flash("no file uploaded!")
        return render_template('upload.html')

    # process the image to ASCII art
    #ascii_filter =convert_image_to_ascii(image_path)

    # render the results on the page
    return render_template('results.html', filename=filename)#, ascii_filter=ascii_filter)



# 
@app.route('/apply_filter/<filename>')
def filter_image(filename):
    # Path to the uploaded image
    original_image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Apply the filter
    ascii_art, updated_image_path = apply_filter(original_image_path, app.config['UPLOAD_FOLDER'])

    # Return ASCII art or serve the updated image as needed
    return f"<pre>{ascii_art}</pre>"
