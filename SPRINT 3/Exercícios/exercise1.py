# Exercícios Parte 1
# Desenvolva um código Python que lê do teclado nome e a idade atual de uma pessoa. 
# Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

import datetime


nome = input ("Qual é o seu nome?").capitalize()
idade = int(input ("Qual é a sua idade?"))
ano100 = (datetime.date.today().year + (100 - idade))
print (nome, ano100)