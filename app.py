from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

usuarios = [
    {"id": 1, "nome": "Pedro Ferreira", "email": "pedro90@gmail.com"},
    {"id": 2, "nome": "Gustavo Paixão", "email": "paixao40@gmail.com"},
    {"id": 3, "nome": "Manuela Tavante <3","email": "manu67@gmail.com"}
]

@app.route("/")
def inicio():
    return "API funcionando!"

@app.route("/usuarios")
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    app.run(debug=True)
