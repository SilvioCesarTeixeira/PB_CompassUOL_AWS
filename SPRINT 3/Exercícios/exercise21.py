# Implemente duas classes, Pato e Pardal, que herdam de uma superclasse chamada Passaro
# as habilidades de voar e emitir som.

# Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, 
# conforme o modelo a seguir.

# Imprima no console exatamente assim:

# Pato
# Voando...
# Pato emitindo som...
# Quack Quack
# Pardal
# Voando...
# Pardal emitindo som...
# Piu Piu

# Superclasse Passaro
class Passaro:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "emitindo som..."

    def voar(self):
        print('Voando...')

# Classe Pato
class Pato(Passaro):
    def emitir_som(self):
        return f"Pato {super().emitir_som()}\nQuack Quack"

# Classe Pardal
class Pardal(Passaro):
    def emitir_som(self):
        return f"Pardal {super().emitir_som()}\nPiu Piu"

# Instâncias das subclasses
a = Pato('Pato')
b = Pardal('Pardal')

# Chama os métodos das subclasses
print (a.nome)
a.voar()
print(a.emitir_som())
print (b.nome)
b.voar()
print(b.emitir_som())
