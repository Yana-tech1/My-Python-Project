import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
def DrawHexagon():
  for i in range(6):
    t.left(60)
    t.forward(100)
DrawHexagon()
