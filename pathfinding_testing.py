from cmu_112_graphics import *

class Point(object):
    def __init__(self,row,col,goalRow,goalCol,g,parent):
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
    app.numRows=31
    app.numCols=28
    app.margin=0
    app.m="draw"
    app.cellWidth=(app.width-2*app.margin)/(app.numRows)
    app.cellHeight=(app.height-2*app.margin)/(app.numCols) 
    app.matrix=[]
    for r in range(app.numRows):
        app.matrix.append([0 for i in range(app.numCols)])
    app.matrix=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1], [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1], [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1], [1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
        
def mousePressed(app,event):
    row,col=coordinatesToRowCol(app,event.x,event.y)
    print(row,col)
    if app.m=="draw":
        app.matrix[row][col]=1
    elif app.m=="erase":
        app.matrix[row][col]=0
    # for row in app.matrix:
    #     print(row)

def mouseDragged(app,event):
    row,col=coordinatesToRowCol(app,event.x,event.y)
    if app.m=="draw":
        app.matrix[row][col]=1
    elif app.m=="erase":
        app.matrix[row][col]=0
    # for row in app.matrix:
    #     print(row)
    
def keyPressed(app,event):
    # print(app.matrix)
    if event.key=="d":
        app.m="draw"
    elif event.key=="e":
        app.m="erase"
    elif event.key=="f":
        app.path=findPath(app)
        print(app.path)

def redrawAll(app,canvas):    
    for row in range(app.numRows):
        for col in range(app.numCols):
            x,y=convertRowColToCoordinates(app,row,col)
            colors=["white","blue","green"]
            fill=colors[app.matrix[row][col]]
            canvas.create_rectangle(x,y,x+app.cellWidth,y+app.cellHeight,fill=fill)
            if (row,col)==(12,13):
                canvas.create_rectangle(x,y,x+app.cellWidth,y+app.cellHeight,fill="black")
    
    for row,col in app.path:
        x,y=convertRowColToCoordinates(app,row,col)
        canvas.create_rectangle(x,y,x+app.cellWidth,y+app.cellHeight,fill="red")
                

def findPath(app):
    openList=[app.source]
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
            if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1 or app.matrix[newRow][newCol]==1:
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
                return final
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