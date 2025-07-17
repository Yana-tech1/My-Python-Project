import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
def DrawCircle():
  for i in range(360):
    t.left(1)
    t.forward(1)
DrawCircle()
