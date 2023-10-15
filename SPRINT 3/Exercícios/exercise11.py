# Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt
# e imprime o seu conteúdo.
# Dica: leia a documentação da função open(...)

nome_arquivo = ('arquivo_texto.txt')

arquivo = open(nome_arquivo, 'r')
texto = arquivo.read()
arquivo.close()
print (texto, end='')