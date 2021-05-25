class pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def dados (self):
        print(self.nome)
        print(self.sobrenome)
        print(self.idade)

gente = pessoa("Elton", "Frois",38)
print(vars(gente))
gente.dados() 
    