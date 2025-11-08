import time

t = input("Digite o tempo desejado (segundos): ")

if t.isdigit():       # verificando se t é um número
  t = int(t)
else:
  print("Entrada inválida!!!")
  quit()

# convertedo segundos em minutos e segundos
# função divimod vai retornar o quociente e o resto da divisão de t/60
# o quociente e o resto da divisão serão armazenados nas variáveis minutos e segundos
while t != 0:
  minutos, segundos = divmod(t, 60)
  temporizador = "{:02d}:{:02d}".format(minutos, segundos)
  print(temporizador, end="\r")   # end="\r" faz vai sobreescrever o printo do tempo na mesma linha de impressão
  time.sleep(1)
  t = t - 1

print("Tempo finalizado!!!")