def draw_walls ():
    global A
    for i in range (len (A)):
        canv.create_rectangle (h + A [i][0], h + A [i][1], h + A [i][2], h + A [i][3], fill = 'blue', outline = 'blue', tag = 'wall')
        #canv.create_text (h + (A [i][0] + A [i][2]) // 2, h + (A [i][1] + A [i][3]) // 2, text = i + 1, fill = 'white')
