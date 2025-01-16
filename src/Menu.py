from questionary import Style, select
import os, time
from src.Game import Jogo

TClear = "clear" if os.name == 'posix' else "cls"

def menu():
  Text = '''
     [][][][][][]  [][][][][][] [][][][][][] [][][][][][] [][][] [][][][][][]
     [][][][][][]  [][][][][][] [][][][][][] [][][][][][] [][][] [][][][][][]
         [][]      [][]             [][]     [][]    [][] [][][] [][]        
         [][]      [][]             [][]     [][]    [][] [][][] [][]        
         [][]      [][][][]         [][]     [][][][]     [][][] [][][][][][]    
         [][]      [][][][]         [][]     [][][][]     [][][] [][][][][][]
         [][]      [][]             [][]     [][]    [][] [][][]         [][]
         [][]      [][]             [][]     [][]    [][] [][][]         [][]
         [][]      [][][][][][]     [][]     [][]    [][] [][][] [][][][][][]
         [][]      [][][][][][]     [][]     [][]    [][] [][][] [][][][][][]'''

  custom_style = Style([
      ("selected", "bold fg:#008000"),    # Aplica negrito e cor clara à opção selecionada
      ("pointer", "fg:#000000"),          # Faz a seta de seleção (pointer) ter uma cor mais sutil
      ("highlighted", "fg:#008000 bold"), # A opção destacada com o cursor em negrito e cor clara
      ("prompt", "#000000"),
      ("question", "#008000"),
      ("separator", "fg:#cc0000")
  ])
  Op = ['Iniciar', 'Holding', 'Sair']
  # Define as opções com bordas para simular "caixas"
  opcoes = [
      f"{" "*30}┌{'─'*3}{'─'*int(len(Op[0]))}{'─'*3 }┐\n {" "*32}│   {Op[0]}   │\n {" "*32}└{'─'*3}{'─'*int(len(Op[0]))}{'─'*3}┘",
      f"{" "*30}┌{'─'*3}{'─'*int(len(Op[1]))}{'─'*3 }┐\n {" "*32}│   {Op[1]}   │\n {" "*32}└{'─'*3}{'─'*int(len(Op[1]))}{'─'*3}┘",
      f"{" "*31}┌{'─'*3}{'─'*int(len(Op[2]))}{'─'*4 }┐\n {" "*33}│   {Op[2]}    │\n {" "*33}└{'─'*3}{'─'*int(len(Op[2]))}{'─'*4}┘"]

  opcao_selecionada = select(

      message=Text,
      choices=opcoes,
      style=custom_style,
  ).ask()

  game = Jogo()
  os.system(TClear)

  OP = opcoes.index(opcao_selecionada)

  if OP == 0:
    os.system(TClear)
    time.sleep(2)
    game.jogar()
  elif OP == 1:
    print("holding")
  elif OP == 2:
    os._exit()