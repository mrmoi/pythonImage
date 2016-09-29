import turtle
from math import sqrt

# Create class Structure
# Inherit from turtle class
class Structure(turtle.Turtle):
    def __init__(self):
        super(Structure, self).__init__()

    # method to create rectangular building
    def rectangularbuilding(self, height, width, color, x, y):
        n = turtle.Turtle()
        n.speed(10)
        n.goto(x, y)
        n.pendown()
        n.begin_fill()
        n.fillcolor(color)
        n.left(90)
        n.forward(height)
        n.right(90)
        n.forward(width)
        n.right(90)
        n.forward(height)
        n.right(90)
        n.forward(width)
        n.end_fill()
        n.penup()
        n.home()

    def trianglebuilding(self, width,  color, x, y):
        a = turtle.Turtle()
        a.speed(10)
        a.goto(x, y)
        a.pendown()
        a.begin_fill()
        a.fillcolor(color)
        a.forward(width)
        a.left(120)
        a.forward(width)
        a.left(120)
        a.forward(width)
        a.right(120)
        #a.forward(width)
        a.end_fill()
        a.penup()
        a.home()

    def triangleroofbuilding(self, height, width, color, x, y):
        b = turtle.Turtle()
        b.speed(10)
        b.goto(x, y)
        b.pendown()
        b.begin_fill()
        b.fillcolor(color)
        b.forward(width)
        b.left(90)
        b.forward(height)
        b.left(60)
        b.forward(width / 2)
        b.left(60)
        b.forward(width / 2)
        b.left(60)
        b.forward(height)
        b.end_fill()
        b.penup()
        b.home()

    def stepbuilding(self, height, width, color, x, y):
        b = turtle.Turtle()
        b.speed(10)
        b.goto(x, y)
        b.pendown()
        b.begin_fill()
        b.fillcolor(color)
        b.forward(width)
        b.left(90)
        b.forward(height)
        b.left(90)
        b.forward(width / 4)
        b.right(90)
        b.forward(width / 4)
        b.left(90)
        b.forward(width / 2)
        b.left(90)
        b.forward(width / 4)
        b.right(90)
        b.forward(width / 4)
        b.left(90)
        b.forward(height)
        b.end_fill()
        b.penup()
        b.home()

    def empirestate(self, height, width, color, x, y):
        a = turtle.Turtle()
        a.speed(10)
        a.goto(x, y)
        a.pendown()
        a.begin_fill()
        a.fillcolor(color)
        a.forward(width)
        a.left(90)
        a.forward(height)

        for i in range(3):
            a.left(90)
            a.forward(width / 8)
            a.right(90)
            a.forward(width / 8)

        a.left(90)
        a.forward(width / 4)

        for i in range(3):
            a.left(90)
            a.forward(width / 8)
            a.right(90)
            a.forward(width / 8)

        a.left(90)
        a.forward(height)
        a.end_fill()
        a.penup()
        a.home()

    def building(self, base, height, color, a, y):
        x = turtle.Turtle()
        x.speed(10)
        x.goto(a, y)
        x.begin_fill()
        x.fillcolor(color)
        x.pendown()
        x.forward(base)
        x.left(90)
        x.forward(height)
        x.circle((base / 2), 180)
        x.forward(height)
        x.end_fill()
        x.penup()
        x.home()

    def curvedbuilding(self, color, a, b):
        y = turtle.Turtle()
        y.speed(10)
        y.goto(a, b)
        y.begin_fill()
        y.fillcolor(color)
        y.pendown()
        y.forward(50)
        y.left(60)
        y.circle(160, 60)
        y.left(60)
        y.forward(50)
        y.left(60)
        y.circle(160, 60)
        y.left(60)
        y.end_fill()
        y.penup()
        y.home()

    def building2(self, width, height, color, x, y):
        z = turtle.Turtle()
        z.speed(10)
        z.goto(x, y)
        z.begin_fill()
        z.fillcolor(color)
        z.pendown()
        z.forward(width)
        z.left(90)
        z.forward(height)
        z.left(90)
        z.forward(width / 6)
        z.right(110)
        z.forward(width / 6)
        z.left(140)
        z.forward(width / 6)
        z.right(90)
        z.forward(width / 2)
        z.left(120)
        z.forward(width / 2)
        z.right(110)
        z.forward(width / 6)
        z.left(140)
        z.forward(width / 6)
        z.right(90)
        z.forward(width / 6)
        z.left(90)
        z.forward(height)
        z.end_fill()
        z.penup()
        z.home()

    def buildingconnect(self, width, height, color, a, b):
        q = turtle.Turtle()
        q.speed(10)
        q.goto(a, b)
        q.begin_fill()
        q.fillcolor(color)
        q.forward(width)
        q.left(90)
        q.forward(height)

        q.left(90)
        q.forward(width / 9)
        q.right(90)
        q.forward(width / 2)
        q.left(90)
        q.forward(width / 9)
        q.left(90)
        q.forward(width / 2)
        q.right(90)
        q.forward(width / 9)
        q.left(90)
        q.forward(width / 9)

        q.right(90)
        q.forward(width / 3)

        q.right(90)
        q.forward(width / 9)
        q.left(90)
        q.forward(width / 9)
        q.right(90)
        q.forward(width / 2)
        q.left(90)
        q.forward(width / 9)
        q.left(90)
        q.forward(width / 2)
        q.right(90)
        q.forward(width / 9)
        q.left(90)
        q.forward(height)

        q.penup()
        q.left(90)
        q.forward(width / 3)
        q.left(90)
        q.pendown()
        q.forward(height / 1.2)
        q.right(90)
        q.forward(width / 4)
        q.right(90)
        q.forward(height / 1.2)
        q.end_fill()
        q.penup()
        q.home()

    def mountains(self, xposition, height, color):
        t = turtle.Turtle()
        t.speed(10)
        t.penup()
        t.goto(xposition, 0)
        t.pendown()
        t.begin_fill()
        t.fillcolor(color)
        t.left(45)
        t.forward(height)
        t.right(20)
        t.circle(-100, 50)
        t.right(20)
        t.forward(height)
        t.right(135)
        t.forward(450)
        t.end_fill()
        t.penup()
        t.home()

    def skyblock(self, x, y, color):
        sky = turtle.Turtle()
        sky.speed(10)
        sky.goto(0, 0)
        sky.pendown()
        ground.begin_fill()
        ground.fillcolor(color)
        ground.left(180)
        ground.forward(x)
        ground.right(90)
        ground.forward(y)
        ground.right(90)
        ground.forward(x * 2)
        ground.right(90)
        ground.forward(y)
        ground.right(90)
        ground.forward(x)
        ground.end_fill()
        ground.penup()
        ground.home()

    def groundblock(self, x, y, color):
        ground = turtle.Turtle()
        ground.speed(10)
        ground.goto(0, 0)
        ground.pendown()
        ground.begin_fill()
        ground.fillcolor(color)
        ground.left(180)
        ground.forward(x)
        ground.left(90)
        ground.forward(y)
        ground.left(90)
        ground.forward(x * 2)
        ground.left(90)
        ground.forward(y)
        ground.left(90)
        ground.forward(x)
        ground.end_fill()
        ground.penup()
        ground.home()

# Start flag code -------------------------------------------#
# Accepts a as width
# Accepts t as item to be drawn
def star(a, t):
    # Calculate Diameter
    diameter = a * 0.0616
    # This is the size of the star
    radius = diameter / 2
    # draw a circle to test coordinates
    # -> position turtle at bottom-center of circle
    t.speed(10)
    t.penup()
    t.right(90)
    t.forward(radius)
    t.left(90)
    #  -> draw circle
    #t.pendown()
    #t.circle(radius)
    #  -> go back to center
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(90)
    # In order to draw a star, I need to figure out the length of one 'leg' of the star.
    # This took a diagram and bit of trigonometry to figure out ...
    leg = radius * sqrt(5 - 2 * sqrt(5))
    # Go to top of star, and point the turtle down the first leg of the star
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(162)
    # Draw the star, starting at the top
    t.begin_fill()
    t.fillcolor('white')
    t.pendown()
    for i in range(5):
        t.forward(leg)
        t.left(72)
        t.forward(leg)
        t.right(144)
    t.end_fill()
    # Return to initial location
    t.penup()
    t.right(18)
    t.forward(radius)
    t.left(90)


def reposition(item, horposition, verposition):
    # Re-Position Arrow to upper left corner of flag
    item.speed(10)
    item.penup()
    item.right(180)
    item.forward(horposition) #275
    item.right(90)
    item.forward(verposition) #250
    item.right(90)

# Accept item as turtle instance object
# Accept x as union length
def top_stripe_reposition(item, x, horposition, verposition):
    # Re-Position Arrow to union length start
    item.speed(10)
    item.penup()
    item.right(180)
    item.forward(horposition) #275
    item.right(90)
    item.forward(verposition) #250
    item.right(90)
    item.forward(x)


def printrectangle(x, a, b):
    # Create instance of turtle
    rectangle = turtle.Turtle()
    rectangle.speed(10)
    # Call reposition function
    reposition(rectangle, a, b)
    # Times by 1.9 to match the specifications
    length = x * 1.9
    # Draw Rectangle
    rectangle.pendown()
    rectangle.forward(length)
    rectangle.right(90)
    rectangle.forward(x)
    rectangle.right(90)
    rectangle.forward(length)
    rectangle.right(90)
    rectangle.forward(x)
    rectangle.penup()
    rectangle.home()

    return length

# Calculate width of union (C)
def innerwidth(x):
    # Calculate inner width
    inner_width = x * 0.5385
    return inner_width

# Calculate length of union (D)
def innerlength(x):
    # Calculate inner length
    inner_length = x * 0.76
    return inner_length

# Draw Union
def drawinnersquare(x, y, a, b):
    # Create instance of turtle to start drawing
    insquare = turtle.Turtle()
    insquare.speed(10)
    # Call reposition function
    reposition(insquare, a, b)
    # Draw Rectangle
    insquare.begin_fill()
    insquare.fillcolor('blue')
    insquare.pendown()
    insquare.forward(y)
    insquare.right(90)
    insquare.forward(x)
    insquare.right(90)
    insquare.forward(y)
    insquare.right(90)
    insquare.forward(x)
    insquare.end_fill()

    insquare.penup()
    insquare.home()

# Calculate stripe width
def stripewidth(x):
    # Calculate stripe width
    stripe_width = x * 0.0769
    return stripe_width

# Calculate top stripes' length
# Accept x as width
def topstripelength(x):
    # Call inner length function and Set y equals to it
    y = innerlength(x)
    # Calculate lenght again and set to z
    z = x * 1.9
    # Calculate top stripe length
    top_stripe_length = z - y
    return top_stripe_length

# Draw top stripes
# Accept x as stripe width
# Accept y as top stripe length
# Accept z as union length
def drawtopstripe(a, x, y, z, d, f):
    # Create instance of turtle
    topStripe = turtle.Turtle()
    topStripe.speed(10)
    # Call function to position at end of union length
    top_stripe_reposition(topStripe, z, d, f)
    bottomstripe = a * 1.9

    topStripe.begin_fill()
    topStripe.fillcolor('red')
    topStripe.pendown()
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('white')
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('red')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('white')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('red')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('white')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('red')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(y)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('white')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('red')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('white')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('red')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('white')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.begin_fill()
    topStripe.fillcolor('red')
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.right(90)
    topStripe.forward(bottomstripe)
    topStripe.right(90)
    topStripe.forward(x)
    topStripe.end_fill()

    topStripe.penup()
    topStripe.home()

# Draw Stars
# accept a as width
def drawstars(a):
    # Create object to draw stars
    d = turtle.Turtle()
    # Call reposition function
    reposition(d)
    d.right(90)
    d.forward(a * 0.054)
    d.left(90)
    d.forward(a * 0.063)

    return d














# End draw flag functions -------------------------------------------#

# Begin drawing -------------------------------------------#
ground = Structure()
ground.groundblock(400, 200, 'dimgray')

sky = Structure()
sky.skyblock(400, 500, 'skyblue')

mountain = Structure()
mountain.mountains(-400, 200, 'darkgreen')

mountain = Structure()
mountain.mountains(-150, 300, 'darkolivegreen')

#----------------------   Draw Building ---------------------#

q1 = Structure()
q1.building(60, 250, 'lightgray', -350, 0)

o1 = Structure()
o1.curvedbuilding('ghostwhite', -300, 0)

y1 = Structure()
y1.rectangularbuilding(300, 50, 'grey', -270, 0)

a1 = Structure()
a1.trianglebuilding(80, 'lightcyan', -230, 0)

b1 = Structure()
b1.triangleroofbuilding(200, 50, 'lightgrey', -185, 0)

w1 = Structure()
w1.stepbuilding(150, 50, 'gainsboro', -140, 0)

t1 = Structure()
t1.empirestate(220, 50, 'LightSteelBlue', -100, 0)

z1 = Structure()
z1.trianglebuilding(50, 'grey', -70, 0)

p1 = Structure()
p1.rectangularbuilding(100, 50, 'honeydew', -40, 0)

w1 = Structure()
w1.triangleroofbuilding(250, 50,'gray', 0, 0)

c1 = Structure()
c1.buildingconnect(80, 250, 'azure', 40, 0)

d1 =  Structure()
d1.building2(60, 300, 'snow', 110, 0)

m1 = Structure()
m1.curvedbuilding('mintcream', 150, 0)

n1 = Structure()
n1.empirestate(270, 50, 'lightcyan', 185, 0)

s1 = Structure()
s1.stepbuilding(195, 50, 'lightgrey', 225, 0)

f1 = Structure()
f1.triangleroofbuilding(230, 45, 'lightsteelblue', 255, 0)


# -------------  Start Drawing Flag -------------  #
def drawFlag(width, horposition, verposition):
    # Width value entered by user
    # Will have to be in form of a question with input validation
    #width = 50

    # variable declaration
    verticalgap = width * 0.054
    horizontalgap = width * 0.063

    doublehorizontal = horizontalgap * 2
    doublevertical = verticalgap * 2

    # Store width in backup width for further use
    backupWidth = width

    # Call function to draw rectangle
    printrectangle(width, horposition, verposition)

    # Call function to calculate inner width
    unionWidth = innerwidth(width)

    # Call function to calculate inner length
    unionLength = innerlength(width)

    # Call function to draw inner square
    drawinnersquare(unionWidth, unionLength, horposition, verposition)

    # Call function to calculate stripe width
    stripeWidth = stripewidth(width)

    # Call function to calculate top stripe length
    topStripeLength = topstripelength(width)

    # Draw top stripes using stripeWidth and topStripeLength variables
    drawtopstripe(width, stripeWidth, topStripeLength, unionLength, horposition, verposition)

    # Position Star
    # Create object to draw stars
    d = turtle.Turtle()

    # Call reposition function
    reposition(d, horposition, verposition)
    # Position to draw first star
    d.right(90)
    d.forward(verticalgap) #1
    d.left(90)
    d.forward(horizontalgap)
    star(width, d)

    # Draw Star
    # First Row
    for i in range(5):
        d.forward(doublehorizontal)
        star(width, d)

    d.home()

    # Second Row
    e = turtle.Turtle()
    reposition(e, horposition, verposition)

    e.right(90)
    for i in range(2):
        e.forward(verticalgap)
    e.left(90)
    e.forward(horizontalgap)
    e.forward(horizontalgap)
    star(width, e)

    for i in range(4):
        e.forward(doublehorizontal)
        star(width, e)

    e.home()

    # Third Row
    f = turtle.Turtle()
    reposition(f, horposition, verposition)
    f.right(90)
    for i in range(3):
        f.forward(verticalgap)
    f.left(90)
    f.forward(horizontalgap)
    star(width, f)

    for i in range(5):
        f.forward(doublehorizontal)
        star(width, f)

    f.home()

    # Fourth Row
    g = turtle.Turtle()
    reposition(g, horposition, verposition)
    g.right(90)
    for i in range(4):
        g.forward(verticalgap)
    g.left(90)
    g.forward(horizontalgap)
    g.forward(horizontalgap)
    star(width, g)

    for i in range(4):
        g.forward(doublehorizontal)
        star(width, g)

    g.home()

    # Fifth Row
    h = turtle.Turtle()
    reposition(h, horposition, verposition)
    h.right(90)
    for i in range(5):
        h.forward(verticalgap)
    h.left(90)
    h.forward(horizontalgap)
    star(width, h)

    for i in range(5):
        h.forward(doublehorizontal)
        star(width, h)

    h.home()

    # Sixth Row
    i = turtle.Turtle()
    reposition(i, horposition, verposition)
    i.right(90)
    for a in range(6):
        i.forward(verticalgap)
    i.left(90)
    i.forward(horizontalgap)
    i.forward(horizontalgap)
    star(width, i)

    for w in range(4):
        i.forward(doublehorizontal)
        star(width, i)

    i.home()

    # Seventh Row
    j = turtle.Turtle()
    reposition(j, horposition, verposition)
    j.right(90)
    for i in range(7):
        j.forward(verticalgap)
    j.left(90)
    j.forward(horizontalgap)
    star(width, j)

    for w in range(5):
        j.forward(doublehorizontal)
        star(width, j)

    j.home()

    # Eight Row
    m = turtle.Turtle()
    reposition(m, horposition, verposition)
    m.right(90)
    for i in range(8):
        m.forward(verticalgap)
    m.left(90)
    m.forward(horizontalgap)
    m.forward(horizontalgap)
    star(width, m)

    for w in range(4):
        m.forward(doublehorizontal)
        star(width, m)

    m.home()

    # Ninth Row
    n = turtle.Turtle()
    reposition(n, horposition, verposition)
    n.right(90)
    for i in range(9):
        n.forward(verticalgap)
    n.left(90)
    n.forward(horizontalgap)
    star(width, n)

    for w in range(5):
        n.forward(doublehorizontal)
        star(width, n)

    n.home()

# Place flag on top of building
drawFlag(25, 80, 265)

# Place flag on top of pyramid
drawFlag(25, 195, 90)

# Extra flag
drawFlag(150, 0, 0)

# Keep screen open
turtle.mainloop()








