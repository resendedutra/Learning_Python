import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title("Place")
janela.geometry("600x300")
janela.resizable(width=False, height=False)
janela.config(bg="#ffffff")

label_1 = Label(janela, text="Nome: ", width=15, font=("Arial 14 bold"), bg="#ffffff")
label_1.place(x=10, y=10)

nome = Label(janela, text="Carlos Dutra", width=15, font=("Arial 14 bold"), bg="#ffffff")
nome.place(x=180, y=10)

label_2 = Label(janela, text="Idade: ", width=15, font=("Arial 14 bold"), bg="#ffffff")
label_2.place(x=10, y=40)

idade = Label(janela, text="51", width=15, font=("Arial 14 bold"), bg="#ffffff")
idade.place(x=180, y=40)

label_3 = Label(janela, text="País: ", width=15, font=("Arial 14 bold"), bg="#ffffff")
label_3.place(x=10, y=70)

pais = Label(janela, text="Brasil", width=15, font=("Arial 14 bold"), bg="#ffffff")
pais.place(x=180, y=70)



janela.mainloop()