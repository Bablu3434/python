import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red", "blue", "green", "orange", "purple", "pink"]

for i in range(36):
    t.color(colors[i % 6])
    
    for j in range(4):
        t.forward(100)
        t.right(90)
    
    t.right(100)

turtle.done()