print("Seja muito bem-vindo ao quiz do Carlos Dutra!")
resposta_usuario = input("Você quer começar (s/n): ")
print(resposta_usuario)
if resposta_usuario != "s":
  quit()

score = 0

print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubsoft \n (C) Activisio \n (D) EA \n")
resposta_1 = input("Resp.: ")

if resposta_1 == "A" or resposta_1 == "a":
  print("Correta \n ")
  score = score + 1
else:
  print("Incorreto \n ")

print("Quem é o protagonista do jogo Grand Theft Auto (GTA)? \n (A) Carlos John \n (B) Carl John \n (C) Carl Jaqueline \n (D) Carlos Johnson \n")
resposta_1 = input("Resp.: ")

if resposta_1 == "B" or resposta_1 == "b":
  print("Correta \n ")
  score = score + 1
else:
  print("Incorreto \n ")

print(f"O quiz chegou ao fim, sua pontação é {score}/2")