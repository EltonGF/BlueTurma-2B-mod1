class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.salario = 0
        self.horas_trabalhadas = 0

    def registra_hora_trabalhada(self,):
        self.horas_trabalhadas += 1

    def calcula_salario(self):
        self.salario = self.horas_trabalhadas * self.valor_hora_trabalhada

funcionario = Funcionario("Elton", "Analista de dados",40)
print(f"Salário atual: {funcionario.salario}")
print(f"Horas trabalhadas: {funcionario.horas_trabalhadas}")
print()
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
funcionario.registra_hora_trabalhada(horas_trabalhadas)
funcionario.calcula_salario()
print(f"Salário atual: {funcionario.salario}")
print(f"Horas trabalhadas: {funcionario.horas_trabalhadas}")
print()
# funcionario.salario = 200
# print(f"Salário atual: {funcionario.salario}")

print(funcionario.salario)

funcionario.registra_hora_trabalhada()
