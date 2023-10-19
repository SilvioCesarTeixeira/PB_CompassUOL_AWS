# Utilizando high order functions, implemente o corpo da função conta_vogais.
# O parâmetro de entrada será uma string e o resultado deverá ser a contagem de
# vogais presentes em seu conteúdo.
# É obrigatório aplicar as seguintes funções:
# len filter lambda
# Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.


def conta_vogais(texto:str)-> int:
    # Definir as vogais para comparação
    vogais_minusculas = 'aeiou'
    # Filtrar as vogais da string de entrada (com minúsculas)
    vogais = filter(lambda letra: letra in vogais_minusculas, texto.lower())
    # Contar as vogais da string de entrada
    contagem = len(list(vogais))
    return contagem


if __name__ == '__main__':
    sequencia = str(input('Digite uma sequencia de caracteres: '))
    print(conta_vogais(sequencia))
