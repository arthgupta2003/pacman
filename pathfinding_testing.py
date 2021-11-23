from cmu_112_graphics import *
import random

class Point(object):
    def __init__(self,row,col,goalRow=1,goalCol=1,g=0,parent=None):
        self.row=row
        self.col=col
        self.goalRow=goalRow
        self.goalCol=goalCol
        self.g=g
        self.h= abs(row-goalRow)+abs(col-goalCol)
        self.f=self.g+self.h
        self.parent=parent

def convertRowColToCoordinates(app, row,col):
    return col*app.cellWidth,row*app.cellHeight

def coordinatesToRowCol(app,x,y):
    return int(y//app.cellHeight), int(x//app.cellWidth)

def appStarted(app):
    app.path=[]
    app.source=Point(1,1,26,24,0,None)
    app.goal=(12,13)
    app.numRows=28
    app.numCols=28
    app.margin=0
    app.m="draw"
    app.cellWidth=(app.width-2*app.margin)/(app.numRows)
    app.cellHeight=(app.height-2*app.margin)/(app.numCols) 
    app.board=[]
    for r in range(app.numRows):
        app.board.append([1 for i in range(app.numCols)])
    app.staticBoard=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1], [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1], [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1], [1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
    # generateRandomBoard(app)
    app.board=app.staticBoard
                
def mousePressed(app,event):
    row,col=coordinatesToRowCol(app,event.x,event.y)
    for r in range(app.numRows):
        for c in range(app.numCols):
            if r==0 or c==0 or r==app.numRows-1 or c==app.numCols-1:
                app.board[r][c]=1
    print(row,col)
    if app.m=="draw":
        app.board[row][col]=1
    elif app.m=="erase":
        app.board[row][col]=0
    # for row in app.board:
    #     print(row)

def mouseDragged(app,event):
    row,col=coordinatesToRowCol(app,event.x,event.y)
    if app.m=="draw":
        app.board[row][col]=1
    elif app.m=="erase":
        app.board[row][col]=0
    # for row in app.board:
    #     print(row)
    
def keyPressed(app,event):
    # print(app.board)
    if event.key=="d":
        generateRandomBoard(app)
    elif event.key=="e":
        app.m="erase"
    elif event.key=="f":
        app.path=findPath(app,1,1,15,5)
        print(app.path)

def redrawAll(app,canvas):    
    for row in range(app.numRows):
        for col in range(app.numCols):
            x,y=convertRowColToCoordinates(app,row,col)
            colors=["white","blue","green"]
            fill=colors[app.board[row][col]]
            canvas.create_rectangle(x,y,x+app.cellWidth,y+app.cellHeight,fill=fill)
            if (row,col)==(12,13):
                canvas.create_rectangle(x,y,x+app.cellWidth,y+app.cellHeight,fill="black")
    
    for row,col in app.path:
        x,y=convertRowColToCoordinates(app,row,col)
        canvas.create_rectangle(x,y,x+app.cellWidth,y+app.cellHeight,fill="red")
   
def generateRandomBoard(app):
    # Using Randomized Prim's algorithm (source: https://en.wikipedia.org/wiki/Maze_generation_algorithm)
    app.board[1][1]=0
    closedList={(1,1)}
    openList={(1,2),(2,1)} 
    while openList!=set():
        parentRow,parentCol=(random.sample(openList, 1))[0] #source: https://stackoverflow.com/questions/15837729/random-choice-from-set-python
        visitedNeighbors=0
        newRow,newCol=1,1
        children=[]
        for drow,dcol in [(1,0),(0,1),(-1,0),(0,-1)]:
            newRow=drow+parentRow
            newCol=dcol+parentCol
            if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1:
                continue
            if (newRow,newCol) in closedList:
                visitedNeighbors+=1
            children.append((newRow,newCol))
        if visitedNeighbors==1:
            closedList.add((parentRow,parentCol))
            app.board[parentRow][parentCol]=0
            for child in children:
                openList.add(child)
        openList.remove((parentRow,parentCol))
    # Add ghost box:
    for i in range(12,17):
        for j in range(10,18):
            app.board[i][j]=app.staticBoard[i][j]
    # Clean up border
    for r in range(app.numRows):
        for c in range(app.numCols):
            if r==0 or c==0 or r==app.numRows-1 or c==app.numCols-1:
                app.board[r][c]=1
                
    # Clears up dead ends
    for r in range(app.numRows):
        for c in range(app.numCols):
            parentRow,parentCol=r,c
            neighboringPaths=0
            if app.board[parentRow][parentCol]==0:
                for drow,dcol in [(1,0),(0,1),(-1,0),(0,-1)]:
                    newRow=drow+parentRow
                    newCol=dcol+parentCol
                    if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1:
                        continue
                    if app.board[newRow][newCol]==0:
                        neighboringPaths+=1
                if neighboringPaths<=1:
                    app.board[parentRow][parentCol]=1
               
    #Adds some holes to map
    for r in range(app.numRows):
        for c in range(app.numCols):
            parentRow,parentCol=r,c
            neighboringPaths=0
            if app.board[parentRow][parentCol]==1:
                for drow,dcol in [(1,0),(0,1),(-1,0),(0,-1)]:
                    newRow=drow+parentRow
                    newCol=dcol+parentCol
                    if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1:
                        continue
                    if app.board[newRow][newCol]==0:
                        neighboringPaths+=1
                if neighboringPaths>=2:
                    app.board[parentRow][parentCol]=1
                    
                
def findPath(app,startRow,startCol,endRow,endCol):
    # Pathfinding using A*
    openList=[Point(startRow,startCol,endRow,endCol,0,None)]
    # Openlist is initialized with the start point, and has no parent(since it is the highest in the tree of points)
    closedList=[]
    while openList!=[]:
        q=openList[0]
        bestF=q.f
        for point in openList:
            if point.f<bestF:
                bestF=point.f
                q=point
        openList.remove(q)
        children=[]
        for drow,dcol in [(1,0),(0,1),(-1,0),(0,-1)]:
            newRow=drow+q.row
            newCol=dcol+q.col
            if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1 or app.board[newRow][newCol]==1:
                continue               
            children.append(Point(q.row+drow,q.col+dcol,q.goalRow,q.goalCol,q.g+1,q))
        for child in children:
            usefulChild=True
            if child.row==child.goalRow and child.col==child.goalCol:
                final=[]
                s=child
                # print(child.row)
                # print(s.row)
                while s!=None:
                    final.append((s.row,s.col))
                    s=s.parent
                return final[::-1]
            for point in openList:
                if point.row==child.row and point.col==child.col and point.f<child.f:
                    usefulChild=False
            for point in closedList:
                if point.row==child.row and point.col==child.col and point.f<child.f:
                    usefulChild=False
            if usefulChild:
                openList.append(child)
        closedList.append(q)
    return None
       
    
    
runApp(width=800,height=800)