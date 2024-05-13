from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename
from photoshop import Session
import os

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/write', methods=['POST'])
def write():
    # Request first_name, last_name, psd_file and profile_image from React application
    ## Example
    ###first_name = request.form['first_name']
    ###last_name = request.form['last_name']
    ###psd_file = request.files['psd_file']
    ###profile_image = request.files['profile_image']

    ###psd_file_path = os.path.abspath(secure_filename(psd_file.filename))
    ###profile_image_path = os.path.abspath(secure_filename(profile_image.filename))

    ###psd_file.save(psd_file_path)
    #profile_image.save(profile_image_path)

    # Load the PSD file
    with Session(psd_file_path, action="open", auto_close=True) as ps:
        doc = ps.active_document
        desc = ps.ActionDescriptor
        desc.putPath(ps.app.charIDToTypeID("null"), profile_image_path)
        event_id = ps.app.charIDToTypeID("Plc ")  # `Plc` needs one space in here.
        ps.app.executeAction(ps.app.charIDToTypeID("Plc "), desc)
        # Edit the text layers called first_name and last_name (replace their text to the ones from the request.form)
        for layer in doc.layers:
            if layer.kind == ps.LayerKind.TextLayer:
                if layer.name == 'first_name':
                    layer.textItem.contents = first_name
                elif layer.name == 'last_name':
                    layer.textItem.contents = last_name

       # Save the modified document as a new PSD file
        opts = ps.ExportOptionsSaveForWeb()
        # Get the path of the current script
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Specify the filename
        new_file_path = os.path.join(script_directory, 'new_file.png')
        active_document = ps.app.activeDocument
        active_document.exportDocument(new_file_path, ps.ExportType.SaveForWeb, opts)
        os.startfile(png_file)


if __name__ == '__main__':
    app.run(port=3000)

