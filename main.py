from cmu_112_graphics import *
import random

class character():
    def __init__(self,fill,outline,initRow,initCol):
        self.dir="Right"
        self.fill=fill
        self.outline=outline
        self.row=initRow
        self.col=initCol
    
    def moveForward(self, app):
        if self.dir=="Right":
            self.col+=1
            if character.invalidMove(self,app):
                self.col-=1
        elif self.dir=="Left":
            self.col-=1
            if character.invalidMove(self,app):
                self.col+=1
        elif self.dir=="Up":
            self.row-=1
            if character.invalidMove(self,app):
                self.row+=1
        elif self.dir=="Down":
            self.row+=1
            if character.invalidMove(self,app):
                self.row-=1
        
    def invalidMove(self,app):
        if self.row<1 or self.row>app.numRows-2 or self.col<1 or self.col>app.numCols-2 or app.board[self.row][self.col]==1:
            return True
        return False
    
    def draw(self,app,canvas):
        # print(self.row,self.col)
        x,y=convertRowColToCoordinates(app, self.row+0.5,self.col+0.5)
        x+=app.margin
        y+=app.margin
        r= app.cellWidth/2
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=self.fill,outline=self.outline)

class pacChar(character):
    def __init__(self,fill,outline,initRow,initCol):
        super().__init__(fill,outline,initRow,initCol)
        self.dir="Up"
        
    def moveForward(self, app):
        super().moveForward(app)
        pacChar.consumePellet(self, app)
        
    def consumePellet(self, app):
        if app.board[self.row][self.col]==2:
            app.board[self.row][self.col]=0
            app.score+=1
            app.numPellets-=1
            if app.numPellets<=0:
                app.isWin=True
        
class ghost(character):
    def __init__(self,fill,outline,initRow,initCol,path=[]):
        super().__init__(fill,outline,initRow,initCol)
        self.path=[]
    
class Point(object):
    # Used for pathfinding
    def __init__(self,row,col,goalRow,goalCol,g,parent):
        self.row=row
        self.col=col
        self.goalRow=goalRow
        self.goalCol=goalCol
        self.g=g
        self.h= abs(row-goalRow)+abs(col-goalCol)
        self.f=self.g+self.h
        self.parent=parent

def findPath(app,startRow,startCol,endRow,endCol):
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

def createBoard(app):
    app.board=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1], [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1], [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1], [1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

def generateBoard(app):
    pass

def convertRowColToCoordinates(app, row,col):
    return col*app.cellWidth,row*app.cellHeight

def moveGhosts(app):    
    for ghost in app.ghosts:
        ghost.row=ghost.path[0][0]
        ghost.col=ghost.path[0][1]
        ghost.path.pop(0)

def drawGhosts(app,canvas):
    for ghost in app.ghosts:
        ghost.draw(app,canvas)

def randomizeGhostMovement(app):
    import random
    directions= ["Left","Right","Down","Up"]
    oppDirs={"Left":"Right","Right":"Left","Down":"Up","Up":"Down"}
    for ghost in app.ghosts:
        d=directions[random.randrange(0,4)]
        # Ghosts are not allowed to reverse directions
        if d!=ghost.dir and d!=oppDirs[ghost.dir]:
            ghost.dir=d
    
def ghostCollisions(app):
    if ((app.pacman.row==app.inky.row and app.pacman.col==app.inky.col) 
        or (app.pacman.row==app.blinky.row and app.pacman.col==app.blinky.col) 
        or (app.pacman.row==app.pinky.row and app.pacman.col==app.pinky.col) 
        or (app.pacman.row==app.clyde.row and app.pacman.col==app.clyde.col)):
        app.isLose=True

def appStarted(app):
    app.isWin=False
    app.isLose=False   
    app.time=0
    app.numPellets=348
    app.numRows=28
    app.numCols=28
    createBoard(app)
    for row in app.board:
        print(row)
    app.margin=0
    app.cellWidth=(app.width-2*app.margin)/(app.numRows)
    app.cellHeight=(app.height-2*app.margin)/(app.numCols)
    app.timerDelay=150
    app.score=0
    app.pacman=pacChar("yellow","black",17,13)
    # Inky, blinky, pinky, and clyde are the ghosts
    app.inky=ghost("cyan","black",12,13)
    app.blinky=ghost("red","black",13,13)
    app.pinky=ghost("pink","black",13,12)
    app.clyde=ghost("orange","black",12,12)
    app.ghosts=[app.inky,app.blinky,app.pinky,app.clyde]
    resetPathFinding(app) #to initialize paths

def resetPathFinding(app):
    # Blinky pathfinds to pac-man's location
    app.blinky.path=findPath(app,app.inky.row,app.inky.col,app.pacman.row,app.pacman.col)
    

    # Inky pathfinds to random tile near pac-man
    while True:
        drow=random.randrange(-3,4)
        dcol=random.randrange(-3,4)
        newRow=app.pacman.row+drow
        newCol=app.pacman.col+dcol
        if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1 or app.board[newRow][newCol]==1:
            continue
        app.inky.path=findPath(app,app.inky.row,app.inky.col,newRow,newCol)
        break
    
    
    # Pinky pathfinds to four tiles ahead of pac-man's location 
    dirToDrowDcol={"Right":(0,1),"Left":(0,-1),"Down":(1,0),"Up":(-1,0)}
    for n in range(4,-1,-1):
        drow,dcol=dirToDrowDcol[app.pinky.dir]
        drow*=n
        dcol*=n
        newRow=app.pacman.row+drow
        newCol=app.pacman.col+dcol
        if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1 or app.board[newRow][newCol]==1:
            continue
        app.pinky.path=findPath(app,app.pinky.row,app.pinky.col,newRow,newCol)
        break
        
        
    # Clyde pathfinds to pacman when he is far from pac-man, when he is close he pathfinds to bottom corner
    clydeDistanceFromPacman= ((app.pacman.row-app.clyde.row)**2+(app.pacman.col-app.clyde.col)**2)**0.5
    if clydeDistanceFromPacman<=8:
        app.clyde.path=findPath(app,app.clyde.row,app.clyde.col,20,6)
    else:
        # Always goes towards 20,6 when far from Pac-Man
        app.clyde.path=findPath(app,app.clyde.row,app.clyde.col,app.pacman.row,app.pacman.col)
    
def keyPressed(app,event):
    k=event.key
    if k=="Up" or k=="Down" or k=="Left" or k=="Right":
        app.pacman.dir=k
        
def timerFired(app):
    app.time+=1
    if app.time%2==1:
        resetPathFinding(app)
    if app.isWin==False and app.isLose==False:
        moveGhosts(app)
        ghostCollisions(app)
        if app.isLose==False:
            app.pacman.moveForward(app)
            ghostCollisions(app)
        
def redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="black")
    drawGrid(app,canvas)
    drawGhosts(app,canvas)
    app.pacman.draw(app, canvas)
    if app.isWin:
        canvas.create_text(app.width/2,app.height/2,text="WIN",font="Times 100 bold", fill="white")
    if app.isLose:
        canvas.create_text(app.width/2,app.height/2,text="DEAD",font="Times 100 bold", fill="white")
    
def drawGrid(app,canvas):
    for row in range(app.numRows):
        for col in range(app.numCols):
            if app.board[row][col]==1:
                # wall
                x,y=convertRowColToCoordinates(app,row,col)
                x+=app.margin
                y+=app.margin
                canvas.create_rectangle(x,y,x+app.cellWidth,y+app.cellHeight,fill="blue")
            elif app.board[row][col]==2:
                # pellet
                x,y=convertRowColToCoordinates(app,row+0.5,col+0.5)
                x+=app.margin
                y+=app.margin
                r=app.cellWidth/6
                canvas.create_oval(x-r,y-r,x+r,y+r,fill="yellow")

runApp(width=540,height=540)