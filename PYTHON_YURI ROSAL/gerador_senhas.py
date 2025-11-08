import random
import string

def gerador_senha(tamanho_senha = 8):
  opcoes_ascii = string.ascii_letters
  opcoes_numeros = string.digits
  opcoes_punct = string.punctuation
  opcoes = opcoes_ascii + opcoes_numeros + opcoes_punct

  for digit in range(0, tamanho_senha):
    