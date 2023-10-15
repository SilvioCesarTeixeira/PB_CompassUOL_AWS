with open('seuarquivo.txt', 'r') as arquivo:
    linhas = arquivo.read().splitlines()

numero_total_de_linhas = len(linhas)

for i, linha in enumerate(linhas):
    if i < numero_total_de_linhas - 1:
        print(linha)
    else:
        print(linha, end="")
