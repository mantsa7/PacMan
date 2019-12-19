def start ():
    global x, y, xB, yB, xP, yP, xI, yI, xC, yC
    global vx, vy, vxB, vyB, vxP, vyP, vxI, vyI, vxC, vyC
    global w, a, f
    global rB, rP, rI, rC
    x, y = 270 + h, 460 + h
    xB, yB = 270 + h, 240 + h
    xP, yP = 270 + h, 300 + h
    xI, yI = 230 + h, 300 + h
    xC, yC = 310 + h, 300 + h
    vx, vy = 0, 0
    vxB, vyB = 0, 0
    vxP, vyP = 0, 0
    vxI, vyI = 0, 0
    vxC, vyC = 0, 0
    a, f = 0, 1
    #rB = (x - xB) ** 2 + (y - yB) ** 2
    #rP = (x - xP) ** 2 + (y - yP) ** 2
    #rI = (x - xI) ** 2 + (y - yI) ** 2
    #rC = (x - xC) ** 2 + (y - yC) ** 2
    draw ()
    canv.update ()
    time.sleep (2)
