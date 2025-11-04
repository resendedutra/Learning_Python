import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title("Pack")
janela.geometry("1200x300")
janela.resizable(width=False, height=False)
janela.config(bg="#ffffff")

label_nome = Label(janela, text="Nome: ", width=15, font="Arial 14 bold", bg="#ffffff")
label_nome.pack(side="left")

nome = Label(janela, text="Carlos Dutra", width=15, font="Arial 14 bold", bg="#ffffff")
nome.pack(side="left")

label_idade = Label(janela, text="Idade: ", width=15, font="Arial 14 bold", bg="#ffffff")
label_idade.pack(side="left")

idade = Label(janela, text="51", width=15, font="Arial 14 bold", bg="#ffffff")
idade.pack(side="left")

label_pais = Label(janela, text="País: ", width=15, font="Arial 14 bold", bg="#ffffff")
label_pais.pack(side="left")

pais = Label(janela, text="Brasil", width=15, font="Arial 14 bold", bg="#ffffff")
pais.pack(side="left")



janela.mainloop()