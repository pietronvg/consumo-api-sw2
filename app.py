from flask import Flask, jsonify
import os

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Pedro Ferreira"},
    {"id": 2, "nome": "Gustavo Paixão"},
    {"id": 3, "nome": "Manuela Tavante <3"},
]

@app.route("/usuarios", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de usuarios - Acesse/usuarios"})

@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "_main_":
   port = int(os.environ.get("PORT",5000))
   app.run(host="0.0.0.0",port=port)
