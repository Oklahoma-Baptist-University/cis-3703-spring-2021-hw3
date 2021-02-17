import graphics
import math

## Whenever we are doing the same thing over and over again,
## it is a good idea to create a function
def draw_circle(win, center, radius, color):
    circ = graphics.Circle(center, radius)
    circ.setFill(color)
    circ.draw(win)
    
def p2(radius):
    win = graphics.GraphWin("Archery", 500, 500)

    draw_circle(win, graphics.Point(250, 250), radius * 5, "white")
    draw_circle(win, graphics.Point(250, 250), radius * 4, "black")
    draw_circle(win, graphics.Point(250, 250), radius * 3, "blue")
    draw_circle(win, graphics.Point(250, 250), radius * 2, "red")
    draw_circle(win, graphics.Point(250, 250), radius, "yellow")
    
    return win

def draw_one(win, pt, size):
    draw_circle(win, graphics.Point(pt.getX() + 10, pt.getY() + 10), 4, "black")
    
def draw_two(win, pt, size):
    draw_circle(win, graphics.Point(pt.getX() + 20, pt.getY() + 10), 4, "black")
    
def draw_three(win, pt, size):
    draw_circle(win, graphics.Point(pt.getX() + 30, pt.getY() + 10), 4, "black")
    
def draw_four(win, pt, size):
    draw_circle(win, graphics.Point(pt.getX() + 10, pt.getY() + 20), 4, "black")
    
def draw_five(win, pt, size):
    draw_circle(win, graphics.Point(pt.getX() + 20, pt.getY() + 20), 4, "black")
    
def draw_six(win, pt, size):
    draw_circle(win, graphics.Point(pt.getX() + 30, pt.getY() + 20), 4, "black")
    
def draw_seven(win, pt, size):
    draw_circle(win, graphics.Point(pt.getX() + 10, pt.getY() + 30), 4, "black")
    
def draw_eight(win, pt, size):
    draw_circle(win, graphics.Point(pt.getX() + 20, pt.getY() + 30), 4, "black")
    
def draw_nine(win, pt, size):
    draw_circle(win, graphics.Point(pt.getX() + 30, pt.getY() + 30), 4, "black")
    
def draw_die(win, size, pt1):
    die = graphics.Rectangle(pt1, graphics.Point(pt1.getX() + 
                                                 size, pt1.getY() + size))
    die.draw(win)
    

def roll_one(win, pt):
    draw_die(win, 40, pt)
    draw_five(win, pt, 50)    
    
def roll_two(win, pt):
    draw_die(win, 40, pt)
    draw_one(win, pt, 50)    
    draw_nine(win, pt, 50)    
    
def roll_three(win, pt):
    draw_die(win, 40, pt)
    draw_one(win, pt, 50)
    draw_five(win, pt, 50)    
    draw_nine(win, pt, 50)    
    
def roll_four(win, pt):
    draw_die(win, 40, pt)
    draw_one(win, pt, 50)    
    draw_three(win, pt, 50)    
    draw_seven(win, pt, 50)    
    draw_nine(win, pt, 50)    
    
def roll_five(win, pt):
    draw_die(win, 40, pt)
    draw_one(win, pt, 50)    
    draw_three(win, pt, 50)    
    draw_five(win, pt, 50)    
    draw_seven(win, pt, 50)    
    draw_nine(win, pt, 50)    
    
def p5():
    win = graphics.GraphWin("Dice", 500, 200)
    
    roll_one(win, graphics.Point(20, 20))
    roll_two(win, graphics.Point(80, 20))
    roll_three(win, graphics.Point(140, 20))
    roll_four(win, graphics.Point(200, 20))
    roll_five(win, graphics.Point(260, 20))
    
    return win

def p7(y_intercept): ##, radius, width, height):
    win = graphics.GraphWin("Problem 7", 200, 200)
    radius = 100
    center_x = 100
    center_y = 100
    
    print("y-intercept = ", y_intercept)
    
    # This calculation assumes a circle at center (0,0), which is the upper left
    # of the window
    x1 = math.sqrt(radius ** 2 - y_intercept ** 2)
    x2 = -math.sqrt(radius ** 2 - y_intercept ** 2)
    
    # Adjust for the location of the center
    x1 = x1 + center_x
    x2 = x2 + center_x
    y_intercept = y_intercept + center_y
    
    print(x1, ", ", y_intercept)
    print(x2, ", ", y_intercept)
    
    c1 = graphics.Circle(graphics.Point(x1, y_intercept), 3)
    c1.setFill('red')
    c1.draw(win)
    
    c2 = graphics.Circle(graphics.Point(x2, y_intercept), 3)
    c2.setFill('red')
    c2.draw(win)
    
    l1 = graphics.Line(graphics.Point(x1, y_intercept), graphics.Point(x2, y_intercept))
    l1.setOutline('red')
    l1.draw(win)
    
    center = graphics.Point(center_x, center_y)
    circ = graphics.Circle(center, radius)
    circ.draw(win)

def p8():
    win = graphics.GraphWin("Problem 8", 500, 500)

    p1 = win.getMouse()
    p2 = win.getMouse()
    
    l1 = graphics.Line(p1, p2)
    l1.setOutline("blue")
    l1.setWidth(5)
    l1.draw(win)
    
    dy = -(p2.getY() - p1.getY())
    dx = p2.getX() - p1.getX()
    
    slopeText = graphics.Text(p1, "Slope = " + str(dy/dx))
    slopeText.draw(win)
    lengthText = graphics.Text(p2, "Length = " + str(math.sqrt(dx ** 2 + dy ** 2)))
    lengthText.draw(win)
    
    mid = l1.getCenter()
    midCirc = graphics.Circle(mid, 4)
    midCirc.setFill("cyan")
    midCirc.draw(win)
    
