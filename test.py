import random
import turtle
size = 4
screen = turtle.Screen()
screen.screensize(1001, 1001)
t = turtle.Turtle()
#the higher the speed the faster the dots happen, leave everything else here the same
t.speed(1000000)
t.penup()
t.goto(0, 400)
t.pendown()
t.dot(size)
t.penup()
t.goto(-462, -400)
t.pendown()
t.dot(size)
t.penup()
t.goto(462, -400)
t.pendown()
t.dot(size)

#these are the coords for the points of the triangle, leave constant
o = [1, 400]
x = [-462, -400]
y = [462, -400]
t.penup()

#this is the initial point, change this to see you still get the same pattern
#keep within +/- 500 for both
spt = [-400, -70]
f = [spt[0], spt[1]]
t.goto(f[0], f[1])

t.pendown()
t.dot(3)

start = [spt[0], spt[1]]
pts = []
pts.append(start)
#100 yes, 1000 yes, 10000
for i in range(10000):
    current = pts[i]
    pt = []
    r = random.randint(0, 2)
    if r == 0:
        pt.append(((o[0] - current[0])/2) + current[0])
        pt.append(((o[1] - current[1])/2) + current[1])
    elif r == 1:
        pt.append(((x[0] - current[0]) / 2) + current[0])
        pt.append(((x[1] - current[1]) / 2) + current[1])
    else:
        pt.append(((y[0] - current[0]) / 2) + current[0])
        pt.append(((y[1] - current[1]) / 2) + current[1])
    print(pt)
    print(r)
    t.penup()
    t.goto(pt[0], pt[1])
    t.pendown()
    t.dot(size)
    pts.append(pt)

turtle.done()