class Celular:
    
    def __init__(self, modelo:str):
        self.modelo = modelo
    
    def enviar_msg(self, mensagem:str):
        print(f'enviando mensagem: {mensagem}')
    
    def abrir_email(self):
        print('abrindo emails...')
    
    def abrir_ytb(self):
        print('abrindo youtube...')

android = Celular('samsung')
iphone = Celular('iphone')

class Pessoa():
    def __init__(self, celular: Celular):
        self.__celular = celular

    def pizza(self):
        print('buscando celular...')
        print('definindo o sabor...')
        self.__celular.enviar_msg('quero pizza de calabresa')
        print('aguardando a chegada da pizza')


    def estudar(self):
        print('sentando no PC...')
        self.__celular.abrir_ytb()
        print('anotando o conteúdo')


android = Celular('samsung')
iphone = Celular('iphone')

galego = Pessoa(android)
matheus = Pessoa(iphone)

galego.pizza()
print()
matheus.estudar()