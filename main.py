import random
from cmu_112_graphics import *
from classes import *
import copy

def appStarted(app):    
    # Title screen
    app.gameOver=False
    app.isWin=False
    app.numLives=3
    app.score=0
    app.mode="title"
    app.scatterMode=False #for powerups
    # In the board:
    # 0=Empty Cell
    # 1=Wall
    # 2=Pellet
    # 3=Power-Up
    app.staticBoard=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1], [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1], [1, 2, 2, 3, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 3, 2, 2, 1], [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1], [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1], [1, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
    app.numPellets=343
    app.board=copy.deepcopy(app.staticBoard)
    app.logo= app.loadImage('images/LOGO.png')
    app.staticMazeButton=Button("Classic \nMode",250,400,380,500,resetGameConditions)
    app.dynamicMazeButton=Button("Random \nMode",420,400,550,500,generateAndSetRandomBoard)
    app.buttons=[app.staticMazeButton,app.dynamicMazeButton]
    resetGameConditions(app)

def game_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="black")
    drawGrid(app,canvas)
    drawGhosts(app,canvas)
    drawCharacter(app,canvas,app.pacman)
    if app.gameOver:
        canvas.create_rectangle(app.width/2-200,app.height/2-200,app.width/2+200,app.height/2+200,fill="black",outline="white")
        canvas.create_text(app.width/2,app.height/2,text=f"  GAME \n  OVER\nScore:{app.score}",font="Courier 60 bold", fill="white")
        return
    if app.isWin:
        canvas.create_rectangle(app.width/2-200,app.height/2-200,app.width/2+200,app.height/2+200,fill="black",outline="white")
        canvas.create_text(app.width/2,app.height/2,text=f"YOU \nWIN \nScore:{app.score}",font="Courier 60 bold", fill="white")
    
def game_keyPressed(app,event):
    k=event.key
    if k=="Up" or k=="Down" or k=="Left" or k=="Right":
        app.pacman.dir=k
    if k=="r":
        appStarted(app)

def game_timerFired(app):
    if app.scatterMode==False:
        if app.gameOver==True:
            return
        app.time+=1
        if app.time%8==0:
            resetPathFinding(app)
            if app.isHit==True:
                resetGameConditions(app)
        if app.isWin==False and app.isHit==False:
            moveGhosts(app)
            ghostCollisions(app)
            if app.isHit==False:
                app.pacman.moveForward(app)
                ghostCollisions(app)
                
    elif app.scatterMode==True:
        # Activates when pac-man eats powerup
        if app.time<=25:
            app.time+=1
            randomizeGhostMovement(app)
            ghostCollisions(app)
            app.pacman.moveForward(app)
            ghostCollisions(app)
        else:
            app.scatterMode=False
            resetPathFinding(app)
            
def generateAndSetRandomBoard(app):
    resetGameConditions(app)
    # Reset board
    for r in range(app.numRows):
        for c in range(app.numCols):
            app.board[r][c]=1
            
    # Using Randomized Prim's algorithm (described in: https://en.wikipedia.org/wiki/Maze_generation_algorithm)
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
            app.board[parentRow][parentCol]=2
            for child in children:
                openList.add(child)
        openList.remove((parentRow,parentCol))    
        
    # Cleans up dead ends
    for x in range(2):
        for r in range(app.numRows):
            for c in range(app.numCols):
                parentRow,parentCol=r,c
                neighboringPaths=0
                if app.board[parentRow][parentCol]==2:
                    for drow,dcol in [(1,0),(0,1),(-1,0),(0,-1)]:
                        newRow=drow+parentRow
                        newCol=dcol+parentCol
                        if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1:
                            continue
                        if app.board[newRow][newCol]==2:
                            neighboringPaths+=1
                    if neighboringPaths==1:
                        app.board[parentRow][parentCol]=1    
    
    #Get rids to random holes in maze that cannot be reached
    for r in range(app.numRows):
        for c in range(app.numCols):
            parentRow,parentCol=r,c
            neighboringPaths=0
            if app.board[parentRow][parentCol]==2:
                for drow,dcol in [(1,0),(0,1),(-1,0),(0,-1)]:
                    newRow=drow+parentRow
                    newCol=dcol+parentCol
                    if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1:
                        continue
                    if app.board[newRow][newCol]==2:
                        neighboringPaths+=1
                if neighboringPaths==0:
                    app.board[parentRow][parentCol]=1    
      
    # Clean up border
    for r in range(app.numRows):
        for c in range(app.numCols):
            if r==1 or c==1 or r==app.numRows-2 or c==app.numCols-2:
                app.board[r][c]=2
            if r==0 or c==0 or r==app.numRows-1 or c==app.numCols-1:
                app.board[r][c]=1
            
    #Adds some holes to map between valid paths
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
                    if app.board[newRow][newCol]==2:
                        neighboringPaths+=1
                if neighboringPaths>=2:
                    app.board[parentRow][parentCol]=1
    
    
    # Add ghost box:
    for i in range(11,19):
        for j in range(9,19):
            app.board[i][j]=app.staticBoard[i][j]
             
    # Add powerups
    quads=[(0,0,app.numRows//2,app.numCols//2),(0,app.numCols//2,app.numRows//2,app.numCols),(app.numRows//2,0,app.numRows,app.numCols//2),(app.numRows//2,app.numCols//2,app.numRows,app.numCols)]
    for r0,c0,r1,c1 in quads:
        while True:    
            a=random.randrange(r0,r1)
            b=random.randrange(c0,c1)
            if app.board[a][b]==2:
                app.board[a][b]=3
                break
    
    # Add wraparound tunnels
    app.board[14][0]=2
    app.board[14][27]=2

    # Finally, count the number of pellets to track win condition
    app.pellets=0
    for r in app.board:
        app.pellets+=r.count(2)
    
def resetGameConditions(app):
    app.isWin=False
    app.isHit=False   
    app.time=0
    app.numRows=28
    app.numCols=28
    app.margin=0
    app.cellWidth=(app.width-2*app.margin)/(app.numRows)
    app.cellHeight=(app.height-2*app.margin)/(app.numCols)
    app.timerDelay=150
    app.pacman=pacChar("yellow","black",17,13)
    
    # Inky, blinky, pinky, and clyde are the ghosts
    app.inky=ghost("cyan","black",13,14)
    app.blinky=ghost("red","black",14,14)
    app.pinky=ghost("pink","black",14,13)
    app.clyde=ghost("orange","black",13,13)
    app.ghosts=[app.inky,app.blinky,app.pinky,app.clyde]
    resetPathFinding(app) #to initialize paths
 
def drawCharacter(app,canvas,charObj):
    x,y=convertRowColToCoordinates(app,charObj.row+0.5,charObj.col+0.5)
    x+=app.margin
    y+=app.margin
    r= app.cellWidth/2
    if app.scatterMode==False or charObj==app.pacman:
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=charObj.fill,outline=charObj.outline)
    elif app.scatterMode==True:
        canvas.create_oval(x-r,y-r,x+r,y+r,fill="magenta",outline="magenta")

def aStarSearch(app,startRow,startCol,endRow,endCol):
    # Pathfinding using A*(logic from:https://www.geeksforgeeks.org/a-search-algorithm/)
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
    
    # In case no path found, pathfind to ghost box
    return aStarSearch(app,startRow,startCol,13,14)

def convertRowColToCoordinates(app,row,col):
    return col*app.cellWidth,row*app.cellHeight

def moveGhosts(app):    
    for ghost in app.ghosts:
        if len(ghost.path)==0:
            resetPathFinding(app)
        ghost.row=ghost.path[0][0]
        ghost.col=ghost.path[0][1]
        ghost.path.pop(0)

def drawGhosts(app,canvas):
    for ghost in app.ghosts:
        drawCharacter(app,canvas,ghost)
    
def ghostCollisions(app):
    if app.scatterMode==False:
        if ((app.pacman.row==app.inky.row and app.pacman.col==app.inky.col) 
            or (app.pacman.row==app.blinky.row and app.pacman.col==app.blinky.col) 
            or (app.pacman.row==app.pinky.row and app.pacman.col==app.pinky.col) 
            or (app.pacman.row==app.clyde.row and app.pacman.col==app.clyde.col)):
            app.isHit=True
            app.numLives-=1
            if app.numLives<=0:
                app.gameOver=True    
    elif app.scatterMode==True:
        for ghost in app.ghosts:
            if app.pacman.row==ghost.row and app.pacman.col==ghost.col:
                app.score+=50
                ghost.row=13
                ghost.col=14
                
def resetPathFinding(app):
    # Source: https://gameinternals.com/understanding-pac-man-ghost-behavior
    # Blinky pathfinds to pac-man's location
    app.blinky.path=aStarSearch(app,app.inky.row,app.inky.col,app.pacman.row,app.pacman.col)
    

    # Inky pathfinds to random tile near pac-man
    while True:
        drow=random.randrange(-3,4)
        dcol=random.randrange(-3,4)
        newRow=app.pacman.row+drow
        newCol=app.pacman.col+dcol
        if newRow<0 or newRow>app.numRows-1 or newCol<0 or newCol>app.numCols-1 or app.board[newRow][newCol]==1:
            continue
        app.inky.path=aStarSearch(app,app.inky.row,app.inky.col,newRow,newCol)
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
        app.pinky.path=aStarSearch(app,app.pinky.row,app.pinky.col,newRow,newCol)
        break
        
        
    # Clyde pathfinds to pacman when he is far from pac-man, when he is close he pathfinds to bottom corner
    clydeTargetRow,clydeTargetCol=bottomRightCorner(app)  
    clydeDistanceFromPacman= ((app.pacman.row-app.clyde.row)**2+(app.pacman.col-app.clyde.col)**2)**0.5
    if clydeDistanceFromPacman<=8:
        app.clyde.path=aStarSearch(app,app.clyde.row,app.clyde.col,clydeTargetRow,clydeTargetCol)
    else:
        app.clyde.path=aStarSearch(app,app.clyde.row,app.clyde.col,app.pacman.row,app.pacman.col)
    
    
def drawGrid(app,canvas,gridColor="blue"):
    if app.scatterMode==True:
        gridColor="green"
    for row in range(app.numRows):
        for col in range(app.numCols):
            if app.board[row][col]==1:
                # wall
                x,y=convertRowColToCoordinates(app,row,col)
                x+=app.margin
                y+=app.margin
                canvas.create_rectangle(x,y,x+app.cellWidth,y+app.cellHeight,fill=gridColor,outline="dark "+gridColor)
            elif app.board[row][col]==2:
                # pellet
                x,y=convertRowColToCoordinates(app,row+0.5,col+0.5)
                x+=app.margin
                y+=app.margin
                r=app.cellWidth/6
                canvas.create_oval(x-r,y-r,x+r,y+r,fill="yellow")
            elif app.board[row][col]==3:
                # power-up
                if app.time//3%2==0: #conditional makes powerup blink
                    x,y=convertRowColToCoordinates(app,row+0.5,col+0.5)
                    x+=app.margin
                    y+=app.margin
                    r=app.cellWidth/3
                    canvas.create_oval(x-r,y-r,x+r,y+r,fill="yellow")

    canvas.create_rectangle(0,0,app.width,16,fill="blue")
    canvas.create_text(app.width/2,16,fill="White",text=f"Score:{app.score}",font="Courier 16 bold")
    canvas.create_text(app.width/1.05,16,fill="White",text=f"Lives:{app.numLives}",font="Courier 16 bold")
    
def randomizeGhostMovement(app):
    import random
    directions= ["Left","Right","Down","Up"]
    for ghost in app.ghosts:
        ghost.dir=directions[random.randrange(0,4)]
        ghost.moveForward(app)
    
def title_redrawAll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill="black")
    canvas.create_image(app.width/2,app.height/3, image=ImageTk.PhotoImage(app.logo))
    canvas.create_text(app.width/2,app.height-50,fill="white",text="Made by Arth Gupta\n15-112 Term Project",font="Times 16")
    for button in app.buttons:
        canvas.create_rectangle(button.x0-20,button.y0,button.x1,button.y1,fill=button.fill,outline=button.outline)
        canvas.create_text((button.x0+button.x1)/2,(button.y0+button.y1)/2,text=button.text,fill="white",font="Courier 24")
        
def title_mousePressed(app,event):
    for button in app.buttons:
        if button.isPressed(event.x,event.y):
            button.action(app)
            app.mode="game"

def bottomRightCorner(app):
    for r in range(app.numRows,-1,-1):
        for c in range(app.numCols):
            if app.board[r][c]!=1:
                return (r,c)

runApp(width=800,height=800)
