Col=200
radius = 50
x = radius/2
y=radius/2
flagX = False
flagY = False
def setup():
    size(360, 360)
    frameRate(30)
    
   
    
def draw():
    global x,y, flagX, flagY,radius,Col
    background(100, 100, 200)
    if(x>=width-radius/2):
        flagX= True
        Col = color(random(255),random(255),random(255))
    if(y>=height-radius/2):
        flagY= True
        Col = color(random(255),random(255),random(255))
    if(x<=radius/2):
        flagX= False
        Col = color(random(255),random(255),random(255))
    if(y<=radius/2):
        flagY= False
        Col = color(random(255),random(255),random(255))
        
                
    if(not(flagX)):
        x+=7
    if(not(flagY)):
        y+=5
    if(flagX):
        x-=7
    if(flagY):
        y-=5

        
    fill(Col)
    circle(x,y,radius)
    
        
       
