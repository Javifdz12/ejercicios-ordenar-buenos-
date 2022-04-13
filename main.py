from clases.Ejercicio1 import introducir_lista,ordenar_lista
from clases.Ejercicio2 import ordenar,dict1,dict2
from clases.Ejercicio3 import ordenar_lista

if __name__ == '__main__':
    lista = introducir_lista()
    print(f'Nuestra lista queda de la siguiente forma:\n{lista}')
    lista_ordenada = ordenar_lista(lista)
    print(f'Que de manera ordenada quedaría de la siguiente forma:\n{lista_ordenada}')

    print(ordenar(dict2))
    print(ordenar(dict1))

    lista = []
    n = int(input('Tamaño de nuestra serie numérica'))
    for i in range(n):
        numero = int(input(f'{i + 1} - '))
        lista.append(numero)

    print(f'\nLista introducida:\n\t{lista}')
    lista_ordenada = ordenar_lista(lista)
    print(f'\nLista ordenada:\n\t{lista}')