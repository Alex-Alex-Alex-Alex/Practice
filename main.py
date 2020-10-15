import turtle as t

#draw pentagon
t.pendown()
for i in range(6):
  t.forward(50)
  t.left(72)

def draw_square():
  for i in range(4):
    t.forward(40)
    t.left(90)

draw_square()