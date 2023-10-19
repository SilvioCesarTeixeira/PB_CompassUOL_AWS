# A função calcula_saldo recebe uma lista de tuplas, correspondendo a um
# conjunto de lançamentos bancários. Cada lançamento é composto pelo seu
# valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 
# Abaixo apresentando uma possível entrada para a função.
# lancamentos = [
#   (200,'D'),
#   (300,'C'),
#   (100,'C') ]
# A partir dos lançamentos, a função deve calcular o valor final, 
# somando créditos e subtraindo débitos. Na lista anterior, por exemplo,
# teríamos como resultado final 200.
# Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, 
# as seguintes funções na resolução: reduce (módulo functools), map

from functools import reduce

lancamentos = [
   (200,'D'),
   (300,'C'),
   (100,'C')
 ]

def calcula_saldo(lancamentos) -> float:
    # Cria duas listas: uma com créditos e outra com débitos
    credito = list(map(lambda x: x[0], filter(lambda x: x[1] == 'C', lancamentos)))
    debito = list(map(lambda x: x[0], filter(lambda x: x[1] == 'D', lancamentos)))

    # Soma respectivamente todos os créditos e todos os débitos
    total_credito = reduce(lambda x, y: x + y, credito, 0)
    total_debito = reduce(lambda x, y: x + y, debito, 0)
    
    #Retorna a diferença entre créditos e débitos
    return float(total_credito - total_debito)

print(calcula_saldo(lancamentos))
