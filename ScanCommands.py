def scan_pac (P):
    global x, y, vx, vy, h, r
    #for i in range (len (A)):
    #if x - r >= Wx [0] and x - r <= Wx [1] or x + r >= Wx [0] and x + r <= Wx [1]:
        #if y - r >= Wy [0] and y - r <= Wy [1] or y + r >= Wy [0] and y + r <= Wy [1]:
            #if vx > 0:
                #vx = 0
                #x -= 2
            #elif vx < 0:
                #vx = 0
                #x += 2
            #if vy > 0:
                #vy = 0
                #y -= 2
            #elif vy < 0:
                #vy = 0
                #y += 2
        #else:
            #if Wx [0] >= x - r and Wx [0] <= x + r or Wx [1] >= x - r and Wx [1] <= x + r:
                #if Wy [0] >= y - r and Wy [0] <= y + r or Wy [1] >= y - r and Wy [1] <= y + r:
                    #vx = -vx
                    #vy = -vy
                    #if vx > 0:
                        #vx = 0
                        #x -= 2
                    #elif vx < 0:
                        #vx = 0
                        #x += 2
                    #if vy > 0:
                        #vy = 0
                        #y -= 2
                    #elif vy < 0:
                        #vy = 0
                        #y += 2
    #else:
        #if Wx [0] >= x - r and Wx [0] <= x + r or Wx [1] >= x - r and Wx [1] <= x + r:
            #if Wy [0] >= y - r and Wy [0] <= y + r or Wy [1] >= y - r and Wy [1] <= y + r:
                #if vx > 0:
                    #vx = 0
                    #x -= 2
                #elif vx < 0:
                    #vx = 0
                    #x += 2
                #if vy > 0:
                    #vy = 0
                    #y -= 2
                #elif vy < 0:
                    #vy = 0
                    #y += 2
    if x - r > P [0] + h and x - r < P [2] + h or x + r > P [0] + h and x + r < P [2] + h or P [0] + h > x - r and P [0] + h < x + r or P [2] + h > x - r and P [2] + h < x + r:
        if y - r > P [1] + h and y - r < P [3] + h or y + r > P [1] + h and y + r < P [3] + h or P [1] + h > y - r and P [1] + h < y + r or P [3] + h > y - r and P [3] + h < y + r:
    
    #if ((x - r) - (P [2] + h)) * ((x + r) - (P [0] + h)) <= 0 and ((y - r) - (P [3] + h)) * ((y + r) - (P [1] + h)) <= 0:
            print (x, y)
            #vx = 0
            #vy = 0
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
            #if vx > 0:
                #vx = 0
                #x -= 2
            #elif vx < 0:
                #vx = 0
                #x += 2
            #elif vy > 0:
                #vy = 0
                #y -= 2
            #elif vy < 0:
                #vy = 0
                #y += 2

def scan_pac_f (P):
    global x, y, vx, vy, h, r
    #if ((x + vx - r) - (P [2] + h)) * ((x + vx + r) - (P [0] + h)) <= 0 and ((y + vy - r) - (P [3] + h)) * ((y + vy + r) - (P [1] + h)) <= 0:
    if x + vx - (r + 2) > P [0] + h and x + vx - (r + 2) < P [2] + h or x + vx + (r + 2) > P [0] + h and x + vx + (r + 2) < P [2] + h or P [0] + h > x + vx - (r + 2) and P [0] + h < x + vx + (r + 2) or P [2] + h > x + vx - (r + 2) and P [2] + h < x + vx + r:
        if y + vy - (r + 2) > P [1] + h and y + vy - (r + 2) < P [3] + h or y + vy + (r + 2) > P [1] + h and y + vy + (r + 2) < P [3] + h or P [1] + h > y + vy - (r + 2) and P [1] + h < y + vy + (r + 2) or P [3] + h > y + vy - (r + 2) and P [3] + h < y + vy + r:
            #print (x, y)
            vx = 0
            vy = 0

def scan_pac_f_1 (P):
    global x, y, vx, vy, h, r
    if ((x + vx - 20) - (P [2] + h)) * ((x + vx + 20) - (P [0] + h)) <= 0 and ((y + vy - 20) - (P [3] + h)) * ((y + vy + 20) - (P [1] + h)) <= 0:
        #print (x, y)
        vx = 0
        vy = 0

def draw_lives (n):
    for i in range (n):
        canv.create_arc (2 * r * i + 15, 15 + 2 * r, 2 * r * i + 15 + 2 * r, 15, start = 45, extent = 270, fill = 'yellow', outline = 'yellow', tag = 'live')

def check_lives ():
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
