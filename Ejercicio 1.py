def introducir_lista():
    n = int(input('¿De cuantos números se compone la lista?'))
    print('Introduce los números enteros:')
    lista = list()
    for i in range(n):
        temp = int(input(f'{i + 1} - '))
        lista.append(temp)

    return lista

lista = introducir_lista()
print(f'Nuestra lista queda de la siguiente forma:\n{lista}')

def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        derecha = lista[i]
        for j in range(i - 1, -1, -1):
            izquierda = lista[j]
            if derecha < izquierda:
                lista[j + 1] = izquierda
                lista[j] = derecha
                derecha = lista[j]

    return lista

lista_ordenada = ordenar_lista(lista)

print(f'Que de manera ordenada quedaría de la siguiente forma:\n{lista_ordenada}')
print("hola")