print("Escolha a opção para temperatura de conversão")
print("1 - Celsius")
print("2 - Fahrenheit")
print("3 - Kelvin")

temp_conversao = int(input("Escolha uma da opções acima: "))
print("Você escolheu a opção", temp_conversao)

print("Escolha a opção para temperatura convertida")
print("1 - Celsius")
print("2 - Fahrenheit")
print("3 - Kelvin")

temp_convertida = int(input("Escolha uma da opções acima: "))
print("Você escolheu a opção", temp_convertida)

temp = float(input("Entre com o valor da temperatura a ser convertida: "))

if temp_conversao == 1:
  if temp_convertida ==1:
    print(temp)
  elif temp_convertida ==2:
    print((temp * 9 / 5) + 32)
  elif temp_convertida == 3:
    print(temp + 273.15)

if temp_conversao == 2:
  if temp_convertida == 1:
    print((temp - 32) * 5/9)
  elif temp_convertida == 2:
    print(temp)
  elif temp_convertida == 3:
    print((temp - 32) * 5/9 + 273.15)

if temp_conversao == 3:
  if temp_convertida == 1:
    print(temp - 273.15)
  elif temp_convertida == 2:
    print((temp - 273.15) * 9/5 + 32)
  elif temp_convertida == 3:
    print(temp)