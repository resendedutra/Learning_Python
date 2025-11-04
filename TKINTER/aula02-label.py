import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title("Label")
janela.geometry("300x300")
janela.resizable(width=False, height=False)
janela.config(bg="#FFFFFF")

label_nome = Label(janela, text="Nome: ", width=14, bg="#c0c0c0", font=("Arial 14 bold"), fg="#FF0000")
label_nome.grid(row=0, column=0, pady=10)

label_idade = Label(janela, text="Idade: ", width=15, bg="#c0c0c0", font=("Arial 14"), fg="#0B851B")
label_idade.grid(row=1, column=0, pady=10)

label_pais = Label(janela, text="País: ", width=15, bg="#c0c0c0", font=("Arial 14"), fg="#0011FF")
label_pais.grid(row=2, column=0, pady=10)



janela.mainloop()