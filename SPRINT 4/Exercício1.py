# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha.
# Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
# Você deverá aplicar as seguintes funções no exercício: map, filter, sorted e sum.
# Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
# a lista dos 5 maiores números pares em ordem decrescente;
# a soma destes valores.


# Função para ler os números inteiros de um arquivo
def ler_numeros_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        numeros = [int(linha.strip()) for linha in arquivo]
    return numeros

# Carregue os números do arquivo
numeros = ler_numeros_do_arquivo('SPRINT 4/number.txt')

# Filtrar os números pares
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

# Ordenar os números pares em ordem decrescente
numeros_pares_ordenados = sorted(numeros_pares, reverse=True)

# Selecionar os 5 maiores números pares
cinco_maiores_pares = numeros_pares_ordenados[:5]

# Calcular a soma dos 5 maiores números pares
soma_cinco_maiores = sum(cinco_maiores_pares)

# Exibir a lista dos 5 maiores números pares e a soma
print("Lista dos 5 maiores números pares (em ordem decrescente):", cinco_maiores_pares)
print("Soma dos 5 maiores números pares:", soma_cinco_maiores)

