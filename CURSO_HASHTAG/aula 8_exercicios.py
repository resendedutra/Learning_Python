# bonus 1: R$2,00 por venda feita
# bonus 2: 1% do valor de venda

def calcular_bonus(lista_vendas):
  bonus1 = 2 * len(lista_vendas)
  bonus2 = 0.01 * sum(lista_vendas)
  return bonus1, bonus2

vendas = {
  "André": [1000, 500, 300, 5000, 1500, 80, 3000],
  "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
  "Alan": [800, 100],
  "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 100, 100, 100, 200]
}

# bonus de cada funcionário
# total de bonus 1 pago aos funcionários
# total de bonus 2 pago aos funcionários

total_bonus1 = 0
total_bonus2 = 0
for vendedor in vendas:
  bonus1, bonus2 = calcular_bonus(vendas[vendedor])
  print(f"Vendedor: {vendedor}, bonus1: {bonus1}, bonus2: {bonus2}")
  total_bonus1 = total_bonus1 + bonus1
  total_bonus2 = total_bonus2 + bonus2
  print("Total bonus1:", total_bonus1)
  print("Total bonus2:", total_bonus2)
  print("Total bonus geral:", total_bonus1 + total_bonus2)