speed = 4
X=50
Y=50
radius = 50
width = 360
length = 360
def setup():
    global length,width
    size(width, length)
    frameRate(30)
    
   
    
def draw():
    global radius,X,Y,speed
    background(100, 200, 200)
    fill(100,50,250)
    stroke(100)
    circle(X,Y,radius)
    
def keyPressed():
    global X,Y,speed
    if(keyCode==39):
        X+=speed
    if(keyCode==37):
        X-=speed
    if(keyCode==40):
        Y+=speed
    if(keyCode==38):
        Y-=speed
        
        
    
        
       
