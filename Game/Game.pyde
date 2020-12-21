def Win():
    size(1000,600)
    stroke(245,182,96)
    fill(90,255,253)
    rect(280,200,440,200)
    noStroke()
    fill(255,0,0)
    circle(360,340,90)
    fill(0,255,0)
    circle(640,340,90)
    fill(2,1,255)
    textSize(52)
    text("You Win. Again?", 300, 270)
    text("N", 340, 360)
    text("Y", 625, 360)
    
    
    
def Inception():
    global i,vel_G,FonGeneral,Mill,Gear1,Gear2,Gear3,FonBehinde,radius,Black,Red,location,velocity,gravitation,radius,flag
    i=0
    vel_G=0       
    location = PVector(245,365)
    velocity = PVector(0,0)
    gravitation = PVector(0,3)
    flag=0
    stroke(0)
    fill(100)
    circle(location.x,location.y,radius*2)
    loop()
    

def Game_Over():
    size(1000,600)
    stroke(245,182,96)
    fill(90,255,253)
    rect(300,200,400,200)
    noStroke()
    fill(255,0,0)
    circle(360,340,90)
    fill(0,255,0)
    circle(640,340,90)
    fill(2,1,255)
    textSize(52)
    text("Again?", 420, 270)
    text("N", 340, 360)
    text("Y", 625, 360)


def Loading_Background():
    
    global i,vel_G,FonGeneral,FonGeneral2,Mill,Gear1,Gear2,Gear3,FonBehinde,FonBehinde2,Gear4,Gear5,Gear6
    background(100,200,50)   
    imageMode(CORNER)
    image(FonBehinde,-100-vel_G/2,0)
    image(FonBehinde2,1800-vel_G/2,0)
    
    push()
    translate(4700-vel_G,0)
    imageMode(CENTER)
    rotate(radians(i*2)%360)
    image(Gear4,0,0)
    pop()
    push()
    translate(4150-vel_G,0)
    imageMode(CENTER)
    rotate(radians(i*2)%360)
    image(Gear5,0,0)
    pop()
    push()
    translate(4580-vel_G,580)
    imageMode(CENTER)
    rotate(radians(i*2)%360)
    image(Gear6,0,0)
    pop()
    
    imageMode(CORNER)
    image(FonGeneral,-vel_G,0) 
    image(FonGeneral2,3500-vel_G,0) 
       
    push()
    translate(1200-vel_G,560)
    imageMode(CENTER)
    rotate(radians(-i)%360)
    image(Mill,0,0)
    pop()
    push()
    translate(1450-vel_G,40)
    imageMode(CENTER)
    rotate(radians(i)%360)
    image(Gear1,0,0)
    pop()    
    push()
    translate(1950-vel_G,300)
    imageMode(CENTER)
    rotate(radians(i)%360)
    image(Gear2,0,0)
    pop()
    push()
    translate(2765-vel_G,310)
    imageMode(CENTER)
    rotate(radians(i)%360)
    image(Gear3,0,0)
    pop()
    
    
    vel_G+=2
    i+=0.5    
    

    


 
def setup():
    global i,vel_G,FonGeneral,FonGeneral2,Mill,Gear1,Gear2,Gear3,FonBehinde,radius,Black,Red,location,velocity,gravitation,radius,flag,Gear4,FonBehinde2,Gear5,Gear6
    Mill=loadImage("mill.png")
    FonGeneral=loadImage("fonGeneral.png")
    FonGeneral2=loadImage("fonGeneral2.png")
    Gear1=loadImage("gear1.png")
    Gear2=loadImage("gear2.png")
    Gear3=loadImage("gear3.png")
    Gear4=loadImage("gear4.png")
    Gear5=loadImage("gear5.png")
    Gear6=loadImage("gear6.png")
    FonBehinde=loadImage("fonBehinde.png")
    FonBehinde2=loadImage("fonBehinde2.png")
    i=0
    vel_G=0
    size(1000,600)
    Black = color(0,0,0)
    Red = color(255,0,0)
    frameRate(29)
    location = PVector(240,365)
    velocity = PVector(0,0)
    gravitation = PVector(0,3)
    radius=20
    flag=0
    Loading_Background()
    fill(20,254,100)
    circle(location.x,location.y,radius*2)
    

        
def draw(): 
    global location,velocity,gravitation,radius,flag,vel_G
    if(flag==1):    
        Loading_Background()
        location.add(velocity+gravitation)
        gravitation *=1.03
        velocity.y*=0.9
        velocity.x*=0.9
        fill(20,254,100)
        circle(location.x,location.y,radius*2)  
        
            
        if(location.x<0 or location.x>width or location.y<0 or location.y>height):
            noLoop()
            Game_Over()
        if(color(0)==get((int)(location.x+radius+1),(int)(location.y)) and color(0)==get((int)(location.x-radius-1),(int)(location.y))):
            noLoop()
            Game_Over()
        if(color(255,0,0)==get((int)(location.x+radius+1),(int)(location.y)) or color(255,0,0)==get((int)(location.x-radius-1),(int)(location.y))):
            noLoop()
            Game_Over()
        if(color(255,0,0)==get((int)(location.x),(int)(location.y+radius+1)) or color(255,0,0)==get((int)(location.x),(int)(location.y-radius-1))):
            noLoop()
            Game_Over()
            
        if(location.y<250 and vel_G>6500):
            noLoop()
            Win()
        
        if(color(0)==get((int)(location.x+radius+1),(int)(location.y))):
            velocity.x = -2
        if(color(0)==get((int)(location.x-radius-1),(int)(location.y))):
            velocity.x = 2
        if(color(0)==get((int)(location.x),(int)(location.y-radius-1))):
            gravitation.y=2
            velocity.y=0
        if( color(0)==get((int)(location.x),(int)(location.y+radius+1))):
            gravitation.y=1
            velocity.y=-4
            
    elif keyPressed == True:
            flag = 1 
            
            
def keyPressed():
    global i,vel_G,FonGeneral,Mill,Gear1,Gear2,Gear3,FonBehinde,radius,Black,Red,location,velocity,gravitation,radius,flag
    if (keyCode==38 and (color(0)!=get((int)(location.x),(int)(location.y-radius-1)))):
        velocity.y=-5
        gravitation.y=1    
    if (keyCode==39 and (color(0)!=get((int)(location.x+radius+1),(int)(location.y)))):
        velocity.x=3
    if (keyCode==37 and (color(0)!=get((int)(location.x-radius-1),(int)(location.y)))):
        velocity.x=-5
    if (keyCode==78):
        exit()
    if (keyCode==89):
        Inception()
