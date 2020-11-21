
size(360, 360)
noStroke()
background(200, 250, 50)
inside = color(0, 190, 0)

# These statements are equivalent to the statements above.
# Programmers may use the format they prefer.
#inside = 0xCC6600
#middle = 0xCC9900
#outside = 0x993300
with pushMatrix():
    translate(80, 80)
    
    fill(inside)
    rect(50, 50, 110, 110)
