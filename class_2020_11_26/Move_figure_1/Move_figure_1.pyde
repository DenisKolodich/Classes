radius = 50
Col = color(100,50,250)
width = 360
length = 360
def setup():
    global length,width
    size(width, length)
    frameRate(30)
    
   
    
def draw():
    global radius,Col
    background(100, 200, 200)
    fill(Col)
    stroke(100)
    circle(mouseX,mouseY,radius)
def mouseClicked():
    global Col
    Col = color(random(255),random(255),random(255))
    
    
def keyPressed():
    if(keyCode==32):
        fill(random(255),random(255),random(255))
        stroke(random(255),random(255),random(255))
        circle(width-(random(width)),length-(random(length)),radius)
        
    
        
       
