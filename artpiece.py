import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
t.pensize(5)
t.pencolor("Orange")
def draw_petal():
  t.circle(100,60)
  t.lt(120)
  t.circle(100,60)
  t.lt(120)
for i in range(30):
  draw_petal()
  t.lt(12)
t.penup()
t.goto(0,-40)
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()
