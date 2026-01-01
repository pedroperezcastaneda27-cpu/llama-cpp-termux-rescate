# credits_manager.py
# Módulo para manejar créditos de usuarios en la plataforma de generación de video

class CreditsManager:
    def __init__(self, initial_credits: int):
        self.credits = initial_credits
        self.history = []

    def consume(self, video_name: str, cost: int) -> bool:
        """
        Consume créditos por un video generado.
        Retorna True si se pudo generar, False si no hay créditos suficientes.
        """
        if self.credits >= cost:
            self.credits -= cost
            self.history.append({"video": video_name, "cost": cost})
            return True
        return False

    def get_balance(self) -> int:
        """Devuelve créditos restantes."""
        return self.credits

    def get_history(self) -> list:
        """Devuelve historial de videos generados."""
        return self.history


# Ejemplo de uso:
if __name__ == "__main__":
    # Usuario con 100 créditos (Plan Básico)
    manager = CreditsManager(initial_credits=100)

    # Intentar generar un video de 2m30s (16 créditos)
    if manager.consume("video_1.mp4", cost=16):
        print("Video generado. Créditos restantes:", manager.get_balance())
    else:
        print("No hay créditos suficientes.")

    # Mostrar historial
    print("Historial:", manager.get_history())
