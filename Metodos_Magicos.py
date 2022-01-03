
class A:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        resultado = 1

        for i in args:
            resultado *= i

        return resultado


a = A()
var = a(1, 2, 3, 4, 5, 6)
print(var)
