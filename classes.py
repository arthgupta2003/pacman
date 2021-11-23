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
        self.h=abs(row-goalRow)+abs(col-goalCol)
        self.f=self.g+self.h
        self.parent=parent