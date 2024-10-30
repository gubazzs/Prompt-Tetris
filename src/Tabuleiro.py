from colorama import Fore, Style, Back

class Tabuleiro():
  
  def __init__(self, X: int, Y: int) -> None:
    self.linhaMorta = None
    self.linhasRemovidas=0
    self.__sizeX = X
    self.__sizeY = Y
    self.__MShape = [[0 for _ in range(self.__sizeX)] for _ in range(self.__sizeY)]
    self.__listcolor = {1:Fore.YELLOW, -1:Fore.YELLOW, 2:Fore.CYAN, -2:Fore.CYAN, 3:Fore.MAGENTA, -3:Fore.MAGENTA, 4:Fore.BLUE, -4:Fore.BLUE,  5:Fore.LIGHTRED_EX, -5:Fore.LIGHTRED_EX, 6:Fore.GREEN, -6:Fore.GREEN,  7:Fore.RED, -7:Fore.RED, 0:Fore.BLACK, 8:Fore.RED, 9:Fore.BLACK}
  
  def getSizeX(self):
    return self.__sizeX
  
  def getShape(self):
    return self.__MShape
  
  def setShape(self, new):
    self.__MShape = new
  
  def ShowMap(self) -> str:
    [self.Colorize(_) for _ in self.__MShape]
    print(f'<!{20*'='}!>')
    print(f'  {10*'\/'}  ')
              
  def Colorize(self, v):
    color = lambda n: Back.BLACK + self.__listcolor[n] + '[]' + Style.RESET_ALL if n != 0 else  Back.BLACK + self.__listcolor[n] + ' .' + Style.RESET_ALL
    print('<!' + ''.join(map(color, v)) + '!>')  
  
  def AddShape(self, peca: object, posX: int, posY: int, TypeRotation=0):
    shape = peca.getShape()
    for i in range(len(shape)):
      for j in range(len(shape[i])):
        if shape[i][j] != 0:
          self.__MShape[posY + i][posX + j] = shape[i][j] 
               
  def RemoveShape(self, peca: object, posX: int, posY: int, TypeRotation=0):
    shape = peca.getShape()
    for i in range(len(shape)):
      for j in range(len(shape[i])):
        if shape[i][j] != 0:
          self.__MShape[posY + i][posX + j] = 0
      
  def Colision(self, peca: object, posX: int, posY: int) -> bool:
    shape = peca.getShape()
    for i in range(len(shape)):
      for j in range(len(shape[i])):
        if shape[i][j] != 0:
          if posY + i >= self.__sizeY or posY + i < 0:
              return True
          if posX + i < 0 or posX + j >= self.__sizeX:
              return True
          if self.__MShape[posY + i][posX + j] in [-1, -2, -3, -4, -5, -6, -7]:
              return True            
    return False
  
  def FixShape(self, peca: object, posX: int, posY: int):
    shape = peca.getShape()
    TypeShape = peca.getTypeShape()
    
    if TypeShape == 'O':
      for i in range(len(shape)):
        for j in range(len(shape[i])):
          self.__MShape[posY + i][posX + j] = -1
    
    elif TypeShape == 'I':
      for i in range(len(shape)):
        for j in range(len(shape[i])):
          self.__MShape[posY + i][posX + j] = -2
    elif TypeShape == 'T':
      for i in range(len(shape)):
        for j in range(len(shape[i])):
          if shape[i][j] != 0:
            self.__MShape[posY + i][posX + j] = -3
    
    elif TypeShape == 'L':
      for i in range(len(shape)):
        for j in range(len(shape[i])):
          if shape[i][j] != 0:
            self.__MShape[posY + i][posX + j] = -4
    
    elif TypeShape == 'J':
      for i in range(len(shape)):
        for j in range(len(shape[i])):
          if shape[i][j] != 0:
            self.__MShape[posY + i][posX + j] = -5
                
    elif TypeShape == 'Z':
      for i in range(len(shape)):
        for j in range(len(shape[i])):
          if shape[i][j] != 0:
            self.__MShape[posY + i][posX + j] = -6
    
    elif TypeShape == 'S':
      for i in range(len(shape)):
        for j in range(len(shape[i])):
          if shape[i][j] != 0:
            self.__MShape[posY + i][posX + j] = -7
          
  def removeLines(self):
    for linha in range(len(self.__MShape)):
      if 0 not in self.__MShape[linha]:
        self.__MShape[linha]=[9] * len(self.__MShape[linha])        
        for linhaMorta in range(len(self.__MShape)):
          if 9 in self.__MShape[linhaMorta]:
            self.linhaMorta = linhaMorta
            break
              
      if self.linhaMorta != None:
        for i in range(self.linhaMorta - 1, -1, -1):
          self.__MShape[i + 1] = self.__MShape[i]
          self.linhaMorta = None