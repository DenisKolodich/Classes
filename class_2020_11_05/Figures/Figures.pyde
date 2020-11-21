Length = 360
Width = 360
LenSquare = 40 
i=0
nX = 5 # количество квадратов по строке
nY = 5 # количество квадратов в столбце
LengX = nX*LenSquare
LengY = nY*LenSquare
IntervalX = (Length-LengX)/(nX+1)
IntervalY = (Width-LengY)/(nY+1)
inside = color(70, 190, 200)
SetCondition = 2 # 1-line, 2-rect, 3-ellipse

def setup():
    global Lenght,Width,SetCondition
    size(Length, Width)
    background(0, 190, 0)
    frameRate(1)

    
def draw():
    background(0, 190, 0)
    global inside, SetCondition,IntervalX,IntervalX,LenSquare,i
    SetCondition = i%3
    i+=1
    fill(inside)
    for y in range(IntervalY,Length-IntervalY,IntervalY+LenSquare):
        for x in range(IntervalY,Width-IntervalY,IntervalX+LenSquare):
            if SetCondition==0:
                rect(x, y, 3, LenSquare)
            elif SetCondition==1:
                rect(x, y, LenSquare, LenSquare)
            elif SetCondition==2:
                circle(x+LenSquare/2, y+LenSquare/2, LenSquare)
