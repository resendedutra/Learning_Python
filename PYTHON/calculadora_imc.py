import tkinter as tk
from tkinter import *
from tkinter import ttk

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("295x300")
janela.configure(bg="white")
#janela.resizable(False, False)

# Cores
cor0 = "#ffffff"
cor1 = "#000000"
cor2 = "#BEBEBE"
cor3 = "#3E64A2"

# Dividir a janela em dois frames (superior e inferior)

# Frame superior
frame_superior = tk.Frame(janela, width=295, height=50, bg=cor0, padx=0, pady=0, relief="flat")
frame_superior.grid(row=0, column=0, padx=0, pady=15, sticky=NSEW)

# Frame inferior
frame_inferior = tk.Frame(janela, width=295, height=290, bg=cor0, padx=0, pady=0, relief="flat")
frame_inferior.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)

# Função calcular
def calcular():
  peso = float(entry_peso.get())
  altura = float(entry_altura.get())
  imc = peso / altura ** 2
  resultado = imc

  if imc < 18.5:
    label_imc["text"] = "Seu IMC é: Abaixo do peso"
  elif imc >= 18.5 and imc < 25:
    label_imc["text"] = "Seu IMC é: Peso normal"
  elif imc >= 25 and imc <30:
   label_imc["text"] = "Seu IMC é: Sobrepeso"
  elif imc >= 30:
    label_imc["text"] = "Seu IMC é: Obesidade"

  print(f"{resultado:.2f}")
  label_resultado["text"] = "{:.{}f}".format(resultado, 2)

  

# Configurando frame superior
app_nome = Label(frame_superior, text="Calculadora de IMC", width=23, height=1, relief="flat", anchor="center", font=("Ivy 16 bold"), bg=cor0, fg=cor3)
app_nome.place(x=0, y=0)

app_linha = Label(frame_superior, text="", width=295, height=1, relief="flat", anchor="center", font=("Ivy 1"), bg=cor3, fg=cor3)
app_linha.place(x=0, y=35)

# Configurando frame inferior
label_peso = Label(frame_inferior, text="Insira seu peso", height=1, relief="flat", anchor="center", font=("Ivy 12 bold"), bg=cor0, fg=cor3)
label_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

entry_peso = Entry(frame_inferior, width=5, relief="solid", font=("Ivy 12 bold"), justify="center")
entry_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

label_altura = Label(frame_inferior, text="Insira sua altura", height=1, relief="flat", anchor="center", font=("Ivy 12 bold"), bg=cor0, fg=cor3)
label_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

entry_altura = Entry(frame_inferior, width=5, relief="solid", font=("Ivy 12 bold"), justify="center")
entry_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

label_resultado = Label(frame_inferior, text="", width=4, height=1, padx=2, pady=18, relief="flat", anchor="center", font=("Ivy 18 bold"), bg=cor3, fg=cor0)
label_resultado.place(x=200, y=10)

label_imc = Label(frame_inferior, text="", width=30, height=1, padx=0, pady=0, relief="flat", anchor="center", font=("Ivy 12 bold"), bg=cor0, fg=cor3)
label_imc.place(x=0, y=100)

button_calcular = Button(frame_inferior, command=calcular, text="Calcular", width=27, height=1, overrelief="solid" , relief="raised", anchor="center", font=("Ivy 12 bold"), bg=cor3, fg=cor0)
button_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=35)




janela.mainloop()