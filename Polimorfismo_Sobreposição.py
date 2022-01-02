"""
Polimorfismo é permitir que classes derivadas de uma SUPERCLASSE ter métodos iguais(de mesmos parâmetros)
mas possuir comportamentos diferentes.
"""

from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()
b.fala('UM ASSUNTO')
c.fala('OUTRO ASSUNTO')