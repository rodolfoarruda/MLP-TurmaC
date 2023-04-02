from typing import Type
from .rotas import IRota

class Rota:
    
    _instance = None

    def __new__(cls, destino):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
      
    def __init__(self, destino) -> None:
        self._rota = None
        self.destino = destino
        
    def set_nivel_seg(self, rota:Type[IRota]):
        self._rota  = rota
    
    def move(self):
        self._rota.atualiza_nivel_seguranca()
        print("O usuário está caminhado para o destino {} nas novas condicoes".format(self.destino))
        

   
 
    
