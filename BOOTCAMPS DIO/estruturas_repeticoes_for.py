texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end="")
else:
  print() # adiciona quebra de linha
  print("Executa no final do laço")