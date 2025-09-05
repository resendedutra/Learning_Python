# is e is not são operadores de identidade
# operadores de identidade mostram se variáveis ocupam mesma região na memória

saldo, limite = 1000, 500
print(saldo is limite)

saldo, limite = 1000, 500
print(saldo is not limite)

saldo, limite = 500, 500
print(saldo is limite)