class Interruptor:
    def __init__(self, comodo:str):
        self.comodo = comodo
    
    def acender(self) -> None:
        print(f'Acendendo a Luz do comodo {self.comodo}')

    def apagar(self) -> None:
        print(f'Apagando a luz do comodo {self.comodo}')


class Pessoa:
    def acender_luz(self, interruptor:Interruptor):
        interruptor.acender()
    
    def apagar_luz(self, interruptor:Interruptor):
        interruptor.apagar()

    def dormir(self):
        print(f'fui de base')

galego = Pessoa()
sala = Interruptor('sala')
quarto = Interruptor('quarto')
galego.acender_luz(sala)
galego.apagar_luz(quarto)
galego.dormir()