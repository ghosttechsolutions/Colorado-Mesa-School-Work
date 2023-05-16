import turtle
t= turtle.Turtle()
t.speed(20)
t.shape("triangle")
for i in range(0,360,15):
    t.seth(i)
    t.circle(60)