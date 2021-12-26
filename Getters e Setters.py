# SETTER = CONFIGURANDO UM VALOR (=), PRECISA TER UM GETTER PRIMEIRO
# GETTER = RETORNA O VALOR CONFIGURADO NO SETTER E PDE TER ELE SEM SETTER (.)

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return 'Oliveira'



p1 = Pessoa('Isabele')
print(p1.nome)
print(p1.sobrenome)

"""


class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    #Getter
    @property
    def preco(self):
        return self._preco


    #setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = valor.replace('R$', '')

        self.preco = valor
"""
