class UserManager:
    def __init__(self):
        self.usuarios = {}
        self.creditos = {}

    def inicializar_usuario(self, nombre):
        usuario = {"nombre": nombre}
        plan = {"name": "Básico", "video_cost": {"video": 1}}
        self.usuarios[nombre] = usuario
        self.creditos[nombre] = 10  # créditos iniciales
        return {"usuario": usuario, "plan": plan}

    def get_balance(self, nombre="Pedro"):
        return self.creditos.get(nombre, 0)

    def consume(self, nombre, video, costo=1):
        if self.creditos.get(nombre, 0) >= costo:
            self.creditos[nombre] -= costo
            return True
        return False

    def get_history(self, nombre="Pedro"):
        return f"Historial de {nombre}: {self.creditos.get(nombre, 0)} créditos restantes"
