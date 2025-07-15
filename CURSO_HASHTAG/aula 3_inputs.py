faturamento = float(input('Insira o valor do faturamento R$'))
custo = float(input('Insira o valor do custo R$ '))
lucro = faturamento - custo
mensagem = (f'O valor do faturamento é de R$ {faturamento:,.2f}, o valor do custo é de R$ {custo:,.2f} e o lucro é de R$ {lucro:,.2f}')
print(mensagem)

faturamento = input('Insira o valor do faturamento R$')
faturamento = faturamento.replace('R$', ' ').replace(',','.')
faturamento = float(faturamento)
custo = input('Insira o valor do custo R$ ')
custo = custo.replace('R$', ' ').replace(',','.')
custo = float(custo)
lucro = faturamento - custo
mensagem = (f'O valor do faturamento é de R$ {faturamento:,.2f}, o valor do custo é de R$ {custo:,.2f} e o lucro é de R$ {lucro:,.2f}')
print(mensagem)

# Neste caso o valor a ser exibido será uma concatenação de textos de vendas do dia 1 e vendas do dia 2
vendas_dia1 = input('Vendas dia 1: ')
vendas_dia2 = input('Vendas dia 2: ')
print(vendas_dia1 + vendas_dia2)