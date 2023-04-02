from src import *


# Exemplo de uso:

rota1 = Rota("A")
rota1.set_nivel_seg(RotaSegura())
rota1.move()


rota2 = Rota("B")
rota2.set_nivel_seg(RotaAltamenteSegura())
rota2.move()


print(id(rota1)) # endereço de memória do objeto generator1
print(id(rota2)) # endereço de memória do objeto generator2

#print("Iniciando percurso!")
#rota1 = Rota().set_nivel_seg(RotaSegura())
#rota1.move()


#if True:
#    print("O carro de polícia está fazendo ronda!")
#    rota1=Rota().set_nivel_seg(RotaAltamenteSegura())

#rota1.nivel_seg()
#rota1.mover()


#if True:
#    print("Ficou escuro!")
#    rota1=Rota(destino="Rua 2", rota = RotaSegura())

#rota1.nivel_seg()
#rota1.mover()
