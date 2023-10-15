#Escreva um código Python para imprimir todos os números primos entre 1 até 100. 
#Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.
#Importante: Aplique a função range().

não_primos = [0,1]
for i in range(2, 101):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            não_primos.append(i)
            break

for num in range(101):
    if (num in não_primos) == False:
        print (num)