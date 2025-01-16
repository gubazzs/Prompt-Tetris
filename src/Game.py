from src.Tabuleiro import Tabuleiro
from src.Pecas import JShape, LShape, SquareShape, LineShape, TShape, ZShape, SShape
import time, os, random
import keyboard

TClear = "clear" if os.name == 'posix' else "cls"

class Jogo():
    
    def __init__(self) -> None:
        self.listclear = [1, 2, 3, 4, 5, 6, 7]
        self.pecaAtual = self.GeraParts()
        self.Tabu = Tabuleiro(10, 20)
        self.posX = 3
        self.posY = 0
        self.counter = 0 
        self.down_rate = 14
    
    def GeraParts(self):
        SelectShape = [SquareShape(), LineShape(), TShape(), ZShape(), SShape(), JShape(), LShape()]   
        return random.choice(SelectShape)
    
    def FramePerScond(self, fps=1):
        time.sleep(fps)
        
    
    def DescerPeca(self):
        if not self.Tabu.Colision(self.pecaAtual, self.posX, self.posY + 1)  and self.counter == self.down_rate:
            self.Tabu.RemoveShape(self.pecaAtual, self.posX, self.posY)
            self.Tabu.setShape([[0 if elemento in self.listclear else elemento for elemento in linha] for linha in self.Tabu.getShape()]) 
            self.posY += 1
            self.Tabu.AddShape(self.pecaAtual, self.posX, self.posY)
            self.counter = 0 
        elif self.counter == self.down_rate:
            self.Tabu.FixShape(self.pecaAtual, self.posX, self.posY)
            self.Tabu.removeLines()
            self.pecaAtual = self.GeraParts()
            self.posX = 3
            self.posY = 0
            if self.Tabu.Colision(self.pecaAtual, self.posX, self.posY):
                os.system(TClear)
                print("Fim de Jogo")
                time.sleep(3)
            self.counter = 0
    
    def ComandoTWO(self):
        
        def insert(v: str, p=0):
            
            if v == 'x':
            # Tenta mover para a esquerda ou direita
                newX = self.posX + p
                newY = self.posY
                # Só move se não houver colisão
                if not self.Tabu.Colision(self.pecaAtual, newX, newY):
                    self.posX = newX
                    
            elif v == 'r':
                if self.posX < self.Tabu.getSizeX() -2: 
                    self.pecaAtual.Rotation()
                
            elif v == 'y':
                self.counter = 14
            return 0
    
        keyboard.add_hotkey('left',lambda : insert('x',-1))
        keyboard.add_hotkey('right',lambda : insert('x',1))    
        keyboard.add_hotkey('down',lambda : insert('y'))
        keyboard.add_hotkey('up', lambda: insert('r'))               
     
        while not self.Tabu.Colision(self.pecaAtual, self.posX, self.posY):
            os.system(TClear)
            self.DescerPeca()
            self.Tabu.ShowMap()
            self.counter += 1
            time.sleep(1/75)
            if self.Tabu.Colision(self.pecaAtual, self.posX, self.posY):
                break
        os.system(TClear)

                                              
    def jogar(self):
        self.ComandoTWO()
