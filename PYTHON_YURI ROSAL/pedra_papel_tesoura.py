import random

score_usuario = 0
score_computador = 0

opcoes = ["r", "p", "t"]
  

while True:
  escolha_usuario = input("Escolha R (pedra) / P (papel) / T (tesoura) / Q (sair): ").lower()

  if escolha_usuario == "q":
    break

  escolha_computador = random.randint(0, 2)
  # 0 para R, 1 para P e 2 para T
  
  opcoes_computador = opcoes[escolha_computador]

  print("o usuário escolheu: " + escolha_usuario)
  print("O computador escolheu: " + opcoes_computador)

  
  if escolha_usuario == opcoes_computador:
    print("Empate!")
  elif escolha_usuario == "r" and opcoes_computador == "t":
    print("Você ganhou!")
    score_usuario = score_usuario + 1
  elif escolha_usuario == "p" and opcoes_computador == "r":
    print("Você ganhou!")
    score_usuario = score_usuario + 1
  elif escolha_usuario == "t" and opcoes_computador == "p":
    print("Você ganhou!")
    score_usuario = score_usuario + 1
  else:
    print("Computador ganhou!")
    score_computador = score_computador + 1

print("A pontuação do usuário é: ", score_usuario)
print("A pontuação do computador é: ", score_computador)

if score_computador < score_usuario:
  print("Vitória!!!")
elif score_computador == score_usuario:
  print("Empate!!!")
else:
  print("Derrota!!!")

print("Até logo!!!")