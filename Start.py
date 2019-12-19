h = 60 #Расстояние от края до поля
r = 12 #Радиус PACMANа
#d = (r + 15) ** 2 Квадрат допустимого расстояния от PACMANа до привидений

from tkinter import *
import time
root = Tk() #Создание окна приложения
canv = Canvas (root, width = 540 + 2 * h, height = 600 + 2 * h, bg = 'black')
canv.pack()

def draw_pac ():

    global x, y, vx, vy
    if vx == 0 and vy == 0: canv.create_oval (x - r, y - r, x + r, y + r, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vx < 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 226 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vx > 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 46 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vy < 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 136 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')
    elif vy > 0: canv.create_arc (x - r, y - r, x + r, y + r, start = 316 - a, extent = 268 + 2 * a, fill = 'yellow', outline = 'yellow', tag = 'Pac')

def moveleft (event):
    global vx, vy
    vx = -2
    vy = 0

def moveright (event):
    global vx, vy
    vx = 2
    vy = 0

def moveup (event):
    global vx, vy
    vx = 0
    vy = -2

def movedown (event):
    global vx, vy
    vx = 0
    vy = 2

def move_pac ():
    global x, y, vx, vy
    x = (x + vx - (h - 20)) % (540 + h - 20) + (h - 20)
    y = y + vy

def move_Blinky ():
    global xB, yB, x, y, vxB, vyB
    #if x == xC: vxC = 0
    #if y == yC: vyC = 0
    if abs (x - xB) >= abs (y - yB):
        if x != xB:
            if x - xB > 0: vxB = v [s]
            else: vxB = -v [s]
        vyB = 0
    else:
        if y != yB:
            if y - yB > 0: vyB = v [s]
            else: vyB = -v [s]
        vxB = 0

def move_Pinky ():
    global xP, yP, x, y, vxP, vyP
    if abs (x - xP) >= abs (y - yP):
        if x != xP:
            if x - xP > 0: vxP = v [s]
            else: vxP = -v [s]
        vyP = 0
    else:
        if y != yP:
            if y - yP > 0: vyP = v [s]
            else: vyP = -v [s]
        vxP = 0

def move_Inky ():
    global xI, yI, x, y, vxI, vyI
    if abs (x - xI) >= abs (y - yI):
        if x != xI:
            if x - xI > 0: vxI = v [s]
            else: vxI = -v [s]
        vyI = 0
    else:
        if y != yI:
            if y - yI > 0: vyI = v [s]
            else: vyI = -v [s]
        vxI = 0

def move_Clyde ():
    global xC, yC, x, y, vxC, vyC
    if abs (x - xC) >= abs (y - yC):
        if x != xC:
            if x - xC > 0: vxC = v [s]
            else: vxC = -v [s]
        vyC = 0
    else:
        if y != yC:
            if y - yC > 0: vyC = v [s]
            else: vyC = -v [s]
        vxC = 0
