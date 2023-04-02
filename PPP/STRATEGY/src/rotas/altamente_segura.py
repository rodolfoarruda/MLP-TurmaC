from .interface import IRota


class RotaAltamenteSegura(IRota):
    
    def atualiza_nivel_seguranca(self):
        print("O status da rota é: altamente segura!")
