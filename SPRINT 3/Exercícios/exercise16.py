# Escreva uma função que recebe uma string de números separados por vírgula
# e retorne a soma de todos eles. Depois imprima a soma dos valores.
# A string deve ter valor  "1,3,4,6,10,76"


def soma (string):
    numeros = string.split(',')
    resultado = 0
    for num in numeros:
        num = int(num)
        resultado = resultado + num
    return resultado

string = "1,3,4,6,10,76"
soma_total = soma(string)   
print (soma_total)

