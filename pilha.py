class Pilha:
    def __init__(self):
        self.items = []
    
    def empilhar(self, item):
        self.items.append(item)
    
    def desempilhar(self):
        return self.items.pop()
    
    def ver_topo(self):
        return self.items[-1] if not self.esta_vazia() else None
    
    def esta_vazia(self):
        return len(self.items) == 0


# Criando uma nova pilha
pilha = Pilha()

# Adicionando itens à pilha
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)

# Verificando o topo da pilha
print(pilha.ver_topo()) # 30

# Removendo um item da pilha
pilha.desempilhar()

# Verificando o topo da pilha novamente
print(pilha.ver_topo()) # 20
