# Calcule o valor mínimo, valor máximo, valor médio e 
# a mediana da lista gerada na célula abaixo:
# Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

# Use as variáveis abaixo para representar cada operação matemática:
# mediana
# media
# valor_minimo 
# valor_maximo 

# Importante: Esperamos que você utilize as funções abaixo em seu código:
# random
# max
# min
# sum

import random 
# amostra aleatoriamente 50 números do intervalo 0...500
lista = random.sample(range(500),50)

# calcula valor máximo
valor_maximo = max(lista)

# calcula valor mínimo
valor_minimo = min(lista)

#calcula a média
media = sum(lista)/len(lista)

# calcula a madiana
lista_ordenada = sorted(lista)
tamanho = len(lista_ordenada)
if tamanho % 2 == 0:
    mediana = (lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2
else:
    mediana = lista_ordenada[tamanho // 2]

# Imprime os resultados
print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')