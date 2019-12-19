def draw_body (xG, yG, c):
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
    canv.create_rectangle (xG - 10, yG - 8, xG - 2, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 8, yG - 10, xG - 4, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 8, yG - 2, xG - 4, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 8, xG + 10, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 10, xG + 8, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 2, xG + 8, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_right (xG, yG):
    canv.create_rectangle (xG - 8, yG - 8, xG, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 6, yG - 10, xG - 2, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 6, yG - 2, xG - 2, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 8, xG + 12, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 6, yG - 10, xG + 10, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 6, yG - 2, xG + 10, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_left (xG, yG):
    canv.create_rectangle (xG - 12, yG - 8, xG - 4, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 10, yG - 10, xG - 6, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG - 10, yG - 2, xG - 6, yG, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG, yG - 8, xG + 8, yG - 2, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 10, xG + 6, yG - 8, fill = 'white', outline = 'white', tag = 'Ghost')
    canv.create_rectangle (xG + 2, yG - 2, xG + 6, yG, fill = 'white', outline = 'white', tag = 'Ghost')

def draw_1 (xG, yG):
    canv.create_rectangle (xG - 8, yG - 6, xG - 4, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 6, xG + 8, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_2 (xG, yG):
    canv.create_rectangle (xG - 8, yG - 4, xG - 4, yG, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 4, xG + 8, yG, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_3 (xG, yG):
    canv.create_rectangle (xG - 8, yG - 10, xG - 4, yG - 6, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 4, yG - 10, xG + 8, yG - 6, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_4 (xG, yG):
    canv.create_rectangle (xG - 4, yG - 6, xG, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG + 8, yG - 6, xG + 12, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
#def draw_5 (xG, yG):
    #canv.create_rectangle (xG - 4, yG - 8, xG, yG - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
    #canv.create_rectangle (xG + 8, yG - 8, xG + 12, yG - 4, fill = 'blue', outline = 'blue', tag = 'Ghost')
def draw_6 (xG, yG):
    canv.create_rectangle (xG - 12, yG - 6, xG - 8, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')
    canv.create_rectangle (xG, yG - 6, xG + 4, yG - 2, fill = 'blue', outline = 'blue', tag = 'Ghost')  


def draw_ghost (xG, yG, vxG, vyG, c):
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
        
        #if x == xG:
            #draw_stop (xG, yG)
            #if y > yG:
                #draw_2 (xG, yG)
            #else:
                #draw_3 (xG, yG)
        #elif x > xG:
            #draw_right (xG, yG)
            #if y >= yG:
                #draw_4 (xG, yG)
            #else:
                #draw_5 (xG, yG)
        #else:
            #draw_left (xG, yG)
            #if y >= yG:
                #draw_6 (xG, yG)
            #else:
                #draw_7 (xG, yG)

def draw_Blinky (xB, yB, vxB, vyB):
    draw_ghost (xB, yB, vxB, vyB, 'red')
    #global xB, yB
    #draw_body (xB, yB, 'red')
    #if vxB == 0 and vyB == 0:
        #draw_stop (xB, yB)
        #draw_1 (xB, yB)
    #else:
        #if x == xB:
            #draw_stop (xB, yB)
            #if y > yB:
                #draw_2 (xB, yB)
            #else:
                #draw_3 (xB, yB)
        #elif x > xB:
            #draw_right (xB, yB)
            #if y >= yB:
                #draw_4 (xB, yB)
            #else:
                #draw_5 (xB, yB)
        #else:
            #draw_left (xB, yB)
            #if y >= yB:
                #draw_6 (xB, yB)
            #else:
                #draw_7 (xB, yB)
    move_Blinky ()

def draw_Pinky (xP, yP, vxP, vyP):
    draw_ghost (xP, yP, vxP, vyP, 'deep pink')
    move_Pinky ()

def draw_Inky (xI, yI, vxI, vyI):
    draw_ghost (xI, yI, vxI, vyI, 'cyan')
    move_Inky ()

def draw_Clyde (xB, yB, vxB, vyB):
    draw_ghost (xB, yB, vxB, vyB, 'orange')
    move_Clyde ()
