# pessoas = {"Leandra Leal":"24/05/1982", "Scarlett Johansson":"17/09/1985","Edson Arantes do Nascimento":"10/10/1940", "Camila Pitanga":"03/03/1980","Silvio Santos":"04/04/1930"}
# nome = input("Digite o nome para data de nascimento: ").title()
# print(pessoas[nome])

# pessoas = {"Leandra Leal":"1982", "Scarlett Johansson":"1985","Edson Arantes do Nascimento":"1940", "Camila Pitanga":"1980","Silvio Santos":"1930"}
# print("Bem vindo. Nós temos essas celebridades cadastradas:")
# for item_percorrido in pessoas:
#     print(item_percorrido)
#     nome = input("Digite o nome para data de nascimento: ").title()
#     print(pessoas.get(nome,f"Desculpe mas o nome {nome} não foi encontrado"))
#     if pessoas.get(nome) != item_percorrido :
#         print("Celebridade não cadastrada.")
#     else:
#         idade = 2021 - int(pessoas[nome])
#         print("Idade nos dias atuais: ", idade)

celebridades = {"Bruna Lombardi": "1983", 
                "Paula Toller": "1980", "Sandy":"1983", 
                "Will Smith":"1970"}

print("Bem vindo ao nosso cadastro de famosos: ")
for item_percorrido in celebridades: #sintaxe do for
    print(item_percorrido)

#print(celebridades.keys)# keys devolve só o prieiro elemento, ou seja, o índice
nome = input("digite o nome do artista: ").title() #primeira letra de todas as palavras em maiúsculo

#print(celebridades["nome"]) #maneira mais fácil sem validação dicinario+ conchetes retorna o valor,sempre

#print(celebridades.get(nome, f"\nDesculpe, o nome {nome} não foi encontrado"))
#dicionario.get(chave)#retorna o valor da chave especificada entre parêntesesdatetime A combination of a date and a time. Attributes: ()
print(2021 - int(celebridades[nome]))


