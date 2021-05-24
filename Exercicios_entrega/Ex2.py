cont = 0
frase = input("Olá. Digite uma frase qualquer: ").lower()
vogal = "aeiou"

for i in vogal : #Pesquisar como fazer contagem das vogais na frase.
    cont += frase.count(i)
    frase = frase.replace(i,"")
print(cont)
print(frase)



