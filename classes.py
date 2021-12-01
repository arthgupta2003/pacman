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
        if self.row<0 or self.row>app.numRows-1 or self.col<0 or self.col>app.numCols-1 or app.board[self.row][self.col]==1:
            return True
        return False

class pacChar(character):
    def __init__(self,fill,outline,initRow,initCol):
        super().__init__(fill,outline,initRow,initCol)
        self.dir="Up"
        
    def moveForward(self, app):
        super().moveForward(app)
        pacChar.consumePellet(self, app)
        if self.row==14 and self.col==0:
            self.row=14
            self.col=27
            pacChar.consumePellet(self, app)
        elif self.row==14 and self.col==27:
            self.row=14
            self.col=0
            pacChar.consumePellet(self, app)

    def consumePellet(self, app):
        if app.board[self.row][self.col]==2:
            app.board[self.row][self.col]=0
            app.score+=10
            if app.scatterMode==True:
                app.score+=10
            app.numPellets-=1
            if app.numPellets<=0:
                app.isWin=True
        if app.board[self.row][self.col]==3:
            app.scatterMode=True
            app.time=0
            app.board[self.row][self.col]=0
        
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
        self.h=abs(row-goalRow)+abs(col-goalCol)
        self.f=self.g+self.h
        self.parent=parent
        
class Button(object):
    def __init__(self,text,x0,y0,x1,y1,action):
        self.action=(action)
        self.text=text
        self.fill="black"
        self.outline="yellow"
        # x0,y0 are top left coordinates of button
        # x1,y1 are bottom right coordinates of button
        self.x0=x0
        self.y0=y0
        self.x1=x1
        self.y1=y1
        
    def isPressed(self,eventX,eventY):
        if eventX>=self.x0 and eventX<=self.x1 and eventY>=self.y0 and eventY<=self.y1:
            return True
        else:
            return False


