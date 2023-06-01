from classes.produto import Produto;

class Cd(Produto):
  def __init__(self, anoFabricacao, preco, segmento):
    super().__init__(anoFabricacao, preco, segmento)
  def desconto(self):
    return self.preco * (0.14);
  def juros(self):
    return self.preco * (0.08);