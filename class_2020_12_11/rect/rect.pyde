x0 = 20
y0 = 20
Color = 10
stepX = 70
stepY = 70
SetCondition = 2  # 1-line, 2-rect, 3-ellipse
def setup():
    size(360, 360)
    stroke(0)
    background(0, 190, 0)

   
    
    
def draw():
    global Color
    #colorMode(RGB, 255)
    for y in range(x0,360,stepY):
        for x in range(y0,360,stepX):
            fill(Color,Color%255,Color%255)
            if SetCondition==1:
                rect(x, y, 3, 40)
            elif SetCondition==2:
                rect(x, y, 40, 40)
            else:
                ellipse(x, y, 40, 40)
            Color +=10
    
