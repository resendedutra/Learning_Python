# O código abaixo é o fundamental para criar uma homepage

from fasthtml.common import *

# Criando o aplicativo
app = FastHTML()

# Definindo a rota para acessar a homepage
@app.get("/")

# Função para carregar a homepage
def homepage():
  return "<h1>Olá Mundo!</h1>"

# Colocar a página no ar
serve()