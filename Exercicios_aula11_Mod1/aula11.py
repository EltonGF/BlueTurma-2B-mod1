# lista_contatos = [("Elton","999585477"),("Márcia","995155842"),("Aiane","987445896"),("Felipe","987452145"),("João","998548758")]
# print(lista_contatos)
# print(lista_contatos[0][0])

# print(type(lista_contatos))
# print()

# contatos = dict(lista_contatos)
# print(type(contatos))
# print(contatos)

# print()

# print(contatos.get("Felipe"))
# print(contatos.get("Márcia"))

# nome = input("Digite um nome: ")
# print(contatos.get(nome , "Nome não encontrado"))

#vingadores = {"Chris Evans":"Capitão América" , "Mark Ruffalo":"Hulk", "Tom Hiddleston":"Loki", "Chris Hemsworth":"Thor","Robert Downey Jr":"Homem de Ferro","Scarlett Johansson":"Viúva Negra"}
#print(vingadores.get("Chris Evans"))
#print(vingadores.get("Mark Ruffalo"))
#ving = input("Digite um nome para buscar seu personagem: ").title()
#print(vingadores.get(ving , "Personagem não encontrado"))

# while ving not in vingadores or ving ==0:
#     print("Nome não encontrado, tente novamente")
#     ving = input("Digite um nome para buscar seu personagem ou 0 para sair: ").title()
#     if ving == "0" :        
#         break
# print(vingadores.get(ving , "Nome não encontrado"))

vingadores = {"Chris Evans":"Capitão América" , "Mark Ruffalo":"Hulk", "Tom Hiddleston":"Loki", "Chris Hemsworth":"Thor","Robert Downey Jr":"Homem de Ferro","Scarlett Johansson":"Viúva Negra"}
print(vingadores)
vingadores["Mark Ruffalo"] = "Hulk Gladiador"
print(vingadores)
