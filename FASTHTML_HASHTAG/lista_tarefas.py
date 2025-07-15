from fasthtml.common import fast_app, serve, Titled, RedirectResponse
from componentes import gerar_titulo, gerar_formulario, gerar_lista_tarefas

# Criando o aplicativo 'app' e as rotas 'routes'
app, routes = fast_app()

# Criando uma lista de tarefas (vazia)
lista_tarefas = []

# Definindo as rotas do site
@routes("/")

def homepage():
  formulario = gerar_formulario()
  print(lista_tarefas)
  elemento_lista_tarefas = gerar_lista_tarefas(lista_tarefas)
  # Tiled é uma classe que retorna alguns parâmetros já estilizados
  return Titled("Lista de Tarefas", formulario, elemento_lista_tarefas) 

@routes("/adicionar_tarefa", methods=["post"])
def adicionar_tarefa(tarefa: str):
  if tarefa:
    lista_tarefas.append(tarefa)
  return RedirectResponse(url="/", status_code=303)

@routes("/deletar/{posicao}")
def deletar_tarefa(posicao: int):
  if len(lista_tarefas) > posicao:
    lista_tarefas.pop(posicao)
  return RedirectResponse(url="/", status_code=303)

serve()