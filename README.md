# Prompt-Tetris

A version of the most popular gamfe, Tetris, working in prompt without GUI

![Static Badge](https://img.shields.io/badge/Development-Working?style=flat&logo=Development&label=Working&color=%23FF8C00)
> [!IMPORTANT]
> The Tetris will recive new features, Conunter Points, Next Piaces, Difficult, and a menu choice call config.
> The config option is chage Icons, colors and a difficult

## About
The game is based in a matrix 10x20, 
### Menu

```python
[][][][][][]  [][][][][][] [][][][][][] [][][][][][] [][][] [][][][][][]
[][][][][][]  [][][][][][] [][][][][][] [][][][][][] [][][] [][][][][][]
    [][]      [][]             [][]     [][]    [][] [][][] [][]        
    [][]      [][]             [][]     [][]    [][] [][][] [][]        
    [][]      [][][][]         [][]     [][][][]     [][][] [][][][][][]    
    [][]      [][][][]         [][]     [][][][]     [][][] [][][][][][]
    [][]      [][]             [][]     [][]    [][] [][][]         [][]
    [][]      [][]             [][]     [][]    [][] [][][]         [][]
    [][]      [][][][][][]     [][]     [][]    [][] [][][] [][][][][][]
    [][]      [][][][][][]     [][]     [][]    [][] [][][] [][][][][][]
```
the menu that use de `questionaty` libary.
Was used this line for create a option with box out.
```python
f"{" "*30}┌{'─'*3}{'─'*int(len(Op[0]))}{'─'*3 }┐\n {" "*32}│   {Op[0]}   │\n {" "*32}└{'─'*3}{'─'*int(len(Op[0]))}{'─'*3}┘"
```
┌─────────────┐
│   INICIAR   │
└─────────────┘

### Pices
The pices it's a class with: Shape, Rotation, TypeShape and a Rot.

```python
class Tshape():
```
Shape.
```python
self.__Shape = [
                [3, 3, 3],
                [0, 3]]
```

TypeShaope

The `self.__TypeShape` it's recive the value like a ID for exemple `self.__TypeShape = 'T'`

Rotation

The Rotation fuction change the `self.__Shape` and use the `self.__Rot` like a counter for choices in the `match case`.

```python
def Rotation(self):
        self.__Rot += 1
        if self.__Rot > 3:
          self.__Rot = 0
        
        match self.__Rot:
            case 0:
                self.__Shape = [
                [3, 3, 3],
                [0, 3]
            ]
            case 1:
                self.__Shape = [
                [0, 3],
                [3, 3],
                [0, 3]
            ]
            case 2:
                self.__Shape = [
                [0 ,3],
                [3, 3, 3]
            ]
            case 3:
                self.__Shape = [
                [3],
                [3, 3],
                [3]
            ]
```

## Board

The board where tha magic happens, cause we have importants function like:
- `ShowMap()`
- `Colorize()`
- `AddShape()`
- `RemoveShape()`
- `Colizion()`
- `FixShape()`
- `removeLines`

All of them, interacting with both the board and the pieces.  
For moving better the pieces, each move it's call `removeShape()` and after call `AddShape()`.  
The `ShowMap()` it's a function that is looping for, returning the `Coloraze()` function, printing line each line.  
The `Colorazie()` is a function where happen the replace of chars and colors using the `colorama` libary.  

## Game

The game literalliy runs here.
In this class, the keys move and rotation the pieces, using the `Keyboard` libary t, get the piaces down, and summon others pieces
This part of the code, is a multiprocessing, reciving a lambda with a `insert()` function that move and rotation the objects pieces 
`keyboard.add_hotkey('KEY', lambda: insert('TYPE'))`


## Install

1. Git Clone
   `git clone https://github.com/gubazzs/Prompt-Tetris.git`

2. find and into a repository folder
  `cd Prompt-Tetris`

4. Install the Requiriments
   `pip3 install -r requiriments.txt`
   
5. Run The file Main.py
   `Python Main.py`

6. Have  a fun!!! 



