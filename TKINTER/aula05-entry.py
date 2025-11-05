import tkinter as tk
from tkinter import *

# Criação da janela
janela = tk.Tk()
janela.title("Entry")
janela.geometry("400x300")
#janela.resizable(width=False, height=False)
janela.config(bg="#000000")

# Função obter dados da entry
def obter_dados():
  nome = entry_nome.get()
  idade = entry_idade.get()
  label_nome_resposta["text"] = nome
  label_idade_resposta["text"] = idade
  entry_nome.delete(0, END)             # limpa a entry (input) nome
  entry_idade.delete(0, END)            # limpa a entry (input) idade

# Criação de label, entry e button
label_nome = Label(janela, text="Nome: ", width=15, font="Arial 12 bold", fg="#ffffff", bg="#000000", anchor="w")
label_nome.grid(row=0, column=0, padx=5, pady=5)

entry_nome = Entry(janela, width=15, font="Arial 12")
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_idade = Label(janela, text="Idade: ", width=15, font="Arial 12 bold", fg="#ffffff", bg="#000000", anchor="w")
label_idade.grid(row=1, column=0, padx=5, pady=5)

entry_idade = Entry(janela, width=15, font="Arial 12", state="disabled")    # o state disable desativa a entry
entry_idade.grid(row=1, column=1, padx=5, pady=5)

label_nome_resposta = Label(janela, text="", width=15, font="Arial 12 bold", fg="#ffffff", bg="#000000", anchor="w")
label_nome_resposta.grid(row=0, column=2, padx=5, pady=5)

label_idade_resposta = Label(janela, text="", width=15, font="Arial 12 bold", fg="#ffffff", bg="#000000", anchor="w")
label_idade_resposta.grid(row=1, column=2, padx=5, pady=5)

botao = Button(janela, command=obter_dados, text="Obter dados", width=10, height=2, relief="raised", fg="#000000", bg="#FF0000")
botao.grid(row=2, column=0, padx=5, pady=5, sticky="w")



janela.mainloop()