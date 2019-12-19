l = 2
l1 = l
s = 0

root.bind ('<Left>', moveleft)
root.bind ('<Right>', moveright)
root.bind ('<Up>', moveup)
root.bind ('<Down>', movedown)

#A = [[60, 60, 150, 120], [180, 60, 300, 120], [330, 30, 360, 120], [390, 60, 510, 120], [540, 60, 630, 120], [60, 150, 150, 180], [180, 150, 210, 300], [240, 150, 390, 180]]
#A = [[60, 60, 105, 90], [135, 60, 195, 90], [225, 30, 240, 90], [270, 60, 330, 90], [360, 60, 405, 90], [60, 120, 105, 135], [135, 120, 150, 225], [180, 120, 285, 135], [315, 120, 330, 225], [360, 120, 405, 135], [225, 135, 240, 180], [150, 165, 195, 180]]

v = [1, 0.5]
A = [[40, 40, 100, 80], [140, 40, 220, 80], [260, 0, 280, 80], [320, 40, 400, 80], [440, 40, 500, 80], [40, 120, 100, 140], [140, 120, 160, 260], [200, 120, 340, 140], [380, 120, 400, 260], [440, 120, 500, 140], [260, 140, 280, 200], [160, 180, 220, 200], [320, 180, 380, 200], [140, 300, 160, 380], [380, 300, 400, 380], [200, 360, 340, 380], [260, 380, 280, 440], [40, 420, 100, 440], [140, 420, 220, 440], [320, 420, 400, 440], [440, 420, 500, 440], [80, 440, 100, 500], [440, 440, 460, 500], [0, 480, 40, 500], [200, 480, 340, 500], [500, 480, 540, 500], [140, 480, 160, 540], [380, 480, 400, 540], [260, 500, 280, 560], [40, 540, 220, 560], [320, 540, 500, 560], [-20, -20, 560, 0], [-20, 600, 560, 620], [-20, 0, 0, 180], [-20, 180, 100, 200], [80, 200, 100, 240], [-20, 240, 100, 260], [-20, 300, 100, 320], [80, 320, 100, 360], [-20, 360, 100, 380], [-20, 380, 0, 600], [540, 0, 560, 180], [440, 180, 560, 200], [440, 200, 460, 240], [440, 240, 560, 260], [440, 300, 560, 320], [440, 320, 460, 360], [440, 360, 560, 380], [540, 380, 560, 600]]
draw_walls ()
draw_lives (l)
start ()

file = open ('1_level.txt')
file.read ()

while l >= 0:
    for i in range (len (A)):
        scan_pac_f (A [i])
    move_pac ()
    xB += vxB
    yB += vyB
    xP += vxP
    yP += vyP
    xI += vxI
    yI += vyI
    xC += vxC
    yC += vyC
    #if x < r + 2:
        #x = r + 2
        #vx = 0
    #if y < r + 2:
        #y = r + 2
        #vy = 0
    #if x > (540 + h) - (r + 2):
        #x = (540 + h) - (r + 2)
        #vx = 0
    #if y > (600 + h) - (r + 2):
        #y = (600 + h) - (r + 2)
        #vy = 0
    time.sleep (0.01)
    draw ()
    canv.update ()
    a += 3 * f
    if a == 0: f = 1
    elif a == 45: f = -1
    #for i in range (len (A)):
        #scan_pac (A [i])
    #scan_pac ()
    rB = (x - xB) ** 2 + (y - yB) ** 2
    rP = (x - xP) ** 2 + (y - yP) ** 2
    rI = (x - xI) ** 2 + (y - yI) ** 2
    rC = (x - xC) ** 2 + (y - yC) ** 2
    check_lives ()

canv.create_text ((540 + 2 * h) // 2, (600 + 2 * h) // 2, text = 'GAME OVER', font = 'Times 72', justify = CENTER, fill = 'dark red')
canv.update ()

root.mainloop()
