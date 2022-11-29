from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random as rd, os, OpenGL.GLUT as glut
os.system('cls')
w, h = 600, 500

play = False
xRintangan = 50 #Rintangan Jalan Kesamping
yRintangan = 150

tr = 600
xPlayer = 0
yPlayer = 10

selesai = False

border_y = [0, 150, 0, 100]

grid_x_player = [550,0, 600,0]
grid_y_player = [0,140, 0,150]
crash_Player = False

x = 10
yRPlayer = rd.randrange(55, 65, 10)
kecepatan = 3
RKecepatan = 0.7
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
    global xRintangan, yRPlayer, xPlayer, yPlayer, crash_Player, border_y

    if not selesai:
        if y > 150:
            y = 150
        if y < 20:
            y = 20

    xRintangan -= RKecepatan
    if xRintangan < -400 and y < border_y[1] or y < border_y[0]:
        yRPlayer = rd.randrange(y -10, y +5, 10)
        # yRPlayer = rd.randrange(65, 55, 10)
        y = yRPlayer
        xRintangan = w
        y = border_y[1]
        y = border_y[0]

    if (yPlayer in range(yRPlayer-10, yRPlayer+10)) and (xRintangan < -390):
        crash_Player = True
        print("MELEDAK BOSS")
    else:
        print("ga kena")

    glTranslated(xRintangan,y,0)
    glPointSize(50)
    glBegin(GL_POINTS)
    glColor3ub(37, 188, 143) 
    glVertex2f(550+xRintangan, y) # Plyaer1 =x[150, 200, 250]
    glEnd()
    glPopMatrix()

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

def playG():
    background()
    transKota()
    jalan()
    Pembatas(160)
    Pembatas(10)
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
        xRintangan -= RKecepatan
        if crash_Player == False:
            if xRintangan < -600:
                xRintangan = 100
                yRPlayer = rd.randrange(65, 55, 10)
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
            x -= 3.5
            if x < value:
                x = cekX

            ScorePlayer += kecepatan
            if ScorePlayer % cek_Kecepatan == 0:
                Level += 1
                cekX -= 5
                cekPoint -= 5
                cek_Kecepatan += 10000
            
            if cekX < 10:
                cekX = 10

            if cekPoint < 10:
                cekPoint = 10
            
    glutTimerFunc(cekPoint,timerPlay,0)

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

def inputMouse(button, state, x,y):
    global play

    if button == GLUT_LEFT_BUTTON:
        play = True

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
    # timerRintangan(0)
    timerPlay(0)
    init()
    glutMainLoop()

Main()