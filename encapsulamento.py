class Mamifero:

    def __init__(self, localizacao:str):
        self.localização = localizacao

    def andar(self):
        print(f'O animal está andando pelo {self.localização}')

    def _dormir(self):
        print('o animal está dormindo')

class Gato(Mamifero):

    def __init__(self, localizacao:str):
        super().__init__(localizacao)
    
    def miar(self):
        print('o animal está miando')
        self.andar()
        self._dormir()

cat = Gato('Argentina')
cat.miar()
