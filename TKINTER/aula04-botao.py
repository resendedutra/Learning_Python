import tkinter as tk
from tkinter import *

janela = tk.Tk()
janela.title("Botão")
janela.geometry("600x300")
janela.resizable(width=False, height=False)
janela.config(bg="#999999")

global contador 

contador = 0

def executar():
  
  global contador
  
  texto_1 = "Número impar: "
  texto_2 = "Número par: "
  
  if (contador % 2) == 0:      # Quer dizer que se o resto da divisão for 0 o número é par
    resultado = texto_2 + str(contador)
    label_1["text"] = resultado
    
  else:
    resultado = texto_1 + str(contador)
    label_1["text"] = resultado
    

  contador +=1

botao = Button(janela, command=executar, text="Clique aqui!", width=10, height=2, relief="raised", fg="#000000", bg="#FF0000")
botao.grid(row=0, column=0, padx=5, pady=5)

label_1 = Label(janela, text="Texto a ser apresentado ao clicar no botão", width=50, height=2, relief="flat", fg="#000000", bg="#FF0000")
label_1.grid(row=0, column=1, pady=5)



janela.mainloop()