# Tupla é um lista imutável

lista_vendas = [1000, 800, 500]
tupla_vendas = (1000, 800, 500)

print(lista_vendas[0])
print(tupla_vendas[0])

lista_vendas[0] = 1200 # para tupla você não consegue fazer isso, alterar o valor da lista

# Aplicação prática de tupla
# bonus 1: R$2,00 por venda feita
# bonus 2: 1% do valor de vendas

def calcular_bonus(lista_vendas):
  bonus1 = 2 * len(lista_vendas)
  bonus2 = 0.01 * sum(lista_vendas)
  return bonus1, bonus2

# Exemplo 1
vendas = [100, 250, 400, 1000]
resultado = calcular_bonus(vendas)
bonus1 = resultado[0]
bonus2 = resultado[1]
print(resultado)
print(bonus1)
print(bonus2)

# Exemplo 2 (unpacking da tupla)
vendas = [100, 250, 400, 1000]
b1, b2 = calcular_bonus(vendas)
print(bonus1)
print(bonus2)

# Exemplo 3
lista_telas = [(1090, 1080), (2140, 1080)]
for altura, largura in lista_telas:
  print(altura, altura)