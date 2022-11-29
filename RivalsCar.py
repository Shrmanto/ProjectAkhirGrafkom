from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random as rd, os, OpenGL.GLUT as glut
os.system('cls')
w, h = 600, 500

play = False
xRintangan = 150 #Rintangan Jalan Kesamping
tr = 600
xPlayer = 0
yPlayer = 10

border_y = [0, 150, 0, 100]

grid_player = [0,140, 0,150]
crash_Player = False

x = 10
yRPlayer = rd.randrange(55, 65)
kecepatan = 10
RKecepatan = 0.6
cekPoint = 30
cekX = 10
cek_Kecepatan = 5000

ScorePlayer = 0
Level = 1

cekLev = 1


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

def kota(zx, vy):
    glPushMatrix()
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
    
    kota1()
    kota2()
    kota3()
    kota4()
    kota5()
    kota6()

def jalan():
    glPushMatrix()
    glBegin(GL_QUADS) 
    glColor3ub(160,160,160) #hitam
    glVertex2f(0, 150)
    glVertex2f(0, 0)
    glVertex2f(700, 0)
    glVertex2f(700, 150)
    glEnd()
    glPopMatrix()

    def GarisTJalan(kck):
        glColor3ub(128,128,128)
        glLineWidth(30)
        glBegin(GL_LINES)
        glVertex2f(0, kck)
        glVertex2f(700, kck)
        glEnd()

    def Tepi(tp):
        glColor3ub(50, 205, 50)
        glLineWidth(25)
        glBegin(GL_LINES)
        glVertex2f(0, tp)
        glVertex2f(700, tp)
        glEnd()
    
    GarisTJalan(80)
    Tepi(150)

def Pembatas(pbt):
    glColor3ub(0, 0, 0)
    glLineWidth(20)
    glBegin(GL_LINES)
    glVertex2f(0, pbt)
    glVertex2f(700, pbt)
    glEnd()

def GMidJalan(kx, ky):
    global x, kecepatan, cekX
    glTranslated(x, 0, 0)
    # x -= kecepatan
    # if x < -w:
    #     x = cekX
    glColor3ub(255, 255, 255)
    glLineWidth(15)
    glBegin(GL_LINES)
    glVertex2f(kx, ky)
    glVertex2f(kx + 70, ky)
    glEnd()

def Rintangan(y):
    glPushMatrix()
    global xRintangan, yRPlayer, xPlayer, yPlayer, crash_Player, border_y, border__y

    xRintangan -= RKecepatan
    if xRintangan < -400 and y < border_y[1] or y < border_y[0]:
        yRPlayer = rd.randrange(y -30, y +10)
        xRintangan = w

    glTranslated(xRintangan,y,0)
    glPointSize(50)
    glBegin(GL_POINTS)
    glColor3ub(37, 188, 143) 
    glVertex2f(550+xRintangan, y) # Plyaer1 =x[150, 200, 250]
    glEnd()
    glPopMatrix()

def Mobil(cx,cy):
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(20+cx, 30+cy)
    glVertex2f(20+cx, 60+cy)
    glVertex2f(80+cx, 60+cy)
    glVertex2f(80+cx, 30+cy)
    glEnd()

def key_Mobil(key, x, y):
    global xPlayer, yPlayer, crash_Player
    if key == GLUT_KEY_UP:
        if crash_Player == False:
            if yPlayer+50 > grid_player[1]:
                yPlayer += 10
                crash_Player = True
            else:
                yPlayer += 10
        else:
            yPlayer += 0
    elif key == GLUT_KEY_DOWN:
        if crash_Player == False:
            if yPlayer-5 < grid_player[0]:
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

def inputMouse(button, state, x,y):
    global play

    if button == GLUT_LEFT_BUTTON:
        play = True

def mainMenu():
    glBegin(GL_QUADS)
    glColor3ub(135, 206, 235) 
    glVertex2f(0, 0)
    glVertex2f(0, 500)
    glVertex2f(700, 500)
    glVertex2f(700, 0)
    glEnd()

    def Rivals():
        #R
        glLineWidth(10)
        glPointSize(5)
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(120, 350)
        glVertex2f(120, 440)
        glVertex2f(170, 440)
        glVertex2f(180, 420)
        glVertex2f(160, 400)
        glVertex2f(138, 400)
        glVertex2f(169, 369)
        glVertex2f(150, 357)
        glVertex2f(130, 389)
        glVertex2f(140, 350)
        glEnd()

        #I
        glLineWidth(10)
        glPointSize(5)
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(190, 350)
        glVertex2f(197, 382)
        glVertex2f(190, 440)
        glVertex2f(220, 440)
        glVertex2f(215, 350)
        glEnd()

        #V
        glLineWidth(10)
        glPointSize(5)
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(257, 350)
        glVertex2f(232, 440)
        glVertex2f(262, 433)
        glVertex2f(266, 380)
        glVertex2f(282, 375)
        glVertex2f(282, 440)
        glVertex2f(312, 440)
        glVertex2f(293, 354)
        glEnd()

        #A
        glLineWidth(10)
        glPointSize(5)
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(310, 350)
        glVertex2f(328, 437)
        glVertex2f(358, 436)
        glVertex2f(383, 354)
        glVertex2f(367, 351)
        glVertex2f(362, 380)
        glVertex2f(335, 380)
        glVertex2f(338, 353)
        glEnd()

        #L
        glLineWidth(10)
        glPointSize(5)
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(391, 350)
        glVertex2f(385, 438)
        glVertex2f(406, 437)
        glVertex2f(401, 366)
        glVertex2f(425, 370)
        glVertex2f(426, 350)
        glEnd()

        #S
        glLineWidth(10)
        glPointSize(5)
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(426, 350)
        glVertex2f(472, 370)
        glVertex2f(478, 387)
        glVertex2f(440, 397)
        glVertex2f(432, 411)
        glVertex2f(438, 435)
        glVertex2f(480, 435)
        glVertex2f(483, 437)
        glVertex2f(445, 426)
        glVertex2f(452, 410)
        glVertex2f(483, 405)
        glVertex2f(493, 376)
        glVertex2f(477, 353)
        glVertex2f(440, 352)
        glEnd()

    def Cars():
        #C
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(212, 230)
        glVertex2f(164, 239)
        glVertex2f(138, 260)
        glVertex2f(150, 300)
        glVertex2f(196, 320)
        glVertex2f(232, 310)
        glVertex2f(167, 290)
        glVertex2f(172, 255)
        glVertex2f(231, 252)
        glEnd()

        #A
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(242, 235)#
        glVertex2f(258, 320)#
        glVertex2f(287, 321)#
        glVertex2f(305, 240)#
        glVertex2f(284, 231)#
        glVertex2f(281, 269)#
        glVertex2f(265, 270)#
        glVertex2f(260, 235)#
        glEnd()

        glBegin(GL_QUADS)
        glColor3ub(135, 206, 235)
        glVertex2f(260, 235)
        glVertex2f(365, 270)
        glVertex2f(281, 269)
        glVertex2f(284, 231)
        glEnd()

        #R
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(315, 230)#
        glVertex2f(315, 318)#
        glVertex2f(351, 325)#
        glVertex2f(365, 308)#
        glVertex2f(356, 289)#
        glVertex2f(336, 285)#
        glVertex2f(380, 245)#
        glVertex2f(356, 236)#
        glVertex2f(333, 268)#
        glVertex2f(336, 236)#
        glEnd()
        glBegin(GL_QUADS)
        glColor3ub(135, 206, 235)
        glVertex2f(336, 236)
        glVertex2f(333, 268)
        glVertex2f(356, 236)
        glVertex2f(336, 232)
        glEnd()

        #S
        glBegin(GL_POLYGON)
        glColor3ub(255, 255, 255) 
        glVertex2f(387, 261)#
        glVertex2f(426, 254)#
        glVertex2f(428, 272)#
        glVertex2f(384, 276)#
        glVertex2f(378, 288)#
        glVertex2f(385, 315)#
        glVertex2f(445, 326)#
        glVertex2f(450, 300)#
        glVertex2f(404, 307)#
        glVertex2f(400, 290)#
        glVertex2f(452, 280)#
        glVertex2f(450, 250)#
        glVertex2f(394, 234)#
        glEnd()
        glBegin(GL_QUADS)
        glColor3ub(135, 206, 235)
        glVertex2f(453, 280)
        glVertex2f(400, 290)
        glVertex2f(404, 307)
        glVertex2f(450, 300)
        glEnd()
        glBegin(GL_QUADS)
        glColor3ub(135, 206, 235)
        glVertex2f(387, 261)
        glVertex2f(426, 254)
        glVertex2f(427, 272)
        glVertex2f(382, 276)
        glEnd()

    Rivals()
    Cars()

def playG():
    background()
    transKota()
    jalan()
    # GarisTJalan(80)
    # Tepi(150)
    Pembatas(160)
    Pembatas(10)
    # Rintangan()
    Mobil(xPlayer, yPlayer)
    drawText('SCORE 1: ',15,460,0,0,0) #player 1
    drawTextNum(ScorePlayer,25,440,0,0,0) # player 1
    drawText('LEVEL : ',15,420,0,0,0)
    drawTextNum(Level,25,400,0,0,0)
    kx = 20
    for i in range(10):
        GMidJalan(kx, 80)
        kx += 100

def play_Game():
    if crash_Player == False:
        playG()
        Rintangan(yRPlayer)
    
    if crash_Player == True:
        bg_text(-50,-50)
        drawTextBold("G A M E O V E R",260,200)

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
    if play == False:
        mainMenu()
    else:
        play_Game()
    glFlush()
    glutSwapBuffers()

def timerRintangan(value):
    global xRintangan, yRPlayer, crash_Player, cekLev, tr
    if play == True:
        xRintangan -= 20
        # if crash_Player == False:
        #     if xRintangan < -w:
        #         xRintangan = w
        # if crash_Player == False:
        #     if xRintangan < -550:
        #         cekLev += 1
        #         xRintangan = 100
        #         yRPlayer = yRPlayer
        #     if (cekLev %2) == 0:
        #         tr-=100
        #     if tr <100:
        #         tr = 100
            # if (yPlayer in range(yRPlayer-50,yRPlayer+20))and(xRintangan < -390):
            #     crash_Player = True
    glutTimerFunc(tr, timerRintangan,0)

def timerPlay(value):
    global x, kecepatan, cekPoint, cek_Kecepatan, Level, ScorePlayer, cekX
    if play == True:
        if crash_Player == False:
            x -= kecepatan
            if x < -value:
                x = cekX
            # ScorePlayer += kecepatan

            # if ScorePlayer % cek_Kecepatan == 0:
            #     Level += 1
            #     cekX -= 5
            #     cekPoint -= 5
            #     cek_Kecepatan += 10000
            
            # if cekX < 20:
            #     cekX = 20

            # if cekPoint < 10:
            #     cekPoint = 10
            
    glutTimerFunc(cekPoint,timerPlay,0)

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
    glutMouseFunc(inputMouse)
    # glutPassiveMotionFunc(mouseFunc)
    # glutTimerFunc(tr, timerRintangan, 0)
    # timerPlay(0)
    # timerRintangan(0)
    init()
    glutMainLoop()

Main()