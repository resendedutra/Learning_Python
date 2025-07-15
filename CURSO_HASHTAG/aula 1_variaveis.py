faturamento = 1000
custo = 500
lucro = faturamento - custo

print('Faturamento = R$', faturamento)
print('Custo = R$', custo)
print('Lucro = R$', lucro)

faturamento = 1200
novas_vendas = 500
taxa = 0.15
despesa = custo * taxa
lucro = faturamento + novas_vendas - (custo + despesa)
margem_lucro = lucro / faturamento

print('Faturamento = R$', faturamento)
print('Margem de luco = ', margem_lucro)
print ('Vendas = R$', novas_vendas)
print('Custo = R$', custo)
print('Taxas = R$', despesa)
print('Lucro = R$', lucro)
if(margem_lucro > 0.80):
    print(True)
else:
    print(False)

# int = números inteiros
# float = números decimais
# strings = textos
# boolean = booleanos (True, False)

# adicição '+'
# subtração '-'
# multiplicação '*'
# divisão '/'
# floor division '//'
# resto da divisão 'mod'
# para decimal usar o ponto '.'