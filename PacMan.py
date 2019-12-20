h = 60  # Расстояние от края до поля
r = 12  # Радиус PACMANа

from tkinter import *
import time

root = Tk()  # Создание главного окна и его передача в переменную root
canv = Canvas(root, width=540 + 2 * h, height=600 + 2 * h,
              bg='black')  # Создаем экземпляр класса Canvas как объект-холст, на котором будем "рисовать" игровое поле
canv.pack()  # Упаковываем с помощью менеджера геометрии - метода pack()


def draw_pac():
    # Рисование Пакмана: в неподвижном состоянии - желтый круг, при движении открывается рот и получается круг с вырезанным сектором

    global x, y, vx, vy  # Координаты Пакмана и проекции его скорости на соответствующие оси
    # В начале игры Пакман не движется --> с помощью метода create_oval() задаем координаты квадрата, описанного вокруг нужного круга
    if vx == 0 and vy == 0:
        canv.create_oval(x - r, y - r, x + r, y + r, fill='yellow', outline='yellow', tag='Pac')
    elif vx < 0:
        canv.create_arc(x - r, y - r, x + r, y + r, start=226 - a, extent=268 + 2 * a, fill='yellow', outline='yellow',
                        tag='Pac')
    # Пакман движется --> с помощью метода create_arc() создаем желтый круг с вырезанным сектором:
    # Для этого передаем координаты квадрата, описанного вокруг круга, в start - градус начала фигуры, в extent - угол поворота
    elif vx > 0:
        canv.create_arc(x - r, y - r, x + r, y + r, start=46 - a, extent=268 + 2 * a, fill='yellow', outline='yellow',
                        tag='Pac')
    elif vy < 0:
        canv.create_arc(x - r, y - r, x + r, y + r, start=136 - a, extent=268 + 2 * a, fill='yellow', outline='yellow',
                        tag='Pac')
    elif vy > 0:
        canv.create_arc(x - r, y - r, x + r, y + r, start=316 - a, extent=268 + 2 * a, fill='yellow', outline='yellow',
                        tag='Pac')


def moveleft(event):
    # Меняем направление скорости на горизонтальное влево
    global vx, vy  # Проекции скорости на оси x, y
    vx = -2
    vy = 0


def moveright(event):
    # Меняем направление скорости на горизонтальное вправо
    global vx, vy  # Проекции скорости на оси x, y
    vx = 2
    vy = 0


def moveup(event):
    # Меняем направление скорости на вертикальное вверх
    global vx, vy  # Проекции скорости на оси x, y
    vx = 0
    vy = -2


def movedown(event):
    # Меняем направление скорости на вертикальное вниз
    global vx, vy  # Проекции скорости на оси x, y
    vx = 0
    vy = 2


def move_pac():
    # Описываем движение Пакмана
    global x, y, vx, vy  # Координаты Пакмана и проекции его скорости на соответствующие оси
    x = (x + vx - (h - 20)) % (540 + h - 20) + (h - 20)  # Не выходим за игровое поле
    y = y + vy


def move_Blinky():
    # Описываем движение Блинки
    global xB, yB, x, y, vxB, vyB  # Координаты Блинки и проекции его скорости на соответствующие оси
    if abs(x - xB) >= abs(y - yB):
        if x != xB:
            if x - xB > 0:
                vxB = v
            else:
                vxB = -v
        vyB = 0
    else:
        if y != yB:
            if y - yB > 0:
                vyB = v
            else:
                vyB = -v
        vxB = 0


def move_Pinky():
    # Описываем движение Пинки
    global xP, yP, x, y, vxP, vyP  # Координаты Пинки и проекции его скорости на соответствующие оси
    if abs(x - xP) >= abs(y - yP):
        if x != xP:
            if x - xP > 0:
                vxP = v
            else:
                vxP = -v
        vyP = 0
    else:
        if y != yP:
            if y - yP > 0:
                vyP = v
            else:
                vyP = -v
        vxP = 0


def move_Inky():
    # Описываем движение Инки
    global xI, yI, x, y, vxI, vyI  # Координаты Инки и проекции его скорости на соответствующие оси
    if abs(x - xI) >= abs(y - yI):
        if x != xI:
            if x - xI > 0:
                vxI = v
            else:
                vxI = -v
        vyI = 0
    else:
        if y != yI:
            if y - yI > 0:
                vyI = v
            else:
                vyI = -v
        vxI = 0


def move_Clyde():
    # Описываем движение Клайда
    global xC, yC, x, y, vxC, vyC  # Координаты Клайда и проекции его скорости на соответствующие оси
    if abs(x - xC) >= abs(y - yC):
        if x != xC:
            if x - xC > 0:
                vxC = v
            else:
                vxC = -v
        vyC = 0
    else:
        if y != yC:
            if y - yC > 0:
                vyC = v
            else:
                vyC = -v
        vxC = 0


def draw_body(xG, yG, c):
    # Создаем функцию, которая рисует тело привидения
    canv.create_rectangle(xG - 14, yG - 4, xG + 14, yG + 8, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG - 12, yG - 10, xG + 12, yG - 4, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG - 10, yG - 12, xG + 10, yG - 10, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG - 8, yG - 14, xG + 8, yG - 12, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG - 4, yG - 16, xG + 4, yG - 14, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG - 14, yG + 8, xG - 6, yG + 10, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG - 12, yG + 10, xG - 8, yG + 12, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG - 4, yG + 8, xG + 4, yG + 10, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG - 2, yG + 10, xG + 2, yG + 12, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG + 6, yG + 8, xG + 14, yG + 10, fill=c, outline=c, tag='Ghost')
    canv.create_rectangle(xG + 8, yG + 10, xG + 12, yG + 12, fill=c, outline=c, tag='Ghost')


def draw_stop(xG, yG):
    # Функция, которая рисует тело привидения, если оно не двигается
    canv.create_rectangle(xG - 10, yG - 8, xG - 2, yG - 2, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG - 8, yG - 10, xG - 4, yG - 8, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG - 8, yG - 2, xG - 4, yG, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG + 2, yG - 8, xG + 10, yG - 2, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG + 4, yG - 10, xG + 8, yG - 8, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG + 4, yG - 2, xG + 8, yG, fill='white', outline='white', tag='Ghost')


def draw_right(xG, yG):
    # Функция, которая рисует тело привидения, если оно движется вправо
    canv.create_rectangle(xG - 8, yG - 8, xG, yG - 2, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG - 6, yG - 10, xG - 2, yG - 8, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG - 6, yG - 2, xG - 2, yG, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG + 4, yG - 8, xG + 12, yG - 2, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG + 6, yG - 10, xG + 10, yG - 8, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG + 6, yG - 2, xG + 10, yG, fill='white', outline='white', tag='Ghost')


def draw_left(xG, yG):
    # Функция, которая рисует тело привидения, если оно движется влево
    canv.create_rectangle(xG - 12, yG - 8, xG - 4, yG - 2, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG - 10, yG - 10, xG - 6, yG - 8, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG - 10, yG - 2, xG - 6, yG, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG, yG - 8, xG + 8, yG - 2, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG + 2, yG - 10, xG + 6, yG - 8, fill='white', outline='white', tag='Ghost')
    canv.create_rectangle(xG + 2, yG - 2, xG + 6, yG, fill='white', outline='white', tag='Ghost')


def draw_1(xG, yG):
    # Рисуем глаза приведения, когда оно стоит на месте
    canv.create_rectangle(xG - 8, yG - 6, xG - 4, yG - 2, fill='blue', outline='blue', tag='Ghost')
    canv.create_rectangle(xG + 4, yG - 6, xG + 8, yG - 2, fill='blue', outline='blue', tag='Ghost')


def draw_2(xG, yG):
    # Рисуем глаза приведения, когда оно движется вверх
    canv.create_rectangle(xG - 8, yG - 4, xG - 4, yG, fill='blue', outline='blue', tag='Ghost')
    canv.create_rectangle(xG + 4, yG - 4, xG + 8, yG, fill='blue', outline='blue', tag='Ghost')


def draw_3(xG, yG):
    # Рисуем глаза приведения, когда оно движется вниз
    canv.create_rectangle(xG - 8, yG - 10, xG - 4, yG - 6, fill='blue', outline='blue', tag='Ghost')
    canv.create_rectangle(xG + 4, yG - 10, xG + 8, yG - 6, fill='blue', outline='blue', tag='Ghost')


def draw_4(xG, yG):
    # Рисуем глаза приведения, когда оно движется вправо
    canv.create_rectangle(xG - 4, yG - 6, xG, yG - 2, fill='blue', outline='blue', tag='Ghost')
    canv.create_rectangle(xG + 8, yG - 6, xG + 12, yG - 2, fill='blue', outline='blue', tag='Ghost')


def draw_5(xG, yG):
    # Рисуем глаза приведения, когда оно движется влево
    canv.create_rectangle(xG - 12, yG - 6, xG - 8, yG - 2, fill='blue', outline='blue', tag='Ghost')
    canv.create_rectangle(xG, yG - 6, xG + 4, yG - 2, fill='blue', outline='blue', tag='Ghost')


def draw_ghost(xG, yG, vxG, vyG, c):
    # Функция, которая рисует тело привидения по ходу его движения,
    # т.е. до этого рисовали привидение просто как объект, а теперь - как движущееся тело
    global x, y
    draw_body(xG, yG, c)
    if vxG == 0 and vyG == 0:
        draw_stop(xG, yG)
        draw_1(xG, yG)
    else:
        if vxG > 0:
            draw_right(xG, yG)
            draw_4(xG, yG)
        elif vxG < 0:
            draw_left(xG, yG)
            draw_5(xG, yG)
        elif vyG > 0:
            draw_stop(xG, yG)
            draw_2(xG, yG)
        else:
            draw_stop(xG, yG)
            draw_3(xG, yG)
    # В зависимости от значения скорости меняется рисовка привидения.


def draw_Blinky(xB, yB, vxB, vyB):
    # Рисуем Блинки - красное привидение
    draw_ghost(xB, yB, vxB, vyB, 'red')
    move_Blinky()


def draw_Pinky(xP, yP, vxP, vyP):
    # Рисуем Пинки - розовое привидение
    draw_ghost(xP, yP, vxP, vyP, 'deep pink')
    move_Pinky()


def draw_Inky(xI, yI, vxI, vyI):
    # Рисуем Инки - голубое привидение
    draw_ghost(xI, yI, vxI, vyI, 'cyan')
    move_Inky()


def draw_Clyde(xB, yB, vxB, vyB):
    # Рисуем Клайда - оранжевое привидение
    draw_ghost(xB, yB, vxB, vyB, 'orange')
    move_Clyde()


def draw_walls():
    # Рисуем стены лабиринта
    global A  # Массив координат стен (задается в основной программе)
    for i in range(len(A)):
        canv.create_rectangle(h + A[i][0], h + A[i][1], h + A[i][2], h + A[i][3], fill='blue', outline='blue',
                              tag='wall')


def draw_lives(n):
    # Рисуем жизни в левом верхнем углу: с помощью метода create_arc() создаем желтый круг с вырезанным сектором:
    # Для этого передаем координаты квадрата, описанного вокруг круга, в start - градус начала фигуры, в extent - угол поворота
    for i in range(n):
        canv.create_arc(2 * r * i + 15, 15 + 2 * r, 2 * r * i + 15 + 2 * r, 15, start=45, extent=270, fill='yellow',
                        outline='yellow', tag='live')


def scan_pac(P):
    # Описываем действия пакмена, если он наткнется на стену - т.е. условия его остановки
    global x, y, vx, vy, h, r
    if x + vx - (r + 2) > P[0] + h and x + vx - (r + 2) < P[2] + h or x + vx + (r + 2) > P[0] + h and x + vx + (r + 2) < \
            P[2] + h or P[0] + h > x + vx - (r + 2) and P[0] + h < x + vx + (r + 2) or P[2] + h > x + vx - (r + 2) and \
            P[2] + h < x + vx + r:
        if y + vy - (r + 2) > P[1] + h and y + vy - (r + 2) < P[3] + h or y + vy + (r + 2) > P[1] + h and y + vy + (
                r + 2) < P[3] + h or P[1] + h > y + vy - (r + 2) and P[1] + h < y + vy + (r + 2) or P[
            3] + h > y + vy - (r + 2) and P[3] + h < y + vy + r:
            vx = 0
            vy = 0


def check_lives():
    # Проверяем количество оставшихся жизней, чтобы понять - перезапускать игру или выводить на экран Game Over
    global rB, rP, rI, rC, r, w, l
    if rB <= (r + 15) ** 2 or rP <= (r + 15) ** 2 or rI <= (r + 15) ** 2 or rC <= (r + 15) ** 2:
        l -= 1
        canv.create_rectangle(2 * r * l + 15, 15 + 2 * r, 2 * r * l + 15 + 2 * r, 15, fill='black')
        canv.update()
        time.sleep(2)
        if l >= 0:
            start()
            draw()
            canv.update()


def draw():
    # Перезапуск игры (следующая жизнь, если истратили)
    global l1
    canv.delete('Pac', 'Ghost')
    draw_pac()
    draw_Blinky(xB, yB, vxB, vyB)
    draw_Pinky(xP, yP, vxP, vyP)
    draw_Inky(xI, yI, vxI, vyI)
    draw_Clyde(xC, yC, vxC, vyC)
    if l1 != l:
        draw_lives(l)
        l1 = l


def start():
    # Описываем состояния привидений при запуске игры
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
    draw()
    canv.update()
    time.sleep(2)


l = 2  # Количество жизней
l1 = l  # Количество жизней при последней попытке

root.bind('<Left>', moveleft)  # Связываем нажатие на кнопку "Left" и вызов функции moveleft()
root.bind('<Right>', moveright)  # Связываем нажатие на кнопку "Right" и вызов функции moveright()
root.bind('<Up>', moveup)  # Связываем нажатие на кнопку "Up" и вызов функции moveup()
root.bind('<Down>', movedown)  # Связываем нажатие на кнопку "Down" и вызов функции movedown()

v = 1  # Скорость приведений
A = [[40, 40, 100, 80], [140, 40, 220, 80], [260, 0, 280, 80], [320, 40, 400, 80], [440, 40, 500, 80],
     [40, 120, 100, 140], [140, 120, 160, 260], [200, 120, 340, 140], [380, 120, 400, 260], [440, 120, 500, 140],
     [260, 140, 280, 200], [160, 180, 220, 200], [320, 180, 380, 200], [140, 300, 160, 380], [380, 300, 400, 380],
     [200, 360, 340, 380], [260, 380, 280, 440], [40, 420, 100, 440], [140, 420, 220, 440], [320, 420, 400, 440],
     [440, 420, 500, 440], [80, 440, 100, 500], [440, 440, 460, 500], [0, 480, 40, 500], [200, 480, 340, 500],
     [500, 480, 540, 500], [140, 480, 160, 540], [380, 480, 400, 540], [260, 500, 280, 560], [40, 540, 220, 560],
     [320, 540, 500, 560], [-20, -20, 560, 0], [-20, 600, 560, 620], [-20, 0, 0, 180], [-20, 180, 100, 200],
     [80, 200, 100, 240], [-20, 240, 100, 260], [-20, 300, 100, 320], [80, 320, 100, 360], [-20, 360, 100, 380],
     [-20, 380, 0, 600], [540, 0, 560, 180], [440, 180, 560, 200], [440, 200, 460, 240], [440, 240, 560, 260],
     [440, 300, 560, 320], [440, 320, 460, 360], [440, 360, 560, 380], [540, 380, 560, 600]]  # Массив стен
draw_walls()  # Нарисовали стены лабиринта
draw_lives(l)  # Нарисовали жизни
start()  # Нарисовали привидения в начале игры

file = open('1_level.txt')
file.read()  # Прочитали файл с лабиринтом

while l >= 0:  # Запускаем цикл обработки событий
    for i in range(len(A)):
        scan_pac(A[i])
    move_pac()
    xB += vxB  # Изменяем положения привидений
    yB += vyB  # Изменяем положения привидений
    xP += vxP  # Изменяем положения привидений
    yP += vyP  # Изменяем положения привидений
    xI += vxI  # Изменяем положения привидений
    yI += vyI  # Изменяем положения привидений
    xC += vxC  # Изменяем положения привидений
    yC += vyC  # Изменяем положения привидений
    time.sleep(0.01)  # Устанавливаем задержку перед началом следующей попытки
    a, f = 0, 1

    draw()  # Перезапуск игры
    canv.update()  # Обновление холста
    rB = (x - xB) ** 2 + (y - yB) ** 2
    rP = (x - xP) ** 2 + (y - yP) ** 2
    rI = (x - xI) ** 2 + (y - yI) ** 2
    rC = (x - xC) ** 2 + (y - yC) ** 2
    check_lives()

# Размещаем текст на холсте: указываем координаты центра текстовой надписи и ее свойства
canv.create_text((540 + 2 * h) // 2, (600 + 2 * h) // 2, text='GAME OVER', font='Times 72', justify=CENTER,
                 fill='dark red')
canv.update()

root.mainloop()
