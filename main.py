from cmu_112_graphics import *

class character():
    def __init__(self,fill,outline):
        self.dir="Right"
        self.col=2
        self.row=2
        self.fill=fill
        self.outline=outline
    
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
        print(self.row,self.col)
        x,y=convertRowColToCoordinates(app, self.row+0.5,self.col+0.5)
        x+=app.margin
        y+=app.margin
        r= app.cellWidth/2
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=self.fill,outline=self.outline)

class pacChar(character):
    def __init__(self,fill,outline):
        super().__init__(fill,outline)
        self.dir="Up"
        self.col=13
        self.row=2
        
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
    pass
    

def createBoard(app):
    app.board=[]
    for row in range(app.numRows):
        currentRow=[]
        for col in range(app.numCols):
            if row==0 or col==0 or row==app.numRows-1 or col==app.numCols-1:
                # 1=wall
                currentRow.append(1)
            elif row%3==2 or col%3==2:
                # 2=pellet
                currentRow.append(2)
                app.numPellets+=1
            # elif row%3==1 or row%6==3 or col%3==1 or col%3==3:
            #     # 0=empty cell
            #     currentRow.append(0)
            else:
                # 1=wall
                currentRow.append(1)
        app.board.append(currentRow)

def convertRowColToCoordinates(app, row,col):
    return col*app.cellWidth,row*app.cellHeight

def moveGhosts(app):
    app.inky.moveForward(app)
    app.blinky.moveForward(app)
    app.pinky.moveForward(app)
    app.clyde.moveForward(app)

def drawGhosts(app,canvas):
    app.inky.draw(app,canvas)
    app.blinky.draw(app,canvas)
    app.pinky.draw(app,canvas)
    app.clyde.draw(app,canvas)

def randomizeGhostMovement(app):
    import random
    directions= ["Left","Right","Down","Up"]
    app.inky.dir= directions[random.randrange(0,4)]
    app.blinky.dir= directions[random.randrange(0,4)]
    app.pinky.dir= directions[random.randrange(0,4)]
    app.clyde.dir= directions[random.randrange(0,4)]
    
def ghostCollisions(app):
    if ((app.pacman.row==app.inky.row and app.pacman.col==app.inky.col) 
        or (app.pacman.row==app.blinky.row and app.pacman.col==app.blinky.col) 
        or (app.pacman.row==app.pinky.row and app.pacman.col==app.pinky.col) 
        or (app.pacman.row==app.clyde.row and app.pacman.col==app.clyde.col)):
        app.isWin=True

def appStarted(app):
    app.isWin=False
    app.numPellets=0
    app.numRows=15
    app.numCols=15
    createBoard(app)
    for row in app.board:
        print(row)
    app.margin=0
    app.cellWidth=(app.width-2*app.margin)/(app.numRows)
    app.cellHeight=(app.height-2*app.margin)/(app.numCols)
    app.timerDelay=85
    app.score=0
    app.pacman=pacChar("yellow","black")
    # Inky, blinky, pinky, and clyde are the ghosts
    app.inky=ghost("cyan","black")
    app.blinky=ghost("red","black")
    app.pinky=ghost("pink","black")
    app.clyde=ghost("orange","black")

def keyPressed(app,event):
    k=event.key
    if k=="Up" or k=="Down" or k=="Left" or k=="Right":
        app.pacman.dir=k
        
def timerFired(app):
    if app.isWin==False:
        app.pacman.moveForward(app)
        randomizeGhostMovement(app)
        moveGhosts(app)
        ghostCollisions(app)
        

def redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="black")
    drawGrid(app,canvas)
    app.pacman.draw(app, canvas)
    drawGhosts(app,canvas)
    if app.isWin:
        canvas.create_text(app.width/2,app.height/2,text="WIN",font="Times 100 bold", fill="white")
    
def drawGrid(app,canvas):
    for row in range(len(app.board)):
        for col in range(len(app.board)):
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