from classes.produto import Produto;

class Livro(Produto):
  def __init__(self, anoFabricacao, preco, segmento):
    super().__init__(anoFabricacao, preco, segmento)
  def desconto(self):
    return self.preco * (0.12);
  def juros(self):
    return self.preco * (0.06);