"""
Tipos de métodos:
    public, protected, private
    public - os atributos podem ser modificados dentro e fora da classe
    protect - os atributos podem ser acessados e modificados somente dentro da classe ou nas filhas da classe
    private - os atributos só estam disponíveis dentro da classe

_private/protect(public _)
__private(_NOMECLASSE__nomeatributo)
"""


class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def inserir_cliente(self, id, nome):
        if 'Clientes' not in self.dados:
            self.dados['Clientes'] = {id: nome}
        else:
            self.dados['Clientes'].update({id: nome})

    def listar_clientes(self):
        for id, nome in self.dados['Clientes'].items():
            print({id, nome})

    def apagar_clientes(self, id):
        del self.dados['Clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Isabele')
bd.inserir_cliente(2, 'Maria')
bd.inserir_cliente(3, 'Mary')
bd.apagar_clientes(3)
bd.listar_clientes()
print(bd.dados)