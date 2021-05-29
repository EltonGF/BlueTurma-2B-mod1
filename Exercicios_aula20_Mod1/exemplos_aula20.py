class Pessoa :
    def __init__(self, nome, idade, cpf, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__telefone = telefone

    
    # Get = Pegar, receber.
    def getNome(self):
        return self.__nome

    def getIdade (self):
        return self.__idade
    
    def getCpf (self):
        return self.__cpf

    def gefTelefone (self):
        return self.__telefone

    # Set = Alterar.
    def setNome(self, nome):
        self.__nome = nome

    def setIdade(self, idade):
        self.__idade = idade

    def setCpf(self, cpf):
        self.__cpf = cpf

    def setTelefone(self, telefone):
        self.__telefone = telefone

class Advogado(Pessoa):
    def __init__(self, nome, idade, cpf, telefone, oab):
        self.__oab = oab
        super().__init__(nome, idade, cpf, telefone)

class Medico(Pessoa):
    def __init__(self, nome, idade, cpf, telefone, crm):
        self.__crm = crm
        super().__init__(nome, idade, cpf, telefone)

advogado = Advogado("Harvey")



    # Set = Alterar.

