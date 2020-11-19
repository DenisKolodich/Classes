
radius = 30
x = radius/2
y=radius/2
flagX = False
flagY = False
def setup():
    size(360, 360)
    frameRate(30)
   
    
def draw():
    global x,y, flagX, flagY,radius
    background(100, 100, 200)
    if(x>=width-radius/2):
        flagX= True
    if(y>=height-radius/2):
        flagY= True
    if(x<=radius/2):
        flagX= False
    if(y<=radius/2):
        flagY= False
        
                
    if(not(flagX)):
        x+=7
    if(not(flagY)):
        y+=5
    if(flagX):
        x-=7
    if(flagY):
        y-=5

        
    fill(200)
    circle(x,y,radius)
    
        
       
