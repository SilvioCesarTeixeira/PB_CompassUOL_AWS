# Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha.
# Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
# Você deverá aplicar as seguintes funções no exercício: map, filter, sorted e sum.
# Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
# a lista dos 5 maiores números pares em ordem decrescente;
# a soma destes valores.


# Função para ler os números inteiros de um arquivo
def ler_numeros_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        lista_numeros = list(map(int, map(str.strip, arquivo)))
    return lista_numeros

# Função que processa uma lista de acordo com uma função fornecida 
def processar(lista_nao_processada, funcao):
    lista_processada = funcao(lista_nao_processada)
    return lista_processada

# Função que filtra os números pares de uma lista
def filtrar_pares(lista):
    lista_pares = list(filter(lambda x: x % 2 == 0, lista))
    return lista_pares

# Função quwe retorna a lista fornecida em ordem decrescente
def decrescente(lista):
    decrescentes = sorted(lista, reverse=True)
    return decrescentes

   

if __name__ == '__main__':

    # Carregar os números do arquivo
    numeros = ler_numeros_do_arquivo('SPRINT 4/Exercícios/number.txt')

      # Filtrar os elementos marcados
    pares_filtrados = filtrar_pares(numeros)

    # Ordenar os números conforme a ordem escolhida
    pares_decrescentes = processar(pares_filtrados, decrescente)

    # Selecionar os 5 maiores números pares
    cinco_maiores = pares_decrescentes[:5] 

    # Calcular a soma dos 5 maiores números pares
    soma = sum(cinco_maiores)

    # Exibir a lista dos 5 maiores números pares e a soma destes
    print(cinco_maiores)
    print(soma)


