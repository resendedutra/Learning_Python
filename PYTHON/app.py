# Importa a biblioteca Tkinter para criar interfaces gráficas
import tkinter as tk
from tkinter import messagebox  # Importa messagebox para mostrar mensagens ao usuário

# Cria a janela principal do aplicativo
root = tk.Tk()
root.title("Cadastro de Produtos")  # Define o título da janela
root.geometry("400x400")  # Define o tamanho da janela (largura x altura)

# Cria uma lista vazia para armazenar os produtos cadastrados
produtos = []

# Função chamada quando o usuário clica no botão "Adicionar Produto"
def adicionar_produto():
    produto = entrada_produto.get()  # Pega o texto digitado no campo de entrada
    if produto.strip() == "":  # Verifica se o campo está vazio ou só com espaços
        messagebox.showwarning("Atenção", "Digite um produto!")  # Mostra aviso
    else:
        produtos.append(produto)  # Adiciona o produto na lista
        atualizar_lista()  # Atualiza a lista exibida na tela
        entrada_produto.delete(0, tk.END)  # Limpa o campo de entrada após adicionar

# Função para atualizar a Listbox que mostra os produtos cadastrados
def atualizar_lista():
    lista_produtos.delete(0, tk.END)  # Limpa a Listbox
    for produto in produtos:  # Percorre cada produto da lista
        lista_produtos.insert(tk.END, produto)  # Adiciona o produto na Listbox

# Cria um rótulo (Label) para instruir o usuário
rotulo = tk.Label(root, text="Digite o nome do produto:")
rotulo.pack(pady=10)  # Adiciona o rótulo na janela com espaçamento vertical

# Cria um campo de entrada de texto (Entry) para o usuário digitar o produto
entrada_produto = tk.Entry(root, width=30)
entrada_produto.pack(pady=5)  # Adiciona o campo na janela com espaçamento

# Cria um botão que chama a função adicionar_produto quando clicado
botao_adicionar = tk.Button(root, text="Adicionar Produto", command=adicionar_produto)
botao_adicionar.pack(pady=10)  # Adiciona o botão na janela com espaçamento

# Cria uma Listbox para mostrar os produtos cadastrados
lista_produtos = tk.Listbox(root, width=50, height=15)
lista_produtos.pack(pady=10)  # Adiciona a Listbox na janela com espaçamento

# Mantém a janela aberta e aguardando interações do usuário
root.mainloop()
