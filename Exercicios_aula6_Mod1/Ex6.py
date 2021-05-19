def nota (x):
    if x >= 9 :
        nota_conc = "A"
    elif x >= 8 and x < 9 :
        nota_conc = "B"
    elif x >= 7 and x < 8 :
        nota_conc = "B"
    elif x >= 7 and x < 8 :
        nota_conc = "C"
    elif x >= 6 and x < 7 :
        nota_conc = "D"
    elif x >= 4 and x < 6 :
        nota_conc = "E"
    else :
        nota_conc = "F"
    return nota_conc

valor_nota = float(input("Digite a nota obtida: "))
print("Sua nota conceito é: ",nota(valor_nota))