# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 15:24:18 2022

@author: sayhan
"""

import numpy as np

NodeNumber = 0    

def IncreaseNodeNumber():
    global NodeNumber
    NodeNumber += 1

def SetNodeID():
    ID = NodeNumber
    IncreaseNodeNumber()
    return ID;

class Node:
    
    ID = 0
    Point = 0
    
    def __init__(self, ParentID, _point, _row, _col, _posx, _posy, _level, _face, _values):
        self.ID = SetNodeID()
        self.Parent = ParentID
        self.Point = _point
        self.Row = _row
        self.Col = _col
        self.Posx = _posx
        self.Posy = _posy
        self.Level = _level
        self.Face = _face
        self.Level = _level
        self.Values = _values

    def GetID(self):
        return self.ID
    
    def GetParent(self):
        return self.Parent
    
    def GetPoint(self):
        return self.Point
    
    def GetRow(self):
        return self.Row
    
    def GetCol(self):
        return self.Col
    
    def GetPosx(self):
        return self.Posx
    
    def GetPosy(self):
        return self.Posy
    
    def GetLevel(self):
        return self.Level
    
    def GetFace(self):
        return self.Face
    
    def GetValues(self):
        return [i.copy() for i in self.Values]
    
    def Print(self):
        return {"ID": self.ID,
                "Parent": self.Parent,
                "Point": self.Point,
                "Row": self.Row,
                "Col": self.Col,
                "Posx": self.Posx,
                "Posy": self.Posy,
                "Level": self.Level,
                "Face": self.Face
                }


Tree = []

inputRow = int(input("Insert Row: "))
inputCol = int(input("Insert Col: "))

row = inputRow
col = inputCol

inputPosx = int(input("Insert Posx: "))
inputPosy = int(input("Insert Posy: "))

posx = inputPosx
posy = inputPosy

Nodes = []

LevelNodes = []


rootParent = -1
rootPoint = 0
rootLevel = 0
rootFace = ""

Points = [0, 0]
point = 0
firstTime = True

values = []
cakeValues = []
cakeValuesInGame = []
def SetValues(_row, _col, _posx, _posy):
    global firstTime, cakeValues, cakeValuesInGame
    for i in range(_row):
        values.append([])
        for j in range(_col):
            if i == _posy - 1 and j == _posx - 1:
                continue
            values[i].append(np.random.randint(1, 9))
    if firstTime:
        cakeValuesInGame = values
        cakeValues = values
    firstTime = False

def RemoveValuesInGame(_direction, _row):
    global cakeValuesInGame
    p = 0
    if _direction == 't':
        for i in range(len(cakeValuesInGame[0])):
            p += cakeValuesInGame[0][i]
        cakeValuesInGame.remove(cakeValuesInGame[0])

    elif _direction == 'b':
        for i in range(len(cakeValuesInGame[len(cakeValuesInGame)-1])):
            p += cakeValuesInGame[len(cakeValuesInGame)-1][i]
        cakeValuesInGame = [i.copy() for i in cakeValuesInGame[:-1]]

    elif _direction == 'r':
        for i in range(_row):
            p += cakeValuesInGame[i][len(cakeValuesInGame[i])-1]
        cakeValuesInGame = [i[:-1].copy() for i in cakeValuesInGame]
        
    elif _direction == 'l':
        for i in range(_row):
            p += cakeValuesInGame[i][0]
        for i in range(_row):
            cakeValuesInGame[i].remove(cakeValuesInGame[i][0])
    return p

def RemoveValues(_direction, _row, _values):
    p = 0
    if _direction == 't':
        for i in range(len(_values[0])):
            p += _values[0][i]
        _values.remove(_values[0])

    elif _direction == 'b':
        for i in range(len(_values[len(_values)-1])):
            p += _values[len(_values)-1][i]
        _values = [i.copy() for i in _values[:-1]]

    elif _direction == 'r':
        for i in range(_row):
            p += _values[i][len(_values[i])-1]
        _values = [i[:-1].copy() for i in _values]
    elif _direction == 'l':
        for i in range(_row):
            p += _values[i][0]
        for i in range(_row):
            _values[i].remove(_values[i][0])
    return [p, _values]



def DrawCake(_row, _col, _posx, _posy):
    if firstTime:
        SetValues(_row, _col, _posx, _posy)
        
    row = _row
    col = _col
    posx = _posx
    posy = _posy
    print('\n\n')
    for i in range(row):
        print(" ___  "*col + " ")
        if ( i == posy-1 ):
            for j in range(posx-1):
                print("|_" + str(cakeValues[i][j]) + "_| ", end = '')
            print("|_X_| ", end = '')
            for j in range(col - 1 - (posx - 1)):
                print("|_" + str(cakeValues[i][posx + j - 1]) + "_| ", end = '')
        else:
            for j in range(col):
                
                print("|_" + str(cakeValues[i][j]) + "_| ", end = '')
        print('\n', end = '')
    print('\n\n')

def DrawCakeInGame(_row, _col, _posx, _posy):
    if firstTime:
        SetValues(_row, _col, _posx, _posy)
        
    row = _row
    col = _col
    posx = _posx
    posy = _posy
    print('\n\n')
    for i in range(row):
        print(" ___  "*col + " ")
        if ( i == posy-1 ):
            for j in range(posx-1):
                print("|_" + str(cakeValuesInGame[i][j]) + "_| ", end = '')
            print("|_X_| ", end = '')
            for j in range(col - 1 - (posx - 1)):
                print("|_" + str(cakeValuesInGame[i][posx + j - 1]) + "_| ", end = '')
        else:
            for j in range(col):
                
                print("|_" + str(cakeValuesInGame[i][j]) + "_| ", end = '')
        print('\n', end = '')
    print('\n\n')

def RowOperation(my_val, _row, _col, _posx, _posy, _values):
    global  Nodes, Tree, currentNode, LevelNodes

    if my_val == _posy or _row == 1:
        return

    face = ""
    if my_val == 1:
        face="t"
    else:
        face="b"

    rt = RemoveValues(face, _row, [i.copy() for i in _values])
    p = rt[0]
    newValues = rt[1]
    
    _row -= 1
    if(my_val == 1):
        _posy -= 1

    newNode = Node(currentNode, p, _row, _col, _posx, _posy, Nodes[currentNode].GetLevel()+1, face, newValues)
    Nodes.append(newNode)
    
    if Nodes[currentNode].GetLevel()+1 == len(LevelNodes):
        LevelNodes[len(LevelNodes)-1].append(newNode)
    else:
        LevelNodes.append([newNode])
    
    if(len(Tree)!=currentNode+1):
        Tree.append([newNode])
    else:
        Tree[currentNode] += [newNode]

def ColOperation(my_val, _row, _col, _posx, _posy, _values):
    global Nodes, Tree, currentNode, LevelNodes

    if my_val == _posx or _col == 1:
        return

    face=""
    if my_val==1:
        face="l"
    else:
        face="r"

    rt = RemoveValues(face, _row, [i.copy() for i in _values])
    p = rt[0]
    newValues = rt[1]

    _col -= 1
    if(my_val == 1):
        _posx -= 1

    newNode = Node(currentNode, p, _row, _col, _posx, _posy, Nodes[currentNode].GetLevel()+1, face, newValues)
    Nodes.append(newNode)
    
    if Nodes[currentNode].GetLevel()+1 == len(LevelNodes):
        LevelNodes[len(LevelNodes)-1].append(newNode)
    else:
        LevelNodes.append([newNode])
    if(len(Tree)!=currentNode+1):
        Tree.append([newNode])
    else:
        Tree[currentNode] += [newNode]

def MakeTree():
    global points, Nodes, Tree, currentNode, point
    run = True
    while run:
        if currentNode==len(Nodes):
            break
        
        row = Nodes[currentNode].GetRow()
        col = Nodes[currentNode].GetCol()
        posx = Nodes[currentNode].GetPosx()
        posy = Nodes[currentNode].GetPosy()
        point = Nodes[currentNode].GetPoint()
        values = Nodes[currentNode].GetValues()
        # print("currentNode:", currentNode, "values length:", len(values), len(values[0]))
        RowOperation(1, row, col, posx, posy, values)
        RowOperation(row, row, col, posx, posy, values)
        ColOperation(1, row, col, posx, posy, values)
        ColOperation(col, row, col, posx, posy, values)
        currentNode += 1
    pass

DrawCake(row, col, posx, posy)

root = Node(rootParent, rootPoint, row, col, posx, posy, 0, rootFace, cakeValues.copy())

currentNode = root.GetID()

LevelNodes.append([root])

Nodes.append(root)

MakeTree()

currentNode = root.GetID()

#  user and ai runs below function
def FindCurrentNodeInGame(_currentNode):
    global row, col, posx, posy, LevelNodes, stage, currentNode
    childs = len(Tree[_currentNode])
    for i in range(childs):
        iPrint = Tree[_currentNode][i].Print()
        if (iPrint["Row"] == row and iPrint["Col"] == col and iPrint["Posx"] == posx and iPrint["Posy"] == posy):
            _currentNode = iPrint["ID"]
            return _currentNode

def RowOperationInGame(my_val):
    global  row, col, posx, posy, Nodes, Tree, currentNode

    if my_val == posy :
        print("wrong parameter. Please try again")
        return

    face=""
    if my_val==1:
        face="t"
    else:
        face="b"

    point = RemoveValuesInGame(face, row)
    row -= 1
    if(my_val == 1):
        posy -= 1
    DrawCakeInGame(row, col, posx, posy)
    newNode = FindCurrentNodeInGame(currentNode)
    currentNode = newNode
    return point

def ColOperationInGame(my_val):
    global row, col, posx, posy, Nodes, Tree, currentNode

    if my_val == posx :
            print("wrong parameter. Please try again")
            return

    face=""
    if my_val==1:
        face="l"
    else:
        face="r"
    point = RemoveValuesInGame(face, row)

    col -= 1
    if(my_val == 1):
        posx -= 1
    
    DrawCakeInGame(row, col, posx, posy)
    newNode = FindCurrentNodeInGame(currentNode)
    currentNode = newNode
    return point

stage = 0

childPosition = 0

# AI calls CheckTheTreeInGame which in turns calls CheckPointsInGame
def CheckPointsInGame(_parent, _maximizer):
    global row, col, posx, posy, stage, currentNode, LevelNodes, childPosition, Tree, Nodes

    ans = Nodes[_parent].GetPoint()
    if _parent >= len(Tree):
        return ans

    childs = len(Tree[_parent])
    p = []
    index = 0
    for i in range(childs):
        p.append(Tree[_parent][i].GetPoint())
        if p[i] == max(p) and _maximizer:
            index = i
        elif p[i] == min(p) and not _maximizer:
            index = i

    if _maximizer:
        return CheckPointsInGame(Tree[_parent][index].GetID(), not _maximizer)
    else:
        return ans + CheckPointsInGame(Tree[_parent][index].GetID(), not _maximizer)
    

def CheckTheTreeInGame(_currentNode, _maximizer):
    global row, col, posx, posy, stage, LevelNodes, childPosition, Tree, Nodes

    points = []
    length = len(Tree[_currentNode])
        
    #     pass
    for k in range(length):
        points.append(CheckPointsInGame(Tree[_currentNode][k].GetID(), not _maximizer))

    for i in range(len(points)):
        if points[i] == max(points):
            return Tree[_currentNode][i].GetFace()
            pass


currentNode = 0
checker = True
while row>1 or col>1:
    if checker:
        my_selection = str(input("Select a side: "))

        stage += 1
        if my_selection == 't':
            Points[0] += RowOperationInGame(1)
        elif my_selection == 'b':
            Points[0] += RowOperationInGame(row)
        elif my_selection == 'l':
            Points[0] += ColOperationInGame(1)
        elif my_selection == 'r':
            Points[0] += ColOperationInGame(col)
        else:
            print("Error\n")
        print("User:", Points[0], "\nAI:", Points[1])

    else:
        newFace = CheckTheTreeInGame(currentNode, True)
        if newFace == 'l':
            Points[1] += ColOperationInGame(1)
            print("AI selected: l")
        elif newFace == 'r':
            Points[1] += ColOperationInGame(col)
            print("AI selected: r")
        elif newFace == 't':
            Points[1] += RowOperationInGame(1)
            print("AI selected: t")
        elif newFace == 'b':
            Points[1] += RowOperationInGame(row)
            print("AI selected: b")
        print("User:", Points[0], "\nAI:", Points[1])
        pass
    checker = not checker
    pass
print(Points[0], Points[1])
if Points[0] > Points[1]:
    print("Player Wins")
elif Points[0] < Points[1]:
    print("AI Wins")
else:
    print("Draw")