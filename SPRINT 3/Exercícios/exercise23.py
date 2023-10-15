# Crie uma classe  Calculo  que contenha um método que aceita 
# dois parâmetros, X e Y, e retorne a soma dos dois. 
# Nessa mesma classe, implemente um método de subtração, 
# que aceita dois parâmetros, X e Y, e retorne a subtração dos dois 
# (resultados negativos são permitidos).

# Utilize os valores abaixo para testar seu exercício:

# x = 4 
# y = 5
# imprima:
# Somando: 4+5 = 9
# Subtraindo: 4-5 = -1

# Classe Calculo para dois parâmetros
class Calculo:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def somar ( X, Y):
        return f'Somando: {X + Y}'

    def subtrair (X, Y):
        return f'Subtraindo: {X - Y}'

soma = Calculo.somar(4,5)
diferença = Calculo.subtrair(4,5)
print(soma)
print(diferença)

