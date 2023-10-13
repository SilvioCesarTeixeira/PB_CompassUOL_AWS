# Desafio da SPRINT3


def validar_dados(linha):
    campos = []                 # Lista para armazenar linha
    campo_temporario = ''       # Variável temporária
    aspas_duplas = False        # Variável que indica se tem aspas duplas

    # Iterarando cada caractere da linha
    for char in linha:
        if char == ',' and not aspas_duplas:     # Adiciona se tem vírgula e sem aspas duplas
            campos.append(campo_temporario)
            campo_temporario = ''
        elif char == '"':         # se achar o caractere ", inverte o status de 'aspas_duplas'
            aspas_duplas = not aspas_duplas
        else:
            campo_temporario += char

    campos.append(campo_temporario)

    return campos


# Abrir CSV como leitura
with open('SPRINT 3/actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

# Lista vazia para armazenar dados
dados = []

# Em cada linha do arquivo
for linha in linhas:
    linha = linha.strip()  # Remover espaços em branco antes e depois do dado
    campos = validar_dados(linha)  # validar dados para dividir os campos
    dados.append(campos)  # Adicionar "lista de campos" à "lista de dados"


# Perguntas dessa tarefa:
# Apresente o ator/atriz com maior número de filmes e a respectiva quantidade.
# A quantidade de filmes encontra-se na coluna Number of Movies do arquivo.


mais_filmes = 0
id_linha_ator = None

for i, linha in enumerate(dados[1:], start=1):
    ator, qtd_filmes = linha[0], int(linha[2])

    if qtd_filmes > mais_filmes:
        mais_filmes = qtd_filmes
        id_linha_ator = i

# Ator/atrizes com o maior número de filmes e a quantidade correspondente
if id_linha_ator:
    resposta1 = f"O maior número de filmes é de {dados[id_linha_ator][0]} com {mais_filmes} filmes!!"
else:
    resposta1 = "Não existe ator ou atriz com mais filmes"

# Gravar arquivo etapa-1.txt
arq_resposta1 = open('SPRINT 3/etapa-1.txt', 'w')
arq_resposta1.write (resposta1)
arq_resposta1.close()



# Apresente a média de receita de bilheteria bruta dos principais filmes,
# considerando todos os atores. Estamos falando aqui da média da coluna Gross.


total_receita_bruta = 0
total_filmes = 0

for linha in dados[1:]:
    receita_bruta = float(linha[5])
    total_receita_bruta += receita_bruta
    total_filmes += 1

media_bruta = total_receita_bruta / total_filmes

# Exibir média
resposta2 = f"A média da receita bruta dos principais filmes é de ${media_bruta:.2f} milhões de dólares."

# Gravar arquivo etapa-2.txt
arq_resposta2 = open('SPRINT 3/etapa-2.txt', 'w')
arq_resposta2.write (resposta2)
arq_resposta2.close()



# Apresente o ator/atriz com a maior média de receita de bilheteria bruta por filme do
# conjunto de dados. Considere a coluna Avarage per Movie para fins de cálculo.

media_por_ator = {}

for linha in dados[1:]:
    ator, media_receita = linha[0], float(linha[2])
   
    if ator in media_por_ator:
        media_por_ator[ator].append(media_receita)
    else:
        media_por_ator[ator] = [media_receita]

# Ator/atriz com a maior média
ator_maior_media = None
maior_media = 0

for ator, medias in media_por_ator.items():
    media_ator = sum(medias) / len(medias)
    if media_ator > maior_media:
        maior_media = media_ator
        ator_maior_media = ator

resposta3 = f"{ator_maior_media} tem a maior média de receita bruta: ${maior_media:.2f} milhões de dólares por filme."


# Gravar arquivo etapa-3.txt
arq_resposta3 = open('SPRINT 3/etapa-3.txt', 'w')
arq_resposta3.write (resposta3)
arq_resposta3.close()



# A coluna #1 Movie contém o filme de maior bilheteria em que o ator atuou.
# Realize a contagem de aparições destes filmes no dataset, listando-os ordenados pela
# quantidade de vezes em que estão presentes. Considere a ordem decrescente e, 
# em segundo nível, o nome do filme.
# Ao escrever no arquivo, considere o padrão de saída
# <sequencia> - O filme <nome filme> aparece <quantidade> vez(es) no dataset,
# adicionando um resultado a cada linha.


def ordenar_filmes(item):
    return (-item[1], item[0])

contagem_filmes = {}

for linha in dados[1:]:
    filme = linha[4]
    if filme in contagem_filmes:
        contagem_filmes[filme] += 1
    else:
        contagem_filmes[filme] = 1

filmes_ordenados = sorted(contagem_filmes.items(), key=ordenar_filmes)

arq_resposta4 = open('SPRINT 3/etapa-4.txt','w')
for i, (filme, contagem) in enumerate(filmes_ordenados, start=1):
    arq_resposta4.write(f"{i} - O filme {filme} aparece {contagem} vez(es) no dataset.\n")
arq_resposta4.close()



# Apresente a lista dos atores ordenada pela receita bruta de bilheteria de seus filmes
# (coluna Total Gross), em ordem decrescente.
# Ao escrever no arquivo, considere o padrão de saída
# <nome do ator> -  <receita total bruta>,
# adicionando um resultado a cada linha.


# Lista de tuplas (nome do ator, receita total bruta)
lista_ator_receita = []

for linha in dados[1:]:
    ator, receita_bruta = linha[0], float(linha[1])
    lista_ator_receita.append((ator, receita_bruta))


def obter_receita_bruta(item):
    return item[1]

atores_ordenados = sorted(lista_ator_receita, key=obter_receita_bruta, reverse=True)

arq_resposta5 = open('SPRINT 3/etapa-5.txt', 'w')
for ator, receita_bruta in atores_ordenados:
    arq_resposta5.write(f"{ator} - ${receita_bruta:.2f}\n")
arq_resposta5.close()
