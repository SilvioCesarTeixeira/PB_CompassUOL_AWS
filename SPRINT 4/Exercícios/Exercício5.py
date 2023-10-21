# Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
# Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação,
# no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.
# Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em 
# formato textual contendo as seguintes informações:
# Nome do estudante
# Três maiores notas, em ordem decrescente
# Média das três maiores notas, com duas casas decimais de precisão
# O resultado do processamento deve ser escrito na saída padrão (print), 
# ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:
# Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>
# Exemplo:
# Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
# Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33
# Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções: round, map, sorted

import csv

grade_notas = {}
with open('SPRINT 4/Exercícios/estudantes.csv', 'r', newline='') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        nome, *notas = linha
        grade_notas[nome] = list(map(int, notas))

# Função para pegar as três maiores notas
maiores_notas = lambda notas: sorted(notas, reverse=True)[:3]

# Função para calcular a média das três maiores notas
media_3_notas = lambda notas: round(sum(maiores_notas(notas)) / 3, 2)

# Aplicação das funções aos dados
resultado = list(map(lambda item: (item[0], maiores_notas(item[1]), media_3_notas(item[1])), grade_notas.items()))

#Impressão do resultado
for nome, tres_maiores, media_tres_maiores in resultado:
    print(f"Nome: {nome} Notas: {tres_maiores} Média: {media_tres_maiores}")
