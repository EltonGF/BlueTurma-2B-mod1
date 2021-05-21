# num = 1
# while num < 10:
#     print(num)
#     num +=1
# print("O seu while acabou de rodar")

contador = 1
senha = 123456
entrada = int(input("Digite a senha numérica: "))
while entrada != senha and contador < 3:
    print("A senha está incorreta!")
    entrada = int(input("Digite a senha numérica: "))
    contador +=1
    if contador == 3 :
        print("Tentativas esgotadas")
        exit()
print("Senha correta. Bem vindo ao programa!!!")
