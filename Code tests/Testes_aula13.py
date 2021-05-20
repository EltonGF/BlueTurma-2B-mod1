vingadores = {"Chris Evans": "Capitão América", "Mark Ruffalo": "Hulk", "Tom Hiddleston": "Loki",
"Chris Hemworth": "Thor", "Robert Downey Jr": "Homem de Ferro", "Scarlett Johansson": "Viúva Negra"}

print(vingadores)

vingadores ["Joaquin Phoenix"] = "Coringa"
vingadores ["Gal Gadot"] = "Mulher Maravilha"

print(vingadores)

# Deletando valores
del vingadores ["Gal Gadot"]

print(vingadores.pop("Joa Phoenix", "Ator não encontrado."))
print(vingadores.pop("Joaquin Phoenix", "Ator não encontrado."))
print(vingadores) 
vingadores.pop("Mark Ruffalo" , "Ator não encontrado")
print(vingadores)

vingadores.popitem()
print(vingadores)

animais = {"Cachorro":"Vira lata caramelo", "Cavalo":"Manga larga", "Gato":"Siamês", "Arara":"Canindé"}

# for item in animais:
#     vingadores[item] = animais[item]
#     print(vingadores)
#     input()
# print(vingadores)

vingadores.update(animais)
print(vingadores)