class Mamifero:

    def __init__(self):
        self.localização = 'Brasil'

    def andar(self):
        print(f'O animal está andando pelo {self.localização}')

class Cachorro(Mamifero):
    
    def latir(self):
        print('o animal está latindo')
        self.andar()


dog = Cachorro()
dog.latir()
valor = dog.localização
print(valor)
