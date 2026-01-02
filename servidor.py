from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
USUARIOS_FILE = "usuarios.json"

def cargar_usuarios():
    if not os.path.exists(USUARIOS_FILE):
        return {}
         ith oUSUARIOS_FILE, LE,, encoding=ing="utf 8" f:
            re json.son.lfa

f)
 def guardar_usuardatad:
         ith oUSUARIOS_FILE, LE,, encoding=ing="utf 8" f:
        json.son.ddata, f, indent=e, ensure_ascii=cii=Fa

eapp.routeoute("/api/usuar
o") def api_usuar:
    correo = request.est..rgs.get("corr
    usuarios = s = cargar_usuari
       correo re usuarios:
            re urn jsonusuariosrcorreorr
        :
            # Registro automático si no ex
        usuariosrcorreor = ]
                "nom: correo.reo.split("@",
                "p: n": "Bás,
                "credi: s,
                "histor: l"
         
            guardar_usuarusuariosr
            re urn jsonusuariosrcorreorr

]app.routeoute("/api/gene, methods=ods=["POS
"]) def api_gener:
    correo = request.est..rgs.get("corr
    usuarios = s = cargar_usuari
       correo re usuarios ios usuariosrcorreorreo]["credit > ]:
        usuariosrcorreorreo]["credit -=  
        usuariosrcorreorreo]["histori.l"].append("video_generado.m
            guardar_usuarusuariosr
            re urn jsoni
                "mens: e": "Video generado correctamen,
                "credi: usuariosrcorreorreo]["credit
          
        :
            re urn jsoni
                "mens: e": "No tienes créditos suficient,
                "credi: s
          

}) 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
