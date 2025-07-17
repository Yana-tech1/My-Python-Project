import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
def DrawTriangle():
  for i in range(3):
    t.left(120)
    t.forward(100)
DrawTriangle()
