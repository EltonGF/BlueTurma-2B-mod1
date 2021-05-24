num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
soma = num1 + num2
multip = num1 * num2
if num1 > num2:
    div = num1 // num2
else :
    div = num2 // num1
if num1 > num2 :
    maior = num1
    print("O número",num1,"é maior.")
elif num2 > num1 :
    maior = num2
    print("O número",num2,"é maior.")
else :
    print("Os números fornecidos são iguais.")
if  soma % 2 == 0 :
    print("O resultado da soma resultou em um número par.")
else:
    print("O resultado das soma resultou em um número ímpar.")

print("A multiplicação dos números é igual a",multip)
print("O quociente da divisão entre os números 7é:",div)
if multip > 40 :
    resultado = multip / div
    print(f"O valor obtido através da divisão do resultado da multiplicação e da divisão inteira é {resultado:.2f}")
else :
    print(f"O resultado da multiplicação foi {multip:.2f},ou seja, menor que 40")