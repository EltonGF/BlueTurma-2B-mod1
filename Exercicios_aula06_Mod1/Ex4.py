def salario (salario_hora,hora_trab,extra):
    if extra <= 40 :
        salario = salario_hora * (extra + hora_trab)
    else :
        salario = salario_hora * ((extra*1.5) + hora_trab)
    return salario

sal_hora = float(input("Digite valor do salário/hora: R$ "))
horas_trab = int(input("Digite valor da quantidade de horas trabalhadas: "))
extra_trab = int(input("Digite valor da quantidade de horas extras trabalhadas: "))

print(salario(sal_hora, horas_trab, extra_trab))

