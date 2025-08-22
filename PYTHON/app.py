import tkinter as tk  # Importa a biblioteca Tkinter e dá um apelido "tk"

# Cria a janela principal
janela1 = tk.Tk()

# Define o título da janela
janela1.title("Minha primeira janela")

# Define o tamanho da janela (largura x altura)
janela1.geometry("400x300")

# Cria um campo de entrada de texto (input)
# - "janela" é a janela onde o campo vai aparecer
# - "width=40" define a largura do campo em número de caracteres
produto = tk.Entry(janela1, width=40)

# Coloca (empacota) o campo de entrada na janela
# - "pady=20" adiciona um espaço vertical (margem) acima e abaixo do campo
produto.pack(pady=20)

# Mantém a janela aberta até o usuário fechar
janela1.mainloop()
