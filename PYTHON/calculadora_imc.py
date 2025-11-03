import tkinter as tk                        # Importa o módulo 'tkinter' com o apelido 'tk' — fornece as classes e funções para criar a interface gráfica.
from tkinter import *                       # Importa tudo do módulo 'tkinter' para o namespace atual (evita precisar do prefixo 'tk.' em alguns usos).
from tkinter import ttk                     # Importa o submódulo 'ttk' do tkinter, que traz widgets com estilo moderno (não usado explicitamente neste código, mas disponível).

janela = tk.Tk()                            # Cria a janela principal da aplicação; instancia a raiz Tkinter onde todos os widgets serão colocados.
janela.title("Calculadora de IMC")          # Define o título da janela que aparece na barra de título do sistema operacional.
janela.geometry("295x300")                  # Define o tamanho inicial da janela em pixels: largura=295 e altura=300.
janela.configure(bg="white")                # Define a cor de fundo da janela principal como branco.
janela.resizable(False, False)              # (Comentado) Impedir redimensionamento horizontal e vertical; atualmente não ativo.

# Cores
cor0 = "#ffffff"                            # Variável com a cor branca (usada como fundo em vários widgets).
cor1 = "#000000"                            # Variável com a cor preta (poderia ser usada para texto; não usada em todas as linhas).
cor2 = "#BEBEBE"                            # Variável com tom de cinza (poderia ser usada para bordas/elementos secundários).
cor3 = "#3E64A2"                            # Variável com um tom de azul, usada como cor principal (texto/elementos de destaque).

# Dividir a janela em dois frames (superior e inferior)
# Frame superior
frame_superior = tk.Frame(janela, width=295, height=50, bg=cor0, padx=0, pady=0, relief="flat")
                                            # Cria um Frame (container) filho da janela principal.
                                            # width/height definem tamanho sugerido; bg define fundo; relief="flat" remove borda aparente.
frame_superior.grid(row=0, column=0, padx=0, pady=15, sticky=NSEW)
                                            # Posiciona o frame_superior na grade (grid) na linha 0, coluna 0.
                                            # padx/pady adicionam espaçamento externo; sticky=NSEW faz o widget "grudar" nas direções Norte/Sul/Leste/Oeste se houver expansão.

# Frame inferior
frame_inferior = tk.Frame(janela, width=295, height=290, bg=cor0, padx=0, pady=0, relief="flat")
                                            # Cria outro Frame para a parte inferior da interface; semelhante ao superior, serve como área para widgets de entrada e botões.
frame_inferior.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)
                                            # Posiciona o frame_inferior na grade na linha 2, coluna 0.
                                            # Observação: linha 1 fica vaga — isso é aceitável mas pode afetar espaçamento; sticky faz o frame esticar se possível.

# Função calcular
def calcular():                             # Define a função 'calcular' que será chamada quando o usuário clicar no botão "Calcular".
  peso = float(entry_peso.get())            # Lê o texto do widget 'entry_peso', converte para float e atribui à variável 'peso'.
                                            # .get() retorna string; float(...) converte e lançará erro se a entrada não for numérica.
  altura = float(entry_altura.get())        # Lê o texto do widget 'entry_altura', converte para float e atribui à variável 'altura'.
  imc = peso / altura ** 2                  # Calcula o IMC pela fórmula peso / (altura²). '**' é exponenciação em Python.
  resultado = imc                           # Atribui o valor do IMC à variável 'resultado' (útil para formatação e exibição posterior).

  if imc < 18.5:                            # Checa a primeira faixa: IMC menor que 18.5.
    label_imc["text"] = "Seu IMC é: Abaixo do peso"
                                            # Se verdadeiro, atualiza o texto do Label 'label_imc' para indicar "Abaixo do peso".
  elif imc >= 18.5 and imc < 25:            # Checa segunda faixa: IMC entre 18.5 (inclusive) e menor que 25.
    label_imc["text"] = "Seu IMC é: Peso normal"
                                            # Atualiza o Label com "Peso normal" se a condição acima for satisfeita.
  elif imc >= 25 and imc <30:               # Checa terceira faixa: IMC entre 25 (inclusive) e menor que 30.
   label_imc["text"] = "Seu IMC é: Sobrepeso"
                                            # Atualiza o Label com "Sobrepeso" — observe a indentação de um espaço aqui (funciona, mas manter indentação consistente é recomendado).
  elif imc >= 30:                           # Checa última faixa: IMC maior ou igual a 30.
    label_imc["text"] = "Seu IMC é: Obesidade"
                                            # Atualiza o Label com "Obesidade" para IMC >= 30.

  print(f"{resultado:.2f}")                 # Exibe no console (terminal) o valor do resultado formatado com 2 casas decimais — útil para depuração.
  label_resultado["text"] = "{:.{}f}".format(resultado, 2)
                                            # Atualiza o Label 'label_resultado' com o valor numérico formatado com 2 casas decimais.
                                            # Usa format() para converter 'resultado' em string com 2 casas.

# Configurando frame superior
app_nome = Label(frame_superior, text="Calculadora de IMC", width=23, height=1, relief="flat", anchor="center", font=("Ivy 16 bold"), bg=cor0, fg=cor3)
                                            # Cria um Label dentro do frame_superior com o texto do título.
                                            # width/height controlam tamanho em caracteres/linhas; anchor="center" centraliza o texto.
                                            # font define família e tamanho; bg/fg definem cores de fundo e do texto.
app_nome.place(x=0, y=0)                    # Posiciona o Label 'app_nome' no frame usando coordenadas absolutas (x=0, y=0).
                                            # .place permite posicionamento preciso; aqui coloca o título no canto superior esquerdo do frame.

app_linha = Label(frame_superior, text="", width=295, height=1, relief="flat", anchor="center", font=("Ivy 1"), bg=cor3, fg=cor3)
                                            # Cria um Label usado como linha decorativa (vazio mas com fundo cor3) para separar visualmente as áreas.
app_linha.place(x=0, y=35)                  # Posiciona essa "linha" no frame_superior nas coordenadas x=0, y=35 — criando uma barra horizontal.

# Configurando frame inferior
label_peso = Label(frame_inferior, text="Insira seu peso", height=1, relief="flat", anchor="center", font=("Ivy 12 bold"), bg=cor0, fg=cor3)
                                            # Cria um Label no frame_inferior pedindo que o usuário insira o peso.
label_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
                                            # Posiciona o label_peso usando grid na linha 0, coluna 0, com espaçamento e comportamento de expansão.

entry_peso = Entry(frame_inferior, width=5, relief="solid", font=("Ivy 12 bold"), justify="center")
                                            # Cria um campo de entrada (Entry) para o usuário digitar o peso.
                                            # width define largura em caracteres, relief="solid" desenha borda, justify="center" centraliza o texto.
entry_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)
                                            # Posiciona o campo entry_peso na mesma linha do label_peso, coluna 1, usando grid.

label_altura = Label(frame_inferior, text="Insira sua altura", height=1, relief="flat", anchor="center", font=("Ivy 12 bold"), bg=cor0, fg=cor3)
                                            # Cria um Label pedindo que o usuário insira a altura.
label_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
                                            # Posiciona label_altura na linha 1, coluna 0 do grid do frame_inferior.

entry_altura = Entry(frame_inferior, width=5, relief="solid", font=("Ivy 12 bold"), justify="center")
                                            # Cria um campo de entrada para a altura, com as mesmas propriedades visuais de entry_peso.
entry_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)
                                            # Posiciona entry_altura na linha 1, coluna 1 correspondente ao label_altura.

label_resultado = Label(frame_inferior, text="", width=4, height=1, padx=2, pady=18, relief="flat", anchor="center", font=("Ivy 18 bold"), bg=cor3, fg=cor0)
                                            # Cria um Label reservado para mostrar o valor numérico do IMC.
                                            # Tem fundo cor3 (azul) e texto em cor0 (branco), maior fonte para destaque.
label_resultado.place(x=200, y=10)         # Posiciona esse label em coordenadas absolutas dentro do frame_inferior (x=200, y=10), funcionando como um "visor" de resultado.

label_imc = Label(frame_inferior, text="", width=30, height=1, padx=0, pady=0, relief="flat", anchor="center", font=("Ivy 12 bold"), bg=cor0, fg=cor3)
                                            # Cria um Label para exibir a descrição do resultado (ex.: "Peso normal", "Sobrepeso", etc.).
label_imc.place(x=0, y=100)                 # Posiciona esse label mais abaixo no frame_inferior em x=0, y=100 — abaixo dos campos de entrada.

button_calcular = Button(frame_inferior, command=calcular, text="Calcular", width=27, height=1, overrelief="solid" , relief="raised", anchor="center", font=("Ivy 12 bold"), bg=cor3, fg=cor0)
                                            # Cria um botão chamado 'Calcular' dentro do frame_inferior.
                                            # 'command=calcular' associa a função definida anteriormente para ser executada ao clicar.
                                            # overrelief e relief controlam o efeito de borda; bg/fg definem cores.
button_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=35)
                                            # Posiciona o botão usando grid na linha 4, coluna 0 e estende em 35 colunas (prática para ocupar espaço horizontal).
                                            # pady=60 dá espaço vertical para separar visualmente o botão dos elementos acima.

janela.mainloop()                           # Inicia o loop principal da interface gráfica; mantém a janela visível e responde a eventos (cliques/entradas).
                                            # Esse comando bloqueia a execução até que a janela seja fechada pelo usuário.
