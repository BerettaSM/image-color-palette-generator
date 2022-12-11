from flask import Blueprint, render_template, request, redirect, url_for, flash
from colorthief import ColorThief

ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}


def allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


views = Blueprint('views', __name__)


@views.route('/', methods=('GET',))
def home():
    return render_template('index.html')


@views.route('/', methods=('POST',))
def verify_image():
    if 'file_elem' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file_elem']
    if file.filename == '':
        flash('No selected file.')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        color_thief = ColorThief(file)
        number = int(request.form['number'])
        color_palette = color_thief.get_palette(color_count=number)
        color_palette = [(color, '#%02x%02x%02x'.upper() % color) for color in color_palette]
        return render_template('index.html', color_palette=color_palette)
    flash('Invalid file format. Expected: ' + '/'.join(list(ALLOWED_EXTENSIONS)))
    return redirect(request.url)
