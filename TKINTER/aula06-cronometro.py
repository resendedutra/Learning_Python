import tkinter
from tkinter import *

# Definições das cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azul

# Criação da janela
janela = Tk()
janela.title("Cronômetro")
janela.geometry("380x200")
janela.resizable(width=False, height=False)
janela.config(bg=cor1)

# Criaçao de variáveis globais
global tempo
global rodar
global contador

tempo = "00:00:00"
rodar = False
contador = -5

# Criação da função iniciar
def iniciar():
  global tempo
  global contador
  
  if rodar:     
    if contador <= -1:         # antes do cronômetro começar
      inicio = "Começando em " + str(contador)
      label_tempo["text"] = inicio
    else:                      # rodando o cronômetro
      temporaria = str(tempo)
      hms = map(int, temporaria.split(":"))
      h = int(h)
      m = int(m)
      s = int(contador)
    
    label_tempo.after(1000, iniciar)
    contador +=1

# Criação da função começar
def comecar():
  global rodar
  rodar = True
  iniciar()

# Criação de label
label_app = Label(janela, text="Cronômetro", font="Arial 12 bold", bg=cor1, fg=cor2)
label_app.place(y=20, relx=0.5, anchor="center")        # colocando o texto na posição 5 para y e centralizado para x

label_tempo = Label(janela, text=tempo, font="Arial 30 bold", bg=cor1, fg=cor6)
label_tempo.place(y=80, relx=0.5, anchor="center")    # colocando o tempo centralizado na janela

# Criação de button
botao_iniciar = Button(janela, command=comecar, text="Iniciar", font="Arial 12 bold", width=10, height=1, bg=cor1, fg=cor2, relief="raised", overrelief="ridge")
botao_iniciar.place(x=20, y=150)

botao_pausar = Button(janela, text="Pausar", font="Arial 12 bold", width=10, height=1, bg=cor1, fg=cor2, relief="raised", overrelief="ridge")
botao_pausar.place(x=135, y=150)

botao_reiniciar = Button(janela, text="Reiniciar", font="Arial 12 bold", width=10, height=1, bg=cor1, fg=cor2, relief="raised", overrelief="ridge")
botao_reiniciar.place(x=250, y=150)



janela.mainloop()