num1 = int(input("Digite o primeiro número a ser somado: "))
num2 = int(input("Digite o primeiro número a ser somado: "))
soma = num1+num2
while soma < 50 :
    print("A soma ainda não resultou em 50. Acresente mais um número: ")
    num3 = int(input("Digite outro número a ser somado: "))
    soma = soma + num3
print("A soma alcançou o número 50!!!")
