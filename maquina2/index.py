from flask import Flask, jsonify, make_response
import json
import os

app = Flask(__name__)

# Ruta al archivo JSON (ajusta la ruta según donde lo guardes en la instancia EC2)
JSON_FILE = os.path.join(os.path.dirname(__file__), "instance_info.json")

# Cargar datos del archivo JSON al iniciar la aplicación
with open(JSON_FILE, 'r') as file:
    instance_data = json.load(file)

# Endpoint /check
@app.route('/check', methods=['GET'])
def check():
    return make_response(jsonify({"status": "OK"}), 200)

# Endpoint /info
@app.route('/info', methods=['GET'])
def info():
    return jsonify(instance_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)