class ConectorBancoDeDados:

    def __init__(self):
        self.connection = None
    
    def conectar_banco(self):
        self.connection = True

class RepositorioDeBanco:

    def __init__(self, conexao: ConectorBancoDeDados):
        self.__conexao = conexao
    
    def busca_dados(self) -> list:
        if self.__conexao.connection:
            return[1, 2 ,3 ,4 ,5]
        return None 

class RegraDeNegocio:

    def __init__(self, repositorio: RepositorioDeBanco):
        self.__repositorio = repositorio

    def calcular_resultados(self):
        dados = self.__repositorio.busca_dados()
        if not dados:
            print('Dados não encontrados. Verifique a conexão com o banco')
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f'o resultado é: {resposta}')

connect = ConectorBancoDeDados()
connect.conectar_banco()

repo = RepositorioDeBanco(connect)
regra = RegraDeNegocio(repo)

regra.calcular_resultados()
