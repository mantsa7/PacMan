def draw_body (xG, yG, c):
    #Создаем функцию, которая рисует тело привидения
    canv.create_rectangle (xG - 14, yG - 4, xG + 14, yG + 8, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 12, yG - 10, xG + 12, yG - 4, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 10, yG - 12, xG + 10, yG - 10, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 8, yG - 14, xG + 8, yG - 12, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 4, yG - 16, xG + 4, yG - 14, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 14, yG + 8, xG - 6, yG + 10, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 12, yG + 10, xG - 8, yG + 12, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 4, yG + 8, xG + 4, yG + 10, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG - 2, yG + 10, xG + 2, yG + 12, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG + 6, yG + 8, xG + 14, yG + 10, fill = c, outline = c, tag = 'Ghost')
    canv.create_rectangle (xG + 8, yG + 10, xG + 12, yG + 12, fill = c, outline = c, tag = 'Ghost')

def draw_stop (xG, yG):
    #Функция, которая рисует тело привидения, если оно не двигается
    canv.create_rectangle (xG - 10, yG - 8, xG - 2, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 8, yG - 10, xG - 4, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 8, yG - 2, xG - 4, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 8, xG + 10, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 10, xG + 8, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 2, xG + 8, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_right (xG, yG):
    #Функция, которая рисует тело привидения, если оно движется вправо
    canv.create_rectangle (xG - 8, yG - 8, xG, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 6, yG - 10, xG - 2, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 6, yG - 2, xG - 2, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 8, xG + 12, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 6, yG - 10, xG + 10, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 6, yG - 2, xG + 10, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_left (xG, yG):
    #Функция, которая рисует тело привидения, если оно движется влево
    canv.create_rectangle (xG - 12, yG - 8, xG - 4, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 10, yG - 10, xG - 6, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 10, yG - 2, xG - 6, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG, yG - 8, xG + 8, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 10, xG + 6, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 2, xG + 6, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_ghost (xG, yG, vxG, vyG, c):
    #Функция, которая рисует тело привидения по ходу его движения,
    #т.е. до этого рисовали привидение просто как объект, а теперь - как движущееся тело
    global x, y
    draw_body (xG, yG, c)
    if vxG == 0 and vyG == 0:
        draw_stop (xG, yG)
        draw_1 (xG, yG)
    else:
        if vxG > 0:
            draw_right (xG, yG)
            draw_4 (xG, yG)
        elif vxG < 0:
            draw_left (xG, yG)
            draw_6 (xG, yG)         
        elif vyG > 0:
            draw_stop (xG, yG)
            draw_2 (xG, yG)           
        else:
            draw_stop (xG, yG)
            draw_3 (xG, yG)    
        #В зависимости от значения скорости меняется рисовка привидения.    

def scan_pac (P):
    #Описываем действия пакмена, если он наткнется на стену - т.е. условия его остановки
    global x, y, vx, vy, h, r
    if x - r > P [0] + h and x - r < P [2] + h or x + r > P [0] + h and x + r < P [2] + h or P [0] + h > x - r and P [0] + h < x + r or P [2] + h > x - r and P [2] + h < x + r:
        if y - r > P [1] + h and y - r < P [3] + h or y + r > P [1] + h and y + r < P [3] + h or P [1] + h > y - r and P [1] + h < y + r or P [3] + h > y - r and P [3] + h < y + r:
    
            print (x, y)
            
            if x < P [0] + h:
                x -= 2
                vx = 0
            if x > P [2] + h:
                x += 2
                vx = 0
            if y < P [1] + h:
                y -= 2
                vy = 0
            if y > P [3] + h:
                y += 2
                vy = 0
           
def scan_pac_f (P):
    global x, y, vx, vy, h, r
    if x + vx - (r + 2) > P [0] + h and x + vx - (r + 2) < P [2] + h or x + vx + (r + 2) > P [0] + h and x + vx + (r + 2) < P [2] + h or P [0] + h > x + vx - (r + 2) and P [0] + h < x + vx + (r + 2) or P [2] + h > x + vx - (r + 2) and P [2] + h < x + vx + r:
        if y + vy - (r + 2) > P [1] + h and y + vy - (r + 2) < P [3] + h or y + vy + (r + 2) > P [1] + h and y + vy + (r + 2) < P [3] + h or P [1] + h > y + vy - (r + 2) and P [1] + h < y + vy + (r + 2) or P [3] + h > y + vy - (r + 2) and P [3] + h < y + vy + r:
            vx = 0
            vy = 0

def scan_pac_f_1 (P):
    global x, y, vx, vy, h, r
    if ((x + vx - 20) - (P [2] + h)) * ((x + vx + 20) - (P [0] + h)) <= 0 and ((y + vy - 20) - (P [3] + h)) * ((y + vy + 20) - (P [1] + h)) <= 0:
        vx = 0
        vy = 0


def check_lives ():
    #Проверяем количество оставшихся жизней, чтобы понять - перезапускать игру или выводить на экран Game Over
    global rB, rP, rI, rC, r, w, l
    if rB <= (r + 15) ** 2 or rP <= (r + 15) ** 2 or rI <= (r + 15) ** 2 or rC <= (r + 15) ** 2:
        l -= 1
        canv.create_rectangle (2 * r * l + 15, 15 + 2 * r, 2 * r * l + 15 + 2 * r, 15, fill = 'black')
        canv.update ()
        time.sleep (2)
        if l >= 0:
            start ()
            draw ()
            canv.update ()
def draw ():
    #Перезапуск игры (следующая жизнь, если стратили)
    global l1
    canv.delete ('Pac', 'Ghost')
    draw_pac ()
    draw_Blinky (xB, yB, vxB, vyB)
    draw_Pinky (xP, yP, vxP, vyP)
    draw_Inky (xI, yI, vxI, vyI)
    draw_Clyde (xC, yC, vxC, vyC)
    if l1 != l:
        draw_lives (l)
        l1 = l

def start ():
    #Описываем состояния привидений при запуске игры 
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
   
    draw ()
    canv.update ()
    time.sleep (2)

l = 2
l1 = l
s = 0

#Описываем управление с кллавиатуры
root.bind ('<Left>', moveleft)
root.bind ('<Right>', moveright)
root.bind ('<Up>', moveup)
root.bind ('<Down>', movedown)

v = [1, 0.5]
A = [[40, 40, 100, 80], [140, 40, 220, 80], [260, 0, 280, 80], [320, 40, 400, 80], [440, 40, 500, 80], [40, 120, 100, 140], [140, 120, 160, 260], [200, 120, 340, 140], [380, 120, 400, 260], [440, 120, 500, 140], [260, 140, 280, 200], [160, 180, 220, 200], [320, 180, 380, 200], [140, 300, 160, 380], [380, 300, 400, 380], [200, 360, 340, 380], [260, 380, 280, 440], [40, 420, 100, 440], [140, 420, 220, 440], [320, 420, 400, 440], [440, 420, 500, 440], [80, 440, 100, 500], [440, 440, 460, 500], [0, 480, 40, 500], [200, 480, 340, 500], [500, 480, 540, 500], [140, 480, 160, 540], [380, 480, 400, 540], [260, 500, 280, 560], [40, 540, 220, 560], [320, 540, 500, 560], [-20, -20, 560, 0], [-20, 600, 560, 620], [-20, 0, 0, 180], [-20, 180, 100, 200], [80, 200, 100, 240], [-20, 240, 100, 260], [-20, 300, 100, 320], [80, 320, 100, 360], [-20, 360, 100, 380], [-20, 380, 0, 600], [540, 0, 560, 180], [440, 180, 560, 200], [440, 200, 460, 240], [440, 240, 560, 260], [440, 300, 560, 320], [440, 320, 460, 360], [440, 360, 560, 380], [540, 380, 560, 600]]
draw_walls ()
draw_lives (l)
start ()

file = open ('1_level.txt')
file.read ()

#рисуем картинку для окончания игры
canv.create_text ((540 + 2 * h) // 2, (600 + 2 * h) // 2, text = 'GAME OVER', font = 'Times 72', justify = CENTER, fill = 'dark red')
canv.update ()

root.mainloop()
