lista_vendas = [100, 50, 80, 150]
total_vendas = sum(lista_vendas)
qtd_vendas = len(lista_vendas)
print(lista_vendas)
print(lista_vendas[0]) # Mostra o item 0 da lista
print(lista_vendas[1]) # Mostra o item 1 da lista
print(lista_vendas[2]) # Mostra o item 2 da lista
print(lista_vendas[3]) # Mostra o item 3 da lista
print(len(lista_vendas)) # Mostra a quantidade de itens da lista
print(lista_vendas[-1]) # Mostra o último item da lista
print(total_vendas)

# Valores máximo, mínimo e média em uma lista
print(max(lista_vendas)) # Mostra o maior valor da lista
print(min(lista_vendas)) # Mostra o menor valor da lista
media_vendas = total_vendas / qtd_vendas # Calcula a média dos valores de venda
print(media_vendas)

# Métodos de lista: encontrar um elemento
print(50 in lista_vendas) # verifica se o item 50 existe na lista de vendas
posicao = lista_vendas.index(50) # coloca o índice do item 50 na variável posicao
print(posicao) # mostra a posição em que o valor 50 está na lista, ou seja, o índice do 1

# Métodos de lista: pegar um pedaço da lista
pedaco_lista = lista_vendas[posicao:] # pega o pedaço da lista começando no índice 1 até o final da lista
print(pedaco_lista)

# Métodos de lista: editar um item da lista
lista_precos = [5000, 7000, 3000, 1000, 10000]
print(lista_precos)
novo_preco = lista_precos[0] * 1.1
lista_precos[0] = novo_preco
print(novo_preco)
print(lista_precos)

# Métodos de lista: remover um item da lista
# remove
lista_precos.remove(7000)
print(lista_precos)
# pop
lista_precos.pop(2) # remove o item conforme índice da lista informado
print(lista_precos)
# o pop pode ser usado armazenando o item removido em uma variável
item_removido = lista_precos.pop(2)
print(lista_precos)
print('O intem removido foi:',item_removido)

# Adicionar item em uma lista
# Método append
lista_precos.append(7000) # o append adiciona um item sempre no final da lista
posicao = lista_precos.index(7000) # armazenando o índice do valor 7000 na variável posicao
item_adicionado = lista_precos[posicao]
print(lista_precos)
print('O item adicionado foi: ', item_adicionado)
# Método extend
lista_precos2 = [8000, 9000]
lista_precos.extend(lista_precos2)
print(lista_precos)
# Adicionar um item em uma posição específica em uma lista
lista_precos.insert(1, 500) # será adicionado o item no posição/índice 1 e o item é o valor 500
print(lista_precos)

# Contar quantidade de vezes que um item aparece na lista
print(lista_precos.count(500))

# Ordenar uma lista
lista_precos.sort() # por padrão assim fica em ordem crescente
print(lista_precos)
lista_precos.sort(reverse=True)
print(lista_precos)
