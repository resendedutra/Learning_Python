# Exemplo 1
faturamento = 2000
custo = 400
lucro = faturamento - custo
margem = lucro / faturamento

if(margem >= 0.5):
    print(f'A empresa teve lucro que foi de R${lucro:,.2f}')
else:
    print(f'A empresa não teve lucro')

# Exemplo 2
faturamento = 700
custo = 400
lucro = faturamento - custo
margem = lucro / faturamento

if(margem >= 0.5):
    print(f'A empresa teve lucro que foi de R${lucro:,.2f}')
else:
    print(f'A empresa não teve lucro')

# Exemplo 3
produtos = ['iphone', 'ipad', 'airpod']
novo_produto = input('Digite o nome do novo produto: ')
if (novo_produto in produtos):
    print('O produto já existe')
else:
    print(f'{novo_produto} foi cadastrado com sucesso')
    produtos.append(novo_produto)

print(produtos)

# Exemplo 4
vendas = 20000
if vendas >= 15000:
    bonus = 500
else:
    if vendas >= 5000 and vendas < 15000:
        bonus = 100
    else:
        if vendas < 5000:
            bonus = 0

print(f'Vendedor ganha bonus de R${bonus}')

vendas = 20000
if vendas >= 15000:
    bonus = 500
elif vendas >= 5000 and vendas < 15000:
    bonus = 100
else:
    bonus = 0

print(f'Vendedor ganha bonus de R${bonus}')


