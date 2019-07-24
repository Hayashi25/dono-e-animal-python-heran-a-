class Pessoa:
    def __init__(self , nome , idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        print(self.nome)

    def get_idade(self):
        print(self.idade)

class Pet:
    def __init__(self, nome_pet  , nascimento):
        self.nome_pet = nome_pet
        self.nascimento = nascimento

    def get_nome_pet(self):
        print(self.nome_pet)

    def velhice(self):
        nasceu = 2019
        ano = self.nascimento
        idade = int(nasceu) - int(ano)
        print(idade)
# velhice = (float(Pet.nascimento) - 2019 )

pessoa1 = Pessoa( "jose" , "60")
pessoa2 = Pessoa("vitor", "13")

print('Esse é o nome do dono:')
pessoa1.get_nome()
print('Essa é a idade do dono:')
pessoa1.get_idade()

pet1 = Pet("Lais" , "2008")

print('Esse é o nome do pet:')
pet1.get_nome_pet()
print('Essa é a idade do pet:')
pet1.velhice()



