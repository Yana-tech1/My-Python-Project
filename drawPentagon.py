import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
def DrawPentagon():
  for i in range(5):
    t.left(72)
    t.forward(100)
DrawPentagon()
