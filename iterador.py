class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)

        self.__items[index] = valor


    def __delitem__(self, index):
        del self.__items[index]


    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration


    def str(self):
        return f'{self.__class__.__name__} ({self.__items})'


if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Isabele')
    lista.add('Maria')

    print(lista)
    lista[0] = 'Isa'
    lista[1] = 'Joana'


    print(lista)

    print(lista[0])
    print(lista[1])


    for i in lista:
        print(i)

