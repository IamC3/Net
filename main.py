import random
import tkinter as tk
import orb
from math import sqrt

canvas_width = 500

orbCount = 100
length = 75

master = tk.Tk()
master.title("Net")

mouseX = mouseY = -100

oldMouseX = mouseX
oldMouseY = mouseY

w = tk.Canvas(master, width=canvas_width, height=canvas_width)
w.pack()


def collision(dot):
    # print(dot.topLeft, dot.bottomRight)
    if dot.topLeft[0] <= 0:
        dot.vel[0] = -dot.vel[0]
        # input("flip1")
    if dot.topLeft[1] <= 0:
        dot.vel[1] = -dot.vel[1]
        # input("flip2")
    if dot.bottomRight[0] >= canvas_width:
        dot.vel[0] = -dot.vel[0]
        # input("flip3")
    if dot.bottomRight[1] >= canvas_width:
        dot.vel[1] = -dot.vel[1]
        # input("flip4")


def callback(e):
    global mouseX, mouseY
    mouseX = e.x
    mouseY = e.y
    # print("Pointer is currently at %d, %d" % (mouseX, mouseY))


def animate():
    global oldMouseX, oldMouseY
    for c in connections:
        w.delete(c)
    connections.clear()
    for i, p in enumerate(points):
        w.move(p, orbs[i].vel[0], orbs[i].vel[1])
        orbs[i].updatePos()
        collision(orbs[i])
    w.move(mousePoint, mouseX - oldMouseX, mouseY - oldMouseY)

    lines()
    w.tag_raise("point")
    oldMouseX = mouseX
    oldMouseY = mouseY
    master.after(20, animate)


def lines():
    for o in orbs:
        for m in orbs:
            if sqrt((o.x - m.x) ** 2 + (o.y - m.y) ** 2) <= length:
                connections.append(w.create_line(o.x, o.y, m.x, m.y, fill="#d3d3d3"))
        if sqrt((o.x - mouseX) ** 2 + (o.y - mouseY) ** 2) <= length:
            connections.append(w.create_line(o.x, o.y, mouseX, mouseY, fill="#2b2d31"))


def update():
    for o in orbs:
        points.append(w.create_oval(o.topLeft[0], o.topLeft[1], o.bottomRight[0], o.bottomRight[1],
                                    fill="black", tags="point"))


mousePoint = w.create_oval(mouseX - orb.size, mouseY - orb.size, mouseX + orb.size, mouseY + orb.size,
                           fill="white", tags="point")

orbs = []
points = []
connections = []
for x in range(orbCount):
    orbs.append(orb.Orb())

update()
animate()
master.bind('<Motion>', callback)
master.mainloop()
