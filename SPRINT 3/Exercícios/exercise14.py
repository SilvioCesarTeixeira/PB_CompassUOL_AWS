# Escreva uma função que recebe um número variável de parâmetros não nomeados e 
# um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.

# Teste sua função com os seguintes parâmetros:

# (1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

def imprime_valor(*args, **kwargs):
    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(value)    
        

imprime_valor(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
