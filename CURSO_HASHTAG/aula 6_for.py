for i in range (10):
    print(i)
    print('Estou aprendendo Python')

lista_precos = [1500, 1000, 800, 2000]
imposto_total = 0
for preco in lista_precos:
    if preco > 1000:
        taxa = 0.15
    else:
        taxa = 0.10
    imposto = preco * taxa
    imposto_total = imposto_total + imposto
    print(f'O preço é R${preco:,.2f} e a taxa de imposto é R${imposto:,.2f}')
print(f'O imposto total é R${imposto_total:,.2f}')

vendas_2023 = {'jan': 15000, 'fev': 10000, 'mar': 5000}
vendas_2024 = {'jan': 16000, 'fev': 11000, 'mar': 5100}
for mes in vendas_2024:
    valor_2023 = vendas_2023[mes]
    valor_2024 = vendas_2024[mes]
    crescimento = valor_2024 / valor_2023 - 1
    print(f'O crescimento de {mes} de 2023 para 2024 foi de {crescimento:.2%}')