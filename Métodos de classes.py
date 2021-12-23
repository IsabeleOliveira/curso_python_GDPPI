from random import randint

class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def pegar_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gerar_id():
        rand = randint(10000, 19999)
        return rand




p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.pegar_ano_nascimento()
print(Pessoa.gerar_id())
