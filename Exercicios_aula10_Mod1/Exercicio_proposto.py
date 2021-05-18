#senha_cad = "Blue123python"
senha_cad = 159753246
#senha = 0
senha = int(input("Digite sua senha: "))
while senha != senha_cad :
    print("Senha incorreta. Tente novamente.")
    senha = int(input("Digite sua senha: "))
    #print(senha)
    #input()
print ("Acesso garantido.")