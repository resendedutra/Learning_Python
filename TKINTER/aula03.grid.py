import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title("Grid")
janela.geometry("400x300")
janela.resizable(width=False, height=False)
janela.config(bg="#ffffff")

label_nome = Label(janela, text="Nome: ", width=15, font="Arial 10 bold", bg="#ffffff", anchor="w")
label_nome.grid(row=0, column=0)

nome = Label(janela, text="Carlos Dutra", width=15, font="Arial 10 bold", bg="#ffffff", anchor="e")
nome.grid(row=0, column=1)

label_idade = Label(janela, text="Idade: ", width=15, font="Arial 10 bold", bg="#ffffff", anchor="w")
label_idade.grid(row=1, column=0)

idade = Label(janela, text="51", width=15, font="Arial 10 bold", bg="#ffffff", anchor="e")
idade.grid(row=1, column=1)

label_pais = Label(janela, text="País: ", width=15, font="Arial 10 bold", bg="#ffffff", anchor="w")
label_pais.grid(row=2, column=0)

pais = Label(janela, text="Brasil", width=15, font="Arial 10 bold", bg="#ffffff", anchor="e")
pais.grid(row=2, column=1)



janela.mainloop()