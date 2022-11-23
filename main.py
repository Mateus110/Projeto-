#importar o Pessoa.py no diretório
from model.Pessoa import Pessoa

#exemplo de uso
mateus = Pessoa(1, "mateus santos")
print(mateus)

#quero mostrar só o nome
print(mateus.nome)