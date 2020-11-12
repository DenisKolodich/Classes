def setup():
    x0 = 20
    y0 = 20
    stepX = 60
    stepY = 70
    size(360, 360)
    background(0, 190, 0)
    inside = color(70, 190, 200)
    SetCondition = 2 # 1-line, 2-rect, 3-ellipse
#def draw():
    fill(inside)
    for y in range(x0,360,stepY):
        for x in range(y0,360,stepX):
            if SetCondition==1:
                rect(x, y, 3, 40)
            elif SetCondition==2:
                rect(x, y, 40, 40)
            else:
                ellipse(x, y, 40, 40)
    
