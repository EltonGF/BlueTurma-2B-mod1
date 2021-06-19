def tipo(x):
    if x > 0 :
        print("P")
    elif x < 0 :
        print("N")
    else :
        print("0")
    
numero = int(input("Digite um número: "))
tipo(numero)
