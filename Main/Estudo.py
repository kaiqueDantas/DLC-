class EstudoClassePython:

    valor = 'olá'

    '''função de construtor da instância, sempre que for estanciado uma classem, esses parâmetros servem para pegar o valor
    do metodo'''
    def __init__(self, nome='', idade =''):
        #Self serve para referênciar a instância da classe
        self.nome = nome
        self.idade = idade


    '''pegar o atributo da classe e retorna o valor'''
    def getValor(self):
        return self.valor

    '''Altera o valor do atributo da classe'''
    def setValor(self, valor):

        self.valor = valor

    def connection(self):
        print(self.server)


    def getName(self):

        pass

    def getMail(self):
        pass

    def getData(self):
        pass

    def close(self):
        pass


