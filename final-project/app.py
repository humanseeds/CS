from flask import Flask, request, render_template, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import os

# configure app
app= Flask(__name__)
