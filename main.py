from cmu_112_graphics import *

class pacChar():
    def __init__(self):
        self.dir="Right"
        self.col=2
        self.row=2
    
    def moveForward(self, app):
        if app.isWin:
            return
        if self.dir=="Right":
            self.col+=1
            if pacChar.invalidMove(self,app):
                self.col-=1
        elif self.dir=="Left":
            self.col-=1
            if pacChar.invalidMove(self,app):
                self.col+=1
        elif self.dir=="Up":
            self.row-=1
            if pacChar.invalidMove(self,app):
                self.row+=1
        elif self.dir=="Down":
            self.row+=1
            if pacChar.invalidMove(self,app):
                self.row-=1
        pacChar.consumePellet(self, app)
        
        
    def consumePellet(self, app):
        if app.board[self.row][self.col]==2:
            app.board[self.row][self.col]=0
            app.score+=1
            app.numPellets-=1
            if app.numPellets<=0:
                app.isWin=True
            
    def invalidMove(self,app):
        if self.row<1 or self.row>app.numRows-2 or self.col<1 or self.col>app.numCols-2 or app.board[self.row][self.col]==1:
            return True
        return False
    
    def draw(self,app, canvas):
        print(self.row,self.col)
        x,y=convertRowColToCoordinates(app, self.row+0.5,self.col+0.5)
        x+=app.margin
        y+=app.margin
        r= app.cellWidth/2
        canvas.create_oval(x-r,y-r,x+r,y+r,fill="yellow",outline="black")
        
class ghost():
    def __init__(self):
        pass

def createBoard(app):
    app.board=[]
    for row in range(app.numRows):
        currentRow=[]
        for col in range(app.numCols):
            if row==0 or col==0 or row==app.numRows-1 or col==app.numCols-1:
                # 1=wall
                currentRow.append(1)
            elif row%6==2 or col%6==2:
                # 2=pellet
                currentRow.append(2)
                app.numPellets+=1
            elif row%6==1 or row%6==3 or col%6==1 or col%6==3:
                # 0=empty cell
                currentRow.append(0)
            else:
                # 1=wall
                currentRow.append(1)
        app.board.append(currentRow)

def convertRowColToCoordinates(app, row,col):
    return col*app.cellWidth,row*app.cellHeight

def appStarted(app):
    app.isWin=False
    app.numPellets=0
    app.numRows=10
    app.numCols=10
    createBoard(app)
    for row in app.board:
        print(row)
    app.margin=0
    app.cellWidth=(app.width-2*app.margin)/(app.numRows)
    app.cellHeight=(app.height-2*app.margin)/(app.numCols)
    app.timerDelay=85
    app.score=0
    app.pacman=pacChar()
    # Inky, blinky, pinky, and clyde are the ghosts
    app.inky=ghost()
    app.blinky=ghost()
    app.pinky=ghost()
    app.clyde=ghost()

def keyPressed(app,event):
    k=event.key
    if k=="Up" or k=="Down" or k=="Left" or k=="Right":
        app.pacman.dir=k
        
def timerFired(app):
    app.pacman.moveForward(app)

def redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="black")
    drawGrid(app,canvas)
    app.pacman.draw(app, canvas)
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