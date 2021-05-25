def conta_vogal(frase) :
    vogal = "aeiou"
    cont = 0
    for i in vogal :                
        cont += frase.count(i)
        frase = frase.replace(i,"")
    print("As vogais apareceram",cont,"vezes.")
    print("A frase sem as vogais ficou da seguinte forma:\n",frase)
frase_usuario = input("Olá. Digite uma frase qualquer: ").lower()
conta_vogal(frase_usuario)
