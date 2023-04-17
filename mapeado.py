import functools
def sumar1 (x):
    return x+10
numeros = [10, 15, 21, 33, 42, 55]
resultado = list(map(sumar1, numeros))
print(resultado)
