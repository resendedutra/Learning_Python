nome = "Carlos"
idade = 51
profissao = "Engenheiro"
area = "Elétrica"
saldo = 45.435

pessoa = {"nome": "Carlos" , "idade": 51, "profissao": "Engenheiro", "area": "Elétrica"}

print("Olá, me chamo %s. Tenho %d anos de idade, trabalho como %s na área %s." %(nome, idade, profissao, area))
print("Olá, me chamo {}. Tenho {} anos de idade, trabalho como {} na área {}.".format(nome, idade, profissao, area))
print("Olá, me chamo {3}. Tenho {2} anos de idade, trabalho como {1} na área {0}.".format(area, profissao, idade, nome))
print("Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} na área {area}.".format(nome=nome, idade=idade, profissao=profissao, area=area))
print("Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} na área {area}.".format(**pessoa))
print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} na área {area}. Meu saldo é de {saldo:10.2f}")
print(f"Olá, me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} na área {area}. Meu saldo é de {saldo:.2f}")
