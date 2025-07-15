from fasthtml.common import *
from componentes import gerar_titulo

# Criando o aplicativo 'app' e as rotas 'routes'
app, routes = fast_app()

# Definindo as rotas do site
@routes("/")

def homepage():
  return gerar_titulo("Lista de Tarefas", "Organize e seja produtivo")

@routes("/blog")
def homepage():
  return gerar_titulo("Lista de Tarefas", "Aqui voce encontra dicas excelentes")

serve()