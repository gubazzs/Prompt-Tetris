import os, time
from src.Game import Jogo
from src.Menu import menu



while True:
  
  game = Jogo()
  os.system('cls')
  
  if menu() == 0:
    os.system('cls')
    time.sleep(2)
    game.jogar()
  elif menu() == 1:
    print("holding")
  elif menu() == 2:
    break

os._exit()
