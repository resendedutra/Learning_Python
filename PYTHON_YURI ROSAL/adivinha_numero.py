import random

print("Seja bem vindo ao Adivinha Número do Carlos!")
escolha_numero = input("Digite o número teto do desafio: ")

if escolha_numero.isdigit():    # isdigit() verifica se o que está na variável é um número
  numero_teto = int(escolha_numero)
else:
  print("Erro: o valor informado não é numérico. Favor execute novamente e informe um número!")
  quit()

random_numero = random.randint(0, numero_teto)    # Retorna um número inteiro aleatório no intervalo [a, b], incluindo ambos os pontos extremos.

numero_tentativas = 0

while True:
  resposta_usuario = input("Adivinhe o número: ")
  
  if resposta_usuario.isdigit():    # isdigit() verifica se o que está na variável é um número
    resposta_usuario = int(resposta_usuario)
  else:
    print("Erro: o valor informado não é numérico. Favor informe um número!")
    continue

  numero_tentativas = numero_tentativas + 1

  if resposta_usuario == random_numero:
    print("Acertou")
    print(f"O número de tentativas foi: {numero_tentativas}")
    break
  elif resposta_usuario > random_numero:
    print("Chutou alto, o número randômico é menor que isso...")
  else:
    print("Chutou baixo, o número randômico é maior que isso")