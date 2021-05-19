def somaImposto (taxa, custo):
    custo_total = custo * (taxaImposto/100+1)
    return custo_total

taxaImposto = float(input("Digite a porcentagem de imposto: "))
custo_fixo = float(input("Informe custo do produto: R$ "))
print("O custo total é de R$ ",somaImposto(taxaImposto, custo_fixo))

#Descobrir como deixar a saída da função formatada para duas casas decimais.