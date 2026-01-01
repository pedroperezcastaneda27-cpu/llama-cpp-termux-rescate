import json
import os

class CargadorDePlanes:
    def __init__(self, base_path="planes"):
        self.base_path = base_path

    def cargar(self, nombre_plan: str) -> dict:
        ruta = os.path.join(self.base_path, nombre_plan, "config.json")
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"No existe el plan: {nombre_plan}")
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
