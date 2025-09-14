nome = "CaRlOs"

print(nome.upper()) # deixa todas as letras maiúsculas
print(nome.lower()) # deixa todas as letras minúsculas
print(nome.title()) # deixa a primeira letra maiúscula e as outras letras minúsculas

palavra = "  Python  "
print(palavra + ".")
print(palavra.strip() + ".") # apaga todos os espaços em branco
print(palavra.lstrip() + ".") # apaga os espaços em branco do lado esquerdo
print(palavra.rstrip() + ".") # apaga os espaços em branco do lado direito

texto = "Python"
print("##" + texto + "##")
print(texto.center(10, "#"))
print(texto.center(10))
print("-".join(texto))