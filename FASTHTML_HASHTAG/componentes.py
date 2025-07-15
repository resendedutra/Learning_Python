from fasthtml.common import Div, H1, P, Form, Input, Button, Ul, Li, A

def gerar_titulo(titulo, subtitulo):
  return Div(
    H1(titulo),
    P(subtitulo),
    P("By Carlos Dutra")
  )

def gerar_formulario():
  formulario = Form(
    Input(type="text", name="tarefa", placeholder="Digite sua tarefa"),
    Button("Enviar Tarefa"),
    method="post", # Método post, para enviar as informações
    action="/adicionar_tarefa", # Define qual rota/link do site as informações serão enviadas
  )
  return formulario

def gerar_lista_tarefas(lista_tarefas):
  itens_lista = [Li(tarefa, " - ", A("Excluir", href="/deletar/{i}")) for i, tarefa in enumerate(lista_tarefas)]
  lista = Ul(
    *itens_lista
  )
  return lista