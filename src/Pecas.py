class SquareShape():

    def __init__(self) -> None:
        self.__Shape = [
            [1, 1],
            [1, 1]
        ]
        self.__TypeShape = 'O'
        
    def Rotation(self):
        self.__Shape

    def getShape(self) -> list:
        return self.__Shape
    
    def getRotation(self) -> None:
        return None
    
    def getTypeShape(self) -> str:
        return self.__TypeShape
        
class LineShape():

    def __init__(self) -> None:
        self.__Shape = [
            [2, 2, 2, 2]
        ]
        self.__TypeShape = 'I'
        
    def Rotation(self):
        if len(self.__Shape[0]) == 4:
            self.__Shape =[
                [2],
                [2],
                [2],
                [2]
            ] 
        else:
            self.__Shape = [
            [2, 2, 2, 2]
        ]
               
    def getShape(self) -> list:
        return self.__Shape
    
    def getRotation(self) -> None:
        return None
    
    def getTypeShape(self) -> str:
        return self.__TypeShape
    
class TShape():

    def __init__(self) -> None:
        self.__Shape = [
          #180° - case 0:
                [3, 3, 3],
                [0, 3]
            ]
        self.__Rot = 0
        self.__TypeShape = 'T'
        
    def Rotation(self):
        self.__Rot += 1
        if self.__Rot > 3:
          self.__Rot = 0
        
        match self.__Rot:
            
            case 0:
                #180°
                self.__Shape = [
                [3, 3, 3],
                [0, 3]
            ]
            case 1:
                #270°
                self.__Shape = [
                [0, 3],
                [3, 3],
                [0, 3]
            ]
            case 2:
                #0°
                self.__Shape = [
                [0 ,3],
                [3, 3, 3]
            ]
            case 3:
                #90°
                self.__Shape = [
                [3],
                [3, 3],
                [3]
            ]
                
    def getShape(self) -> list:
      return self.__Shape
  
    def getRotation(self) -> int:
        return self.__Rot
    
    def getTypeShape(self) -> str:
        return self.__TypeShape

class LShape():

    def __init__(self) -> None:
        self.__Shape = [
                [4],
                [4],
                [4, 4]
                ]
        self.__Rot = 0
        self.__TypeShape = 'L'
        
    def Rotation(self):
        self.__Rot += 1
        if self.__Rot > 3:
          self.__Rot = 0
        
        match self.__Rot:
            
            case 0:
                #180°
                self.__Shape = [
                [4],
                [4],
                [4, 4]
                ]
                
            case 3:
                #270°
                self.__Shape = [
                [0, 0, 4],
                [4, 4, 4]
                
            ]
            case 2:
                #0°
                self.__Shape = [
                [4, 4],
                [0, 4],
                [0, 4]
            ]
            case 1:
                #90°
                self.__Shape = [
                [4, 4, 4],
                [4]
            ]
                
    def getShape(self) -> list:
      return self.__Shape
  
    def getRotation(self) -> int:
        return self.__Rot
    
    def getTypeShape(self) -> str:
        return self.__TypeShape

class SShape():

    def __init__(self) -> None:
        self.__Shape = [
                [7, 7, 0],
                [0, 7, 7]
                ]
        self.__Rot = 0
        self.__TypeShape = 'S'
        
    def Rotation(self):
        self.__Rot += 1
        if self.__Rot > 1:
          self.__Rot = 0
        
        match self.__Rot:
            
            case 0:
                #180°
                self.__Shape = [
                [7, 7, 0],
                [0, 7, 7]
                ]
                
            case 1:
                #270°
                self.__Shape = [
                [0,7],
                [7,7],
                [7,0]
                ]
                
    def getShape(self) -> list:
      return self.__Shape
  
    def getRotation(self) -> int:
        return self.__Rot
    
    def getTypeShape(self) -> str:
        return self.__TypeShape

class ZShape():

    def __init__(self) -> None:
        self.__Shape = [
                [0, 6, 6],
                [6, 6, 0]
                ]
        self.__Rot = 0
        self.__TypeShape = 'Z'
        
    def Rotation(self):
        self.__Rot += 1
        if self.__Rot > 1:
          self.__Rot = 0
        
        match self.__Rot:
            
            case 0:
                #180°
                self.__Shape = [
                [0, 6, 6],
                [6, 6, 0]
                ]
                
            case 1:
                #270°
                self.__Shape = [
                [6,0],
                [6,6],
                [0,6]
                ]
                
    def getShape(self) -> list:
      return self.__Shape
  
    def getRotation(self) -> int:
        return self.__Rot
    
    def getTypeShape(self) -> str:
        return self.__TypeShape

class JShape():

    def __init__(self) -> None:
        self.__Shape = [
                [0, 5],
                [0, 5],
                [5, 5]
                ]
        self.__Rot = 0
        self.__TypeShape = 'J'
        
    def Rotation(self):
        self.__Rot += 1
        if self.__Rot > 3:
          self.__Rot = 0
        try:
          match self.__Rot:

              case 0:
                  #180°
                  self.__Shape = [
                  [0, 5],
                  [0, 5],
                  [5, 5]
                  ]

              case 3:
                  #270°
                  self.__Shape = [
                  [5, 0, 0],
                  [5, 5, 5]

              ]
              case 2:
                  #0°
                  self.__Shape = [
                  [5, 5],
                  [5, 0],
                  [5, 0]
              ]
              case 1:
                  #90°
                  self.__Shape = [
                  [5, 5, 5],
                  [0, 0, 5]
              ]
        except IndexError:
          self.__Rot -= 1
                
    def getShape(self)-> list:
      return self.__Shape
  
    def getRotation(self) -> int:
        return self.__Rot
    
    def getTypeShape(self) -> str:
        return self.__TypeShape
