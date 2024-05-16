from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS  # Importar CORS
from werkzeug.utils import secure_filename
from photoshop import Session
import os

app = Flask(__name__, static_url_path='')
CORS(app)  # Habilitar CORS para la aplicación Flask

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/write', methods=['POST'])
def write():
    data = request.form  # Use request.form to get form data
    first_name = data['first_name']
    last_name = data['last_name']

    with Session("C:/Users/Admin/Desktop/Proyecto_nuevo.psd", action="open") as ps:
        doc = ps.active_document
        desc = ps.ActionDescriptor
        
        for layer in doc.layers:
            if layer.kind == ps.LayerKind.TextLayer:
                if layer.name == 'first_name':
                    layer.textItem.contents = first_name
                elif layer.name == 'last_name':
                    layer.textItem.contents = last_name

        opts = ps.ExportOptionsSaveForWeb()
        script_directory = os.path.dirname(os.path.abspath(__file__))
        new_file_path = os.path.join(script_directory, 'new_file.png')
        active_document = ps.app.activeDocument
        active_document.exportDocument(new_file_path, ps.ExportType.SaveForWeb, opts)

        return jsonify({'message': 'Datos recibidos correctamente'})

if __name__ == '__main__':
    app.run(port=3002)