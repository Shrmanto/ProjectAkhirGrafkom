from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random as rd, os, OpenGL.GLUT as glut
os.system('cls')
w, h = 600, 500

xPlayer = 0
yPlayer = 10

grid_player = [0,700, 0,150]
crash_Player = False

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

def bg_text(x,y):
    glColor3ub(255, 0, 0)     
    glBegin(GL_QUADS)
    glVertex2f(285+x,230+y)
    glVertex2f(495+x,230+y)
    glVertex2f(495+x,280+y)
    glVertex2f(285+x,280+y)
    glEnd()

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

def kota():
    pass

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

def Pembatas(pbt):
    glColor3ub(0, 0, 0)
    glLineWidth(25)
    glBegin(GL_LINES)
    glVertex2f(0, pbt)
    glVertex2f(700, pbt)
    glEnd()

def GMidJalan(kx, ky):
    glColor3ub(255, 255, 255)
    glLineWidth(15)
    glBegin(GL_LINES)
    glVertex2f(kx, ky)
    glVertex2f(kx + 70, ky)
    glEnd()

def Mobil(x,y):
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(20+x, 30+y)
    glVertex2f(20+x, 60+y)
    glVertex2f(80+x, 60+y)
    glVertex2f(80+x, 30+y)
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

def play():
    background()
    jalan()
    GarisTJalan(80)
    Tepi(150)
    Pembatas(160)
    Pembatas(10)
    kx = 10
    for i in range(10):
        GMidJalan(kx, 80)
        kx += 100

    Mobil(xPlayer, yPlayer)

def play_Game():
    if crash_Player == False:
        play()
    
    if crash_Player == True:
        bg_text(-40,0)
        drawTextBold("G A M E O V E R",260,255)
        drawText("Enter To Play",280,236,38, 33, 98)

def iterate():
    glViewport(0, 0, 600, 600) #utk mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 650, 0.0, 500, 0.0, 1.0) #utk mengatur berapa blok yang digunakan (skala) nilai x, y, z
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    play_Game()
    glFlush()
    glutSwapBuffers()

def init():
    glClearColor(0.1, 0,2, 0.2)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def Main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(100, 100)
    wind = glutCreateWindow("Racing Rivals")
    glutDisplayFunc(showScreen)
    glutSpecialFunc(key_Mobil)
    # glutMouseFunc(input_untuk_mouse)
    # glutPassiveMotionFunc(mouseFunc)
    # glutTimerFunc(20, timer, 10)
    # timer(20)
    init()
    glutIdleFunc(showScreen)
    glutMainLoop()

Main()