# Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.
# Dica: leia a documentação do pacote json

import json

nome_arquivo = ('person.json')

arquivo = open(nome_arquivo, 'r')
dict_json = json.load(arquivo)
print (dict_json)