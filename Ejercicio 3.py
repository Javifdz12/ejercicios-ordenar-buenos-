def deplazar_celdas(inicio, lista):
    maximo = lista[inicio]
    i = inicio
    condicion = True
    while condicion and maximo > lista[i + 1]:
        i += 1
        if i == len(lista) - 1:
            condicion = False

    lista[inicio : i] = lista[inicio + 1 : i + 1]
    lista[i] = maximo

    return lista

def ordenar_lista(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] <= lista[i+1]:
            i += 1 
        else:
            lista = deplazar_celdas(i, lista)
            i = 0

lista = []
n = int(input('Tamaño de nuestra serie numérica'))
for i in range(n):
    numero = int(input(f'{i + 1} - '))
    lista.append(numero)

print(f'\nLista introducida:\n\t{lista}')
lista_ordenada = ordenar_lista(lista)
print(f'\nLista ordenada:\n\t{lista}')
