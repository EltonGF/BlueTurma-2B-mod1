# pessoas = {"Leandra Leal":"24/05/1982", "Scarlett Johansson":"17/09/1985","Edson Arantes do Nascimento":"10/10/1940", "Camila Pitanga":"03/03/1980","Silvio Santos":"04/04/1930"}
# nome = input("Digite o nome para data de nascimento: ").title()
# print(pessoas[nome])

pessoas = {"Leandra Leal":"1982", "Scarlett Johansson":"1985","Edson Arantes do Nascimento":"1940", "Camila Pitanga":"1980","Silvio Santos":"1930"}
print("Bem vindo. Nos temos essas celebridades cadastradas:")
for item_percorrido in pessoas:
    print(item_percorrido)
nome = input("Digite o nome para data de nascimento: ").title()
print(pessoas.get(nome,f"Desculpe mas o nome {nome} não foi encontrado"))
idade = 2021 - int(pessoas[nome])
print("Idade nos dias atuais: ", idade)