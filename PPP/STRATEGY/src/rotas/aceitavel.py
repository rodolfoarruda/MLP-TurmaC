from .interface import IRota


class RotaAceitavel(IRota):
    
    def atualiza_nivel_seguranca(self):
        print("O status da rota é: aceitavel!")
        
