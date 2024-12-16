from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import os

# configure app
app= Flask(__name__)

# folder config for image uploads
UPLOAD_Folder = 'saved-uploads'
ALLOWED-EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}



# render the file upload
@app.route('/')
def index():
    return render_template('upload.html')



#
@app.route('/uplad'. methods=['POST'])
    def upload_image():



#
@app.route('/image/<filename>')
def show_image(filename):



