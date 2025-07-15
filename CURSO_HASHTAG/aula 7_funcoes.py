lista_precos = [1500, 1000, 800, 2000]

# produtos de até 1000 pagam 10% de imposto
# produtos acima de 1000 pagam 15% de imposto

def calcular_imposto(lista_valores):
  imposto_total = 0
  for preco in lista_valores:
    if preco > 1000:
      taxa = 0.15
    else:
      taxa = 0.1
    imposto = preco * taxa
    imposto_total = imposto_total + imposto
  return imposto_total

calcular_imposto(lista_precos)
imposto_total_lista1 = calcular_imposto(lista_precos)
print(imposto_total_lista1)

lista2_precos = [500, 4000, 3200, 2600, 1000]
calcular_imposto(lista2_precos)
imposto_total_lista2 = calcular_imposto(lista2_precos)
print(imposto_total_lista2)

def se_inscreva_no_canal():
  print("Clica no botão abaixo do vídeo onde está escrito se inscreva")
  print("Dê um like no vídeo")

se_inscreva_no_canal()