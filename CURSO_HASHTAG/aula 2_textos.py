faturamento = 1000
custo = 500
lucro = faturamento - custo

mensagem = 'O faturamento foi de R$'+ str(faturamento) + ' e o lucro foi de R$'+ str(lucro)
print(mensagem)

mensagem = f'O faturamento foi de R${faturamento} e o lucro foi de R${lucro}'
print(mensagem)


# Tornar todas as letras minúsculas, usar o '.lower()'
# Retirar espaços vazios antes, entre e depois das palavras, usar o '.strip()'
email = ' EMAIL_FALSO@gmail.com '
print(email.lower())
print(email.strip())
print(email.lower().strip())

# Pegar o tamanho do texto
print(len(email))
print(len(email.lower().strip()))

# Pegar posição de caracter
posicao = email.find('@')
print(posicao)

# Pegar pedaços de um texto
print(email[posicao:14])
print(email[posicao:]) #vai pegar até o final do texto
print(email[:posicao]) #vai pegar do início do texto até a posição desejada
print(email[:posicao+1]) #vai pegar do início do texto até a posição desejada

# Trocar pedaço de um texto
novo_emial = email.replace('gmail.com', 'yahoo.com.br')
print(novo_emial.lower().strip())

# Deixar a primeira letra maiúscula da primeira palava
nome = 'carlos dutra'
nome = nome.capitalize() 
print(nome)

# Deixar as primeiras letras maiúsculas de cada palavra
nome = nome.title()
print(nome)

# Deixar todas as letras maiúsculas de cada palavra
nome = nome.upper()
print(nome)

# Formatação númerica
faturamento = 1_000 # underline indica milhar
custo = 500
lucro = faturamento - custo
margem = lucro / faturamento

mensagem = f'O faturamento foi de R${faturamento:.2f}, o lucro foi de R${lucro:.2f} e a margem foi de {margem:.1%}'
print(mensagem)
mensagem = f'O faturamento foi de R${faturamento:,}, o lucro foi de R${lucro:,} e a margem foi de {margem:.1%}'
print(mensagem)
mensagem = f'O faturamento foi de R${faturamento:,.2f}, o lucro foi de R${lucro:,.2f} e a margem foi de {margem:.2%}'
print(mensagem)