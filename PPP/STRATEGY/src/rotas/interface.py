from abc import ABC , abstractclassmethod


class IRota(ABC):
    
    @abstractclassmethod
    def atualiza_nivel_seguranca(self) -> None:
        raise NotImplementedError
    
    
    
