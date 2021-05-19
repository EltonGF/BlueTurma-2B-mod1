def comparacao (x,y) :
    if x < y :
        print("O número",x,"é menor.")
    elif y < x :
        print("O número",y,"é menor.")
    else :
        print("São iguais")

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
comparacao(num1, num2)