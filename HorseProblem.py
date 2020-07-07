X = 0
Y = 1
SIZE = 5

def buildBoard():
    board = []
    for x in range(SIZE):
        for y in range(SIZE):
            box = [x, y]
            board.append(box)
    print(board)
    return board

def buildGraph(board, black):
    graph = {}
    for box in board:
        graph[tuple(box)] = getPossiblePlay(box, black)
    print(graph)
    return graph

def isBlackPiece(box, black):
    for blackPieces in black:
        if box[X] == blackPieces[X] and box[Y] == blackPieces[Y]:
            return True
    return False

# Get possible moves for the horse
def getPossiblePlay(box, black):
    posibleMoves = []
    x = box[X] + 2
    y = box[Y] + 1
    if x < SIZE and y < SIZE:
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = box[X] + 2
    y = box[Y] - 1 
    if x < SIZE and y >= 0 :
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = box[X] + 1
    y = box[Y] - 2
    if x < SIZE and y >= 0 :
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = box[X] - 1 
    y = box[Y] - 2 
    if x >= 0 and y >= 0:
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = box[X] - 2
    y = box[Y] + 1
    if x >= 0  and y < SIZE:
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = box[X] - 2
    y = box[Y] - 1 
    if x >= 0  and y >= 0 :
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = box[X] + 1
    y = box[Y] + 2
    if x < SIZE and y < SIZE :
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = box[X] - 1 
    y = box[Y] + 2 
    if x >= 0 and y < SIZE:
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    return posibleMoves

def visited(box, visitedBox):
    if visitedBox.count(box) > 0:
        return True
    else:
        return False

# DFS Algorithm
def DFS(graph, whites, startHorse):
    stack = []
    visitedBox = []
    stack.append(startHorse)
    visitedBox.append(startHorse)
    while len(stack) > 0:
        box = stack[len(stack) - 1]
        stack.pop()
        visitedBox.append(box)
        if visited(whites, visitedBox):
            break
        neighboors = graph.get(tuple(box))
        for neighboor in neighboors:
            if not visited(neighboor, visitedBox):
                stack.append(neighboor)
    print('SOLUTION')            
    print(visitedBox)

def isSolution(whites, visitedBox):
    for white in whites:
        if visitedBox.count(white) < 1:
            return False
    return True
             

# Using readlines() 
file1 = open("/Users/deyanirasurysadaymezamartinez/Documents/Sury/Maestria/2/IA/Proyecto2_CaballoAjedrez/test3.txt", "r") 
Lines = file1.readlines() 
  
count = 0
whites = []
blacks = []
reading = 1

#Read file for initialized board
print("Test file")
for line in Lines: 
    #print("Line{}: {}".format(count, line.strip()))
    print("Coordinate: {}".format(line.strip()))
    if not line.strip():
        reading = reading + 1
        continue
    line = line.replace('\n','')
    coord = list(map(int,line.split(" ")))
    if reading == 1:
        startHorse = coord
    elif reading == 2:
        whites.append(coord)
    else:
        blacks.append(coord)
print('HORSE START POSITION')
print (startHorse)
print('WHITE PIECES POSITION')
print (whites)
print('BLACK PIECES POSITION')
print (blacks)
board = buildBoard()
graph = buildGraph(board, blacks)

DFS(graph, whites, startHorse)




