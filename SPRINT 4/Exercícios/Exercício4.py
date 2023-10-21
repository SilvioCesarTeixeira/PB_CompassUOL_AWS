# A função calcular_valor_maximo deve receber dois parâmetros, chamados de 
# operadores e operandos. Em operadores, espera-se uma lista de caracteres 
# que representam as operações matemáticas suportadas (+, -, /, *, %), 
# as quais devem ser aplicadas à lista de operadores nas respectivas posições. 
# Após aplicar cada operação ao respectivo par de operandos, a função deverá
# retornar o maior valor dentre eles. Veja o exemplo:
# Entrada:
# operadores = ['+','-','*','/','+']
# operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

# Aplicar as operações aos pares de operandos:
# [ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 

# Obter o maior dos valores: 12

# Na resolução da atividade você deverá aplicar as seguintes funções: max, zip, map


# Função que retorna o valor máximo da sequencia de operações
def calcular_valor_maximo(operadores, operandos):
    
    # Dict contendo as operações como chave e as funções lambdas como valor
    operacoes_suportadas = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '%': lambda x, y: x % y
    }

    # Lista de tuplas contendo o operador e os operandos
    combinados = list(zip(operadores, operandos))

    # Lista de resultados, aplicando a função lambda (do dict) \
    # de acordo com o operador
    resultados = list(map(lambda a: operacoes_suportadas[a[0]](*a[1]), combinados))
    #retorno do valor máximo dos resultados
    return float(max((resultados)))


operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

maximo= calcular_valor_maximo(operadores, operandos)
print(maximo)
