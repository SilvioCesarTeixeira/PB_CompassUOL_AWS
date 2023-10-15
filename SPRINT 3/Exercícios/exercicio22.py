# Crie uma classe chamada Pessoa, com um atributo privado chamado nome 
# (declarado internamente na classe como __nome) e um atributo público de nome id.
# Adicione dois métodos à classe, sendo um para definir o valor de __nome e 
# outro para retornar o valor do respectivo atributo.
# Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, 
# nunca diretamente.  Você pode alcançar este comportamento através do recurso
# de properties do Python.

# Veja um exemplo de como seu atributo privado pode ser lido e escrito:
# pessoa = Pessoa(0) 
# pessoa.nome = 'Fulano De Tal'
# print(pessoa.nome)

class Pessoa:
    # Declarar atributos privado (__nome) e público (id)
    def __init__(self, id):
        self.__nome = None 
        self.id = id

    # Obter atributo privado por função get (também privada)
    def _get_nome(self):
        return self.__nome

    # Setar atributo privado por função set (também privada)
    def _set_nome(self, valor):
        self.__nome = valor

    # criar propriedade nome para acessar o atributo preivado
    nome = property(_get_nome, _set_nome)

# Instanciar classe Pessoa
pessoa = Pessoa(0)

# Setar e obter o atributo privado através da propriedade 'nome'
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)
