nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
idade = input("Informe sua idade: ")

print(nome, sobrenome, ", minha idade é",idade)
print(nome, sobrenome, end="...\n") # inserindo uma quebra de linha no final
print(nome, idade, sep="#") # o hasht será o separador entre Carlos e Dutra