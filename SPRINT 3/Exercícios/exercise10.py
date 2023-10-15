#Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados.
#Utilize a lista a seguir para testar sua função.
# ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def tira_duplicados (lista):
    lista_sem_duplicados = list(set(lista))
    return lista_sem_duplicados

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
nova_lista = tira_duplicados (lista)
print (nova_lista)
