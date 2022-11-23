class Pessoa:
  #atributos
  id = None
  nome = None

  #Método construto
  def __init__(self,id,nome):
    self.id = id
    self.nome = nome

  #metodo para ajudar na execução
  def __str__(self):
    return(f"{self.nome} ({self.id})")
    