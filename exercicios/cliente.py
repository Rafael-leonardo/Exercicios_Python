class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero, cidade, estado ):
        self.enderecos.append(Endereco(rua, numero, cidade, estado))

    def list_enderecos(self):
        for endereco in self.enderecos:
            print(self.nome)
            print(endereco.rua, ',', endereco.numero, ',', endereco.cidade, ',', endereco.estado)

class Endereco:
    def __init__(self, rua, numero, cidade, estado):
        self.cidade = cidade
        self.estado = estado
        self.rua = rua
        self.numero = numero