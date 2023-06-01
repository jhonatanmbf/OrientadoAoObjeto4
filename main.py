from classes.produto import Produto;
from classes.cd import Cd;
from classes.dvd import Dvd;
from classes.livro import Livro;

def PrintActionForClassChosen(anoFabricacao, preco, segmento, classeInst):
  classeEscolhida = classeInst(anoFabricacao, preco, segmento);
  print(f"Os atributos da classeEscolhida: Ano:{classeEscolhida.anoFabricacao}, preço:{classeEscolhida.preco}, segmento:{classeEscolhida.segmento}")
  classeEscolhida.preco -= classeEscolhida.desconto()
  print(f"O classeEscolhida aplicou um desconto agora seu preço é {classeEscolhida.preco}")
  classeEscolhida.preco += classeEscolhida.juros()
  print(f"O classeEscolhida aplicou um juros seu preço é {classeEscolhida.preco}")


def main():

  print("Escolha a classe que deseja instanciar:")
  print("1 - Produto")
  print("2 - Cd")
  print("3 - Dvd")
  print("4 - Livro")

  decision = int(input("Escolha o numero correspondente a classe que deseja: "))

  if(decision == 1):
    PrintActionForClassChosen('2022', 1000, 'alimenticio', Produto)
  elif(decision == 2):
    PrintActionForClassChosen('2023', 1000, 'musica', Cd)
  elif(decision == 3):
    PrintActionForClassChosen('2023', 1000, 'musica', Dvd)
  else:
    PrintActionForClassChosen('2022', 100, 'finanças', Livro)



if __name__ == "__main__":
  main();