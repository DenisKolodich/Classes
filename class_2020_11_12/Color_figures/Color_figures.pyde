Length = 360
Width = 360
LenSquare = 50 
i=0
nX = 5 # количество квадратов по строке
nY = 5 # количество квадратов в столбце

LengX = nX*LenSquare
LengY = nY*LenSquare
IntervalX = (Length-LengX)/(nX+1)
IntervalY = (Width-LengY)/(nY+1)
SetCondition = 2 # 1-line, 2-rect, 3-ellipse
N = nY*nX

def setup():
    global Lenght,Width,SetCondition
    size(Length, Width)
    background(0, 190, 0)
    frameRate(2)
    colorMode(RGB, Width);

    
def draw():
   
    background(Width/4, Width/2, Width/2)
    global inside, SetCondition,IntervalX,IntervalX,LenSquare,i
    SetCondition = i%3
    i+=1
    N=nY*nX
    t=Width/N-1
    for y in range(IntervalY,Length-IntervalY,IntervalY+LenSquare):
        for x in range(IntervalY,Width-IntervalY,IntervalX+LenSquare):
            if SetCondition==0:
                fill(N/3,N/2,N)
                rect(x, y, 3, LenSquare)
                N+=t
                print(N,N,N)
            elif SetCondition==1:
                fill(N/3,N/2,N)
                rect(x, y, LenSquare, LenSquare)
                N+=t
            elif SetCondition==2:
                fill(N/3,N/2,N)
                circle(x+LenSquare/2, y+LenSquare/2, LenSquare)
                N+=t
