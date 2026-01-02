from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
USUARIOS_FILE = "usuarios.json"

def cargar_usuarios():
    if not os.path.exists(USUARIOS_FILE):
        return {}
    with open(USUARIOS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_usuarios(data):
    with open(USUARIOS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route("/api/usuario")
def api_usuario():
    correo = request.args.get("correo")
    usuarios = cargar_usuarios()
    if correo in usuarios:
        return jsonify(usuarios[correo])
    else:
        # Registro automático si no existe
        usuarios[correo] = {
            "nombre": correo.split("@")[0],
            "plan": "Básico",
            "creditos": 5,
            "historial": []
        }
        guardar_usuarios(usuarios)
        return jsonify(usuarios[correo])

@app.route("/api/generar", methods=["POST"])
def api_generar():
    correo = request.args.get("correo")
    usuarios = cargar_usuarios()
    if correo in usuarios and usuarios[correo]["creditos"] > 0:
        usuarios[correo]["creditos"] -= 1
        usuarios[correo]["historial"].append("video_generado.mp4")
        guardar_usuarios(usuarios)
        return jsonify({
            "mensaje": "Video generado correctamente.",
            "creditos": usuarios[correo]["creditos"]
        })
    else:
        return jsonify({
            "mensaje": "No tienes créditos suficientes.",
            "creditos": 0
        })

if __name__
