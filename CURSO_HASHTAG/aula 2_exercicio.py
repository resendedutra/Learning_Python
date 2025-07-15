# Exercício
# nome = 'joao paulo lira'
# email = 'emailfalsodolira@gmail.com'
# Qual o servidor do email?
# Qual o 1° nome do usuário?
# Criar mensagem personalizada dizendo o usuário '1° nome" tal foi cadastrado com sucesso no email tal

nome = 'joao paulo lira'
email = 'emailfalsodolira@gmail.com'

posicao_1 = email.find('@')
print(posicao_1)
print(email[posicao_1:])

posicao_2 = nome.find('p')
primeiro_nome = nome[:posicao_2-1].replace('joao', 'João').capitalize()
print(nome[:posicao_2-1])

mensagem = f'O usuário {primeiro_nome} foi cadastrado com sucesso no {email}!!!'
print(mensagem)