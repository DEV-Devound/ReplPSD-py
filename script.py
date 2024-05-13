from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
import photoshop.api as ps
import os

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/write', methods=['POST'])
def write():
    # Request first name, last name and psd file from React
    ## Example
    #first_name = request.form['first_name']
    #last_name = request.form['last_name']
    #psd_file = request.files['psd_file']
    #profile_image = request.files['profile_image']

    psd_file_path = os.path.abspath(secure_filename(psd_file.filename))
    #profile_image_path = os.path.abspath(secure_filename(profile_image.filename))

    psd_file.save(psd_file_path)
    #profile_image.save(profile_image_path)

    # Load the PSD file
    doc = ps.Application().open(psd_file_path)

    # Edit the text layers called first_name and last_name (replace their text to the ones from the request.form)
    for layer in doc.layers:
        if layer.kind == ps.LayerKind.TextLayer:
            if layer.name == 'first_name':
                layer.textItem.contents = first_name
            elif layer.name == 'last_name':
                layer.textItem.contents = last_name

    print("Input are: " + first_name + " " + last_name)

    # Make it import the profile image into the PSD file
    # Import the profile image as a new layer

    # Save the document as a new JPG file
    new_jpg_file = 'new_' + os.path.splitext(psd_file.filename)[0] + '.jpg'
    doc.saveAs(new_jpg_file, options=ps.JPEGSaveOptions(quality=12), asCopy=True)

    return 'File has been written with the name ' + new_jpg_file

if __name__ == '__main__':
    app.run(port=3000)
