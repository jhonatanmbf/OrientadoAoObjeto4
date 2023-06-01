class Produto():
  def __init__(self, anoFabricacao, preco, segmento):
    self.anoFabricacao = anoFabricacao;
    self.preco = preco;
    self.segmento = segmento;
  def desconto(self):
    return self.preco * (0.10);
  def juros(self):
    return self.preco * (0.05);