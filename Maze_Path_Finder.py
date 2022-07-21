import random
import turtle


def listsum(input):
    my_sum = 0
    for row in input:
        my_sum += sum(row)
    return my_sum

def mazegenerate(sizex,sizey):
    Walls=[[[1,1,1,1] for a in range(sizex)] for b in range(sizey)]
    x=0
    y=0
    visitsum=0
    currentnode=[x,y]
    visited=[[0 for a in range(sizex)] for b in range(sizey)]
    visited[x][y]=1
    visitn=[[x,y]]
    n=0
    while visitsum!=(sizex*sizey):#check to see if finished
        options=[0,0,0,0]
        if x!=0:
            if visited[y][x-1]==0:
                options[0]=1
                #wall can be removed on the left
        if y!=sizey-1:
            if visited[y+1][x]==0:
                options[1]=1
                #wall can be removed above
        if x!=sizex-1:
            if visited[y][x+1]==0:
                options[2]=1
                #wall can be removed on the right
        if y!=0:
            if visited[y-1][x]==0:
                options[3]=1
                #wall can be removed below
        
        if options==[0,0,0,0]:
            currentnode=visitn[n-1]
            x=currentnode[0]
            y=currentnode[1]
            n=n-1
            #moves back to previous square/node
        else:
            nodefound=False
            while nodefound==False:
                randomint=random.randint(0,3)
                if options[randomint]==1:
                    if randomint==0:
                        oppisitenode=[currentnode[0]-1,currentnode[1]]#moves into cell on the left
                        Walls[currentnode[1]][currentnode[0]][0]=0#removing wall left
                        Walls[oppisitenode[1]][oppisitenode[0]][2]=0
                    elif randomint==1:
                        oppisitenode=[currentnode[0],currentnode[1]+1]#moves into cell above
                        Walls[currentnode[1]][currentnode[0]][1]=0#removing wall above
                        Walls[oppisitenode[1]][oppisitenode[0]][3]=0
                    elif randomint==2:
                        oppisitenode=[currentnode[0]+1,currentnode[1]]#moves into cell on the right
                        Walls[currentnode[1]][currentnode[0]][2]=0#removing wall right
                        Walls[oppisitenode[1]][oppisitenode[0]][0]=0
                    else:
                        oppisitenode=[currentnode[0],currentnode[1]-1]#moves into cell below
                        Walls[currentnode[1]][currentnode[0]][3]=0#removing wall below
                        Walls[oppisitenode[1]][oppisitenode[0]][1]=0
                    n=n+1
                    visitn.insert(n,oppisitenode)
                    currentnode=oppisitenode
                    visited[currentnode[1]][currentnode[0]]=1
                    x=currentnode[0]
                    y=currentnode[1]
                    nodefound=True
        visitsum=listsum(visited)
    return(Walls)

def printmaze(sizex,sizey,Walls):
    startx=-380
    starty=-startx
    gridsize=(2*(-startx))/sizex
    turtle.clear()
    turtle.speed(0)
    turtle.penup()
    turtle.goto(startx,starty)
    turtle.pendown()
    turtle.goto(-startx,starty)
    turtle.goto(-startx,-starty)
    turtle.setheading(0)
    for y in range(sizex):
        turtle.penup()
        turtle.goto(startx,-starty+gridsize*(y))
        for x in range(sizey):
            if Walls[y][x][3]==1:
                turtle.pendown()
            else:
                turtle.penup()
            turtle.forward(gridsize)
    turtle.left(90)
    for x in range(sizex):
        turtle.penup()
        turtle.goto(startx+gridsize*(x),-starty)
        for y in range(sizey):
            if Walls[y][x][0]==1:
                turtle.pendown()
            else:
                turtle.penup()
            turtle.forward(gridsize)






def oppisitenode(b,currentnode):
    if b==0:
        oppisitenode=[currentnode[0]-1,currentnode[1]]
    elif b==1:
        oppisitenode=[currentnode[0],currentnode[1]+1]
    elif b==2:
        oppisitenode=[currentnode[0]+1,currentnode[1]]
    else:
        oppisitenode=[currentnode[0],currentnode[1]-1]
    return(oppisitenode)

def Dijkstrasearch(Walls,sizey,sizex):
    visited=[[0 for a in range(sizex)] for b in range(sizey)]
    visited[0][0]=1#starts bottom left with 1
    currentnodes=[[0,0]]
    new=True
    while new==True:
        new=False
        for a in range(len(currentnodes)):#searches at all current nodes/squares
            currentnode=currentnodes[0]
            for b in range(4):#checks all 4 possible directions
                if Walls[currentnode[1]][currentnode[0]][b]==0:#check for wall
                    nodeotherside=oppisitenode(b,currentnode)
                    if visited[nodeotherside[1]][nodeotherside[0]]==0:#check if hasnt been visited
                        visited[nodeotherside[1]][nodeotherside[0]]=visited[currentnode[1]][currentnode[0]]+1
                        currentnodes.append(nodeotherside)#adds the new node to the list of nodes curently at
                        new=True
                        dotatxy(nodeotherside[0],nodeotherside[1],gridsize,-380,-380,sizex,visited[currentnode[1]][currentnode[0]]+1)
            currentnodes.remove(currentnode)#removes the node previously at because it has been searched
    return(visited)

def Dijkstraroute(visited,sizex,sizey,Walls):
    distance=visited[sizex-1][sizey-1]
    routecoordinates=[[sizex-1,sizey-1]]#sets finish to top right
    while routecoordinates[0]!=[0,0]:
        if Walls[routecoordinates[0][1]][routecoordinates[0][0]][0]==0:#backtracks by looking at each square and chosing the correct one to go in so no wall and distance=distance-1
            if visited[routecoordinates[0][1]][routecoordinates[0][0]-1]==distance-1:
                routecoordinates.insert(0,[routecoordinates[0][0]-1,routecoordinates[0][1]])
                distance=distance-1
        if Walls[routecoordinates[0][1]][routecoordinates[0][0]][1]==0:
            if visited[routecoordinates[0][1]+1][routecoordinates[0][0]]==distance-1:
                routecoordinates.insert(0,[routecoordinates[0][0],routecoordinates[0][1]+1])
                distance=distance-1
        if Walls[routecoordinates[0][1]][routecoordinates[0][0]][2]==0:
            if visited[routecoordinates[0][1]][routecoordinates[0][0]+1]==distance-1:
                routecoordinates.insert(0,[routecoordinates[0][0]+1,routecoordinates[0][1]])
                distance=distance-1
        if Walls[routecoordinates[0][1]][routecoordinates[0][0]][3]==0:
            if visited[routecoordinates[0][1]-1][routecoordinates[0][0]]==distance-1:
                routecoordinates.insert(0,[routecoordinates[0][0],routecoordinates[0][1]-1])
                distance=distance-1
    return(routecoordinates)

def displayroute(routecoordinates,startx,starty,gridsize):
    turtle.speed(0)
    turtle.penup()
    x=startx+gridsize/2
    y=starty+gridsize/2
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pensize(gridsize/2)
    turtle.color("red")
    for a in range(len(routecoordinates)-1):
        x=x+(routecoordinates[a+1][0]-routecoordinates[a][0])*gridsize
        y=y+(routecoordinates[a+1][1]-routecoordinates[a][1])*gridsize
        turtle.goto(x,y)

def dotatxy(x,y,gridsize,startx,starty,sizex,colour):
    turtle.penup()
    turtle.goto(startx+gridsize/2+x*gridsize,starty+gridsize/2+y*gridsize)
    turtle.pendown()
    turtle.pencolor((0,0.99-colour/(sizex*sizex),0))
    turtle.pensize(gridsize/2)
    turtle.forward(1)


    

sizex=15
sizey=15
startx=-380
starty=startx
gridsize=(2*(-starty))/sizey
Walls=mazegenerate(sizex,sizey)
printmaze(sizex,sizey,Walls)
visited=Dijkstrasearch(Walls,sizey,sizex)
routecoordinates=Dijkstraroute(visited,sizex,sizey,Walls)
input()
displayroute(routecoordinates,startx,starty,gridsize)
