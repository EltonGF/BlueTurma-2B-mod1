import random
cont = 0
senha = 15975346
senha1 = int(input("Digite a senha para iniciar o programa: "))
while senha != senha1 :
    print("Senha incorreta. Tente novamente.")
    senha1 = int(input("Digite a senha para iniciar o programa: "))
print("BEM VINDO!!!\nVocê acaba de entrar em um jogo de adivinhação...")
palpite = int(input("Vamos lá. Dê um palpite entre 0 e 20: "))
while palpite < 0 or palpite > 20 :
    print("Seu palpite não será aceito, pois está fora do limite. Tente novamente.")
    palpite = int(input("Dê um palpite entre 0 e 20: "))
num_aleatorio = random.randint(0,21)
while num_aleatorio != palpite :
    cont += 1
    if palpite > num_aleatorio :
        print("Seu palpite foi maior que o número a ser adivinhado.\nContinue tentando...")
        palpite = int(input("Dê um novo palpite entre 0 e 20: "))
    else :
        print("Seu palpite foi menor que o número a ser adivinhado.\nContinue tentando...")
        palpite = int(input("Dê um novo palpite entre 0 e 20: "))
print("Parabéns!!! Você adivinhou nosso número, grande vidente.")
print("Você precisou de",cont,"palpites até acertar. Até a próxima.")