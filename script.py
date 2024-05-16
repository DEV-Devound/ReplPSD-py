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
    data = request.get_json()  # Asegúrate de obtener el JSON de la solicitud
    print(data)  # Imprimir el contenido del JSON en la terminal

    first_name = data['first_name']
    last_name = data['last_name']
    psd_file = request.files['psd_file']

    if psd_file:
        psd_file_path = os.path.join('path_to_save', secure_filename(psd_file.filename))
        psd_file.save(psd_file_path)

        with Session(psd_file_path, action="open", auto_close=True) as ps:
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
            os.startfile(new_file_path)

            return jsonify({'message': 'Datos recibidos correctamente'})

    return jsonify({'message': 'No se recibió ningún archivo PSD'}), 400

if __name__ == '__main__':
    app.run(port=3002)