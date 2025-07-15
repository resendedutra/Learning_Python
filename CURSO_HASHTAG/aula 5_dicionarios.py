# Exemplo 1
produtos = ['iphone', 'ipad', 'airpod']
precos = [7000, 5000, 2000]
dic_produtos = {'iphone': 7000, 'ipad': 5000, 'airpod': 2000}

# Pegar item em uma lista
produto = 'iphone'
posicao = produtos.index(produto)
preco = precos[posicao]
print(produto, preco)

# Pegar um item em um dicionário
print(dic_produtos['ipad'])
dic_vendas = {'dutra': [1000, 500, 1500], 'carlos': [500, 400, 500]}
print(dic_vendas['dutra'])

# Adicionar um item em um dicionário
dic_produtos['macbook'] = 10000
print(dic_produtos)

# Editar um item em um dicionário
dic_produtos['iphone'] = 8000
dic_produtos['airpod'] = dic_produtos['airpod'] * 1.1
print(dic_produtos['iphone'], dic_produtos['airpod'])

# Remover um item de um dicionário
# dic_produtos.pop('macbook')
item_removido = dic_produtos.pop('macbook')
print(dic_produtos)
print(item_removido)

# Verificar se existe um item no dicionário
print('iphone' in dic_produtos)
# ou
print('iphone' in dic_produtos.keys())
print(2200 in dic_produtos.values())

# Transformar um dicionário numa lista padrão
lista_produtos = list(dic_produtos.keys())
print(lista_produtos)
lista_precos = list(dic_produtos.values())
print(lista_precos)

# Contar quantos produtos existe no dicionário
qtde = len(dic_produtos)
print(qtde)
venda_total = sum(dic_produtos.values())
print(venda_total)

# Exercício
dic_produtos = {'iphone': 7000, 'ipad': 5000, 'airpod': 2000, 'macbook': 12000}
produto_buscado = input('Digite no nome do produto: ')
produto_buscado = produto_buscado.strip().lower()

if produto_buscado in dic_produtos:
    preco = dic_produtos[produto_buscado]
    print(f'O produto {produto_buscado} existe e seu valor é de R${preco}')
else:
    print('O produto buscado não exite!')