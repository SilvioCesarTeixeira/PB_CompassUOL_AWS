# Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: 
# a lista recebida dividida em 3 partes iguais.

# Teste sua implementação com a lista abaixo
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# lista recebida
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Calcula o tamanho das 3 sublistas
tamanho = len(lista) // 3

# Divide a lista recebida em três sublistas de mesmo tamanho
lista1 = lista[:tamanho]
lista2 = lista[tamanho:2*tamanho]
lista3 = lista[2*tamanho:]

# Imprimir as três listas
print (lista1, lista2, lista3)
