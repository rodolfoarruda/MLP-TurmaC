from typing import Type
from .rotas import IRota

class Rota:
      
    def __init__(self, rota: type[IRota]):
        self.rota = rota
        
    def acao(self):
        self.rota.atualiza_nivel_seguranca()        
    
        
    
    
    
