from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random as rd, os, OpenGL.GLUT as glut
os.system('cls')
w, h = 600, 500

play = False
selesai = False
crash_Player = False

xy = 0
Cek_xy = 20

xPlayer = 0
yPlayer = 10

xRintangan = 50

border_y = [0, 150, 0, 100]
grid_y_player = [0,125, 0,150]
yRPlayer = rd.randrange(55, 65, 10)

jumlah_bintang = 1000

def drawText(ch,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  

def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = (0,0,0)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

def bg_text(fx,gy):
    glColor3ub(255, 0, 0)     
    glBegin(GL_QUADS)
    glVertex2f(285+fx,230+gy)
    glVertex2f(495+fx,230+gy)
    glVertex2f(495+fx,280+gy)
    glVertex2f(285+fx,280+gy)
    glEnd()

def drawTextNum(skor,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

def mainMenu():
    glBegin(GL_QUADS)
    glColor3ub(135, 206, 235) 
    glVertex2f(0, 0)
    glVertex2f(0, 500)
    glVertex2f(700, 500)
    glVertex2f(700, 0)
    glEnd()

    def jalan():
        glBegin(GL_QUADS)
        glColor3ub(160, 160, 160) 
        glVertex2f(0, 65)
        glVertex2f(0, 0)
        glVertex2f(700, 0)
        glVertex2f(700, 65)
        glEnd()

    def TextMenu():
        def Rivals():
            x = 0
            glTranslated(x, 0, 0)
            x += 10
            #R
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+80, 350)
            glVertex2f(x+80, 440)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+80, 440)
            glVertex2f(x+120, 440)
            glVertex2f(x+120, 440)
            glVertex2f(x+120, 400)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+80, 400)
            glVertex2f(x+120, 350)
            glVertex2f(x+120, 350)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+80, 400)
            glVertex2f(x+120, 400)
            glEnd()

            #I
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+160, 350)
            glVertex2f(x+160, 440)
            glEnd()

            #V
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+200, 440)
            glVertex2f(x+230, 350)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+230, 350)
            glVertex2f(x+260, 440)
            glEnd()

            #A
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+290, 350)
            glVertex2f(x+320, 440)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+320, 440)
            glVertex2f(x+350, 350)
            glEnd()

            #L
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+380, 350)
            glVertex2f(x+380, 440)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+380, 350)
            glVertex2f(x+430, 350)
            glEnd()

            #S
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+460, 350)
            glVertex2f(x+510, 350)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+510, 350)
            glVertex2f(x+510, 390)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+510, 390)
            glVertex2f(x+460, 390)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+460, 390)
            glVertex2f(x+460, 440)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+460, 440)
            glVertex2f(x+510, 440)
            glEnd()

        def Cars():
            x = 0
            glTranslated(x, 0, 0)
            x += 10
            #C
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+128, 250)
            glVertex2f(x+128, 320)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+128, 250)
            glVertex2f(x+180, 250)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+128, 320)
            glVertex2f(x+180, 320)
            glEnd()

            #A
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+220, 240)
            glVertex2f(x+250, 320)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+250, 320)
            glVertex2f(x+280, 240)
            glEnd()

            #R
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+320, 240)
            glVertex2f(x+320, 320)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+320, 320)
            glVertex2f(x+360, 320)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+360, 320)
            glVertex2f(x+360, 290)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+360, 290)
            glVertex2f(x+320, 290)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+320, 290)
            glVertex2f(x+360, 240)
            glEnd()

            #S
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+390, 250)
            glVertex2f(x+450, 250)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+450, 250)
            glVertex2f(x+450, 280)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+450, 280)
            glVertex2f(x+390, 280)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+390, 280)
            glVertex2f(x+390, 320)
            glEnd()
            glLineWidth(10)
            glBegin(GL_LINE_LOOP)
            glColor3ub(255, 255, 255) 
            glVertex2f(x+390, 320)
            glVertex2f(x+450, 320)
            glEnd()

        Rivals()
        Cars()

    def start_game():
        glPushMatrix()
        glColor3b(36, 150, 127)
        glBegin(GL_QUADS)
        glVertex2f(200, 100)
        glVertex2f(400, 100)
        glVertex2f(400, 160)
        glVertex2f(200, 160)
        glEnd()
        glColor3ub(0,0,0)
        glLineWidth(3)
        glBegin(GL_LINE_LOOP)
        glVertex2f(200, 100)
        glVertex2f(400, 100)
        glVertex2f(400, 160)
        glVertex2f(200, 160)
        glEnd()
        glPopMatrix()
        drawTextBold("P L A Y G A M E",235,125)
    
    jalan()
    TextMenu()
    start_game()

def GameOver():
    glPointSize(8)
    glColor3f(1.0, 1.0, 1.0) #RGB
    glBegin(GL_POINTS)
    y = 1000
    for i in range(jumlah_bintang):
        x = rd.randrange(-1000,1000)
        glVertex2f(x,y)
        if y != 1000:
            x = x
        y -= 100
    glEnd()

    def Game():
        #G
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,450)
        glVertex2f(100,450)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(100,450)
        glVertex2f(100,350)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(100,350)
        glVertex2f(200,350)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,350)
        glVertex2f(200,400)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,400)
        glVertex2f(150,400)
        glEnd()

        #A
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,350)
        glVertex2f(250,450)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(250,450)
        glVertex2f(300,350)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(225,400)
        glVertex2f(275,400)
        glEnd()

        #M
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,350)
        glVertex2f(300,450)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,450)
        glVertex2f(350,400)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(350,400)
        glVertex2f(400,450)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,450)
        glVertex2f(400,350)
        glEnd()

        #E
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,450)
        glVertex2f(500,450)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,400)
        glVertex2f(500,400)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,350)
        glVertex2f(500,350)
        glEnd()

    def Over():
        #O
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(100,330)
        glVertex2f(200,330)
        glVertex2f(200,230)
        glVertex2f(100,230)
        glVertex2f(100,230)
        glEnd()

        #V
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,330)
        glVertex2f(250,230)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(250,230)
        glVertex2f(300,330)
        glEnd()

        #E
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,330)
        glVertex2f(300,230)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,330)
        glVertex2f(400,330)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,280)
        glVertex2f(400,280)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,230)
        glVertex2f(400,230)
        glEnd()

        #R
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,330)
        glVertex2f(400,230)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,330)
        glVertex2f(500,330)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(500,330)
        glVertex2f(500,280)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(500,280)
        glVertex2f(400,280)
        glEnd()
        glColor3ub(255, 255, 255)
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,280)
        glVertex2f(500,230)
        glEnd()

    def Ulang():
        drawTextBold("M E N G U L A N G  G A M E ! !",170,150)
        drawTextBold("1. ENTER UNTUK MENGULANG",170,125)
        drawTextBold("2. ESC UNTUK EXIT GAME",170,100)
    
    Game(), Over(), Ulang()

def Mobil(cx,cy):
    global selesai, xPlayer, yPlayer

    if not selesai:
        if xPlayer > 500:
            xPlayer = 500
        if xPlayer < -0:
            xPlayer = -0
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(20+cx, 30+cy)
    glVertex2f(20+cx, 60+cy)
    glVertex2f(80+cx, 60+cy)
    glVertex2f(80+cx, 30+cy)
    glEnd()

def Rintangan(y):
    glPushMatrix()
    global xRintangan, yRPlayer, xPlayer, yPlayer, crash_Player, border_y

    if not selesai:
        if y > 150:
            y = 150
        if y < 25:
            y = 25

    xRintangan -= 0.1
    if xRintangan < -400 and y < border_y[1] or y < border_y[0]:
        yRPlayer = rd.randrange(y -15, y +10, 10)
        # y = rd.randrange(yPlayer -15, yPlayer +10, 10)
        y = yRPlayer
        xRintangan = 100

    # if (yPlayer in range(yRPlayer-10, yRPlayer+30)) and (xRintangan < -390):
    #     crash_Player = True
    #     print("MELEDAK BOSS")
    # else:
    #     print("ga kena")

    glTranslated(xRintangan,y,0)
    glPointSize(50)
    glBegin(GL_POINTS)
    glColor3ub(37, 188, 143) 
    glVertex2f(550+xRintangan, y)
    glEnd()
    glPopMatrix()

def background():
    glPushMatrix()
    glColor3ub(135, 206, 235)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 500)
    glVertex2f(700, 500)
    glVertex2f(700, 0)
    glEnd()
    glPopMatrix()

def jalan():
    glBegin(GL_QUADS) 
    glColor3ub(160,160,160)
    glVertex2f(0, 150)
    glVertex2f(0, 0)
    glVertex2f(1000, 0)
    glVertex2f(1000, 150)
    glEnd()

    def GarisTJalan(kck):
        glColor3ub(128,128,128)
        glLineWidth(30)
        glBegin(GL_LINES)
        glVertex2f(0, kck)
        glVertex2f(1000, kck)
        glEnd()

    def Tepi(tp):
        glColor3ub(50, 205, 50)
        glLineWidth(25)
        glBegin(GL_LINES)
        glVertex2f(0, tp)
        glVertex2f(1000, tp)
        glEnd()
    
    def GMidJalan(kx, ky):
        global xy, Cek_xy
        glPushMatrix()
        glTranslated(xy, 0, 0)
        glColor3ub(255, 255, 255)
        glLineWidth(15)
        glBegin(GL_LINES)
        glVertex2f(kx, ky)
        glVertex2f(kx + 70, ky)
        glEnd()
        glPopMatrix()

    def transMidJalan():
        def MidJalan1():
            GMidJalan(30, 80)
        def MidJalan2():
            GMidJalan(130, 80)
        def MidJalan3():
            GMidJalan(230, 80)
        def MidJalan4():
            GMidJalan(330, 80)
        def MidJalan5():
            GMidJalan(430, 80)
        def MidJalan6():
            GMidJalan(530, 80)
        def MidJalan7():
            GMidJalan(630, 80)
        def MidJalan8():
            GMidJalan(730, 80)
        def MidJalan9():
            GMidJalan(830, 80)
        def MidJalan10():
            GMidJalan(930, 80)
        def MidJalan11():
            GMidJalan(1030, 80)

        MidJalan1()
        MidJalan2()
        MidJalan3()
        MidJalan4()
        MidJalan5()
        MidJalan6()
        MidJalan7()
        MidJalan8()
        MidJalan9()
        MidJalan10()
        MidJalan11()

    def Pembatas(pbt):
        glColor3ub(0, 0, 0)
        glLineWidth(20)
        glBegin(GL_LINES)
        glVertex2f(0, pbt)
        glVertex2f(700, pbt)
        glEnd()

    Tepi(150)
    Pembatas(160)
    Pembatas(10)
    GarisTJalan(80)
    transMidJalan()

def kota(zx, vy):
    global xy, Cek_xy
    glPushMatrix()
    xy -= 0.1
    if xy < -400:
        xy = Cek_xy
    glTranslated(xy, 0, 0)
    glBegin(GL_QUADS) 
    glColor3ub(160,160,160) #hitam
    glVertex2f(zx + 0, 150)
    glVertex2f(zx + 0, vy+270)
    glVertex2f(zx + 100, vy+270)
    glVertex2f(zx + 100, 150)
    glEnd()
    glPopMatrix()

def transKota():
    def kota1():
        kota(0,0)
    def kota2():
        kota(115, -30)
    def kota3():
        kota(220, 45)
    def kota4():
        kota(340, -20)
    def kota5():
        kota(440, 25)
    def kota6():
        kota(570, -10)
    def kota7():
        kota(640, 10)
    def kota8():
        kota(770, 20)
    def kota9():
        kota(840, 30)
    def kota10():
        kota(940, -10)
    
    kota1()
    kota2()
    kota3()
    kota4()
    kota5()
    kota6()
    kota7()
    kota8()
    kota9()
    kota10()

def key_Mobil(key, x, y):
    global xPlayer, yPlayer, crash_Player
    if key == GLUT_KEY_UP:
        if crash_Player == False:
            if yPlayer+50 > grid_y_player[1]:
                yPlayer += 10
                crash_Player = True
            else:
                yPlayer += 10
        else:
            yPlayer += 0
    elif key == GLUT_KEY_DOWN:
        if crash_Player == False:
            if yPlayer-5 < grid_y_player[0]:
                yPlayer -= 10
                crash_Player = True
            else:
                yPlayer -= 10
        else:
            yPlayer -= 0
    elif key == GLUT_KEY_RIGHT:
        if xPlayer+50 > 600:
            xPlayer +=0
        else:
            xPlayer += 10
    elif key == GLUT_KEY_LEFT:
        if xPlayer-20 < 600:
            xPlayer -=10
        else:
            xPlayer -= 10    

def iterate():
    glViewport(0, 0, 600, 500) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 600, 0.0, 500, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    background()
    GameOver()
    # transKota()
    # jalan()

    # Mobil(xPlayer, yPlayer)

    # Rintangan(yRPlayer)
    # if play == False:
    #     mainMenu()
    # else:
    #     play_Game()
    glFlush()
    glutSwapBuffers()

def init():
    glClearColor(0.1, 0,2, 0.2)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def Main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(350, 100)
    wind = glutCreateWindow("Racing Rivals")
    glutDisplayFunc(showScreen)
    glutSpecialFunc(key_Mobil)
    glutIdleFunc(showScreen)
    # glutMouseFunc(inputMouse)
    # init()
    glutMainLoop()

Main()