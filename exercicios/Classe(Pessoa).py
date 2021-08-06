class Pessoa:
    def __init__(self, nome, idade, comendo = None, falando = False):
        self.nome = nome
        self.idade = idade 
        self.comendo = comendo
        self.falando = falando
    
    def comer(self, alimento):
        if self.comendo == True:
            print(f'{self.nome} já esta comendo')
            return

        if self.falando == True:
            print(f'{self.nome} não pode comer falando.')
            self.comendo = False
            return

        print(f'{self.nome} esta comendo {alimento}.')
        self.comendo = True
        
    def falar(self, assunto):
        if self.falando == True:
            print(f'{self.nome} já esta falando')
            return

        if self.comendo == True:
            print(f'{self.nome} não pode falando comendo.')
            self.comendo = False
            return

        print(f'{self.nome} esta falando sobre {assunto}.')
        self.falando = True
        
    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} esta falando.')
            return

        else:
            print(f'{self.nome} parou de falar.')
            self.falando = False

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} esta comendo.')
            return

        else:
            print(f'{self.nome} parou de comer.')
            self.comendo = False

