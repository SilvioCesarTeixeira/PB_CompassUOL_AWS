import hashlib

while True:
    entrada = input("Digite uma sequência de caracteres (ou 'sair' para deixar a aplicação): ")
    if entrada == 'sair':
        break
    print (f'Hash: {hashlib.sha256(entrada.encode()).hexdigest()}')
