import turtle
t = turtle.Turtle()
t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
def DrawHeptagon():
  for i in range(7):
    t.left(51.42)
    t.forward(100)
DrawHeptagon()
