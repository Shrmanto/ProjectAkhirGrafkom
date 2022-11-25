from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random as rd, os
os.system('cls')

intTransAwan = 0
w,h= 1280,720

jedag, jedug = 1,1
x = 50
kecepatan = 1
pos_x_awan = 0
pos_y_awan = 0
pos_x_gjalan = 0
pos_y_gjalan = 0
pos_x_gkota1 = 20
pos_y_gkota1 = 0
pos_x_gkota2 = 1900
pos_y_gkota2 = 0

pos_x_pemain = 0
pos_y_pemain = -500

def MainMenu():
    global jedag,jedug
    #M
    glTranslated(0,rd.randrange(-jedag,jedug),0)
    glBegin(GL_LINE_LOOP)
    glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
    glVertex2f(3.576757916323,5.5896610088214)
    glVertex2f(4.0130331519056,5.5896610088214)
    glVertex2f(4.3869833538336,4.8417606049654)
    glVertex2f(4.7609335557616,5.5896610088214)
    glVertex2f(5.2387588137807,5.5896610088214)
    glVertex2f(5.0102336903803,4.5509104479103)
    glVertex2f(5.1972087913443,4.0107601562365)
    glVertex2f(4.5947334660158,4.0107601562365)
    glVertex2f(4.6570584996705,4.6340104927832)#1
    glVertex2f(4.2623332865243,4.1977352572005)
    glVertex2f(3.950708118251,4.8002105825289)
    glVertex2f(3.7221829948505,3.9899851450183)
    glVertex2f(3.2235827256132,4.0107601562365)
    glVertex2f(3.5975329275412,4.8002105825289)
    glEnd()

def langit():
    #LANGIT
    glColor3ub(135, 206, 235)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 720)
    glVertex2f(1280, 720)
    glVertex2f(1280, 0)
    glEnd()

def Jalan():
    #JALAN
    glColor3ub(105, 105, 105)
    glBegin(GL_QUADS)
    glVertex2f(0, 210)
    glVertex2f(1280, 210)
    glVertex2f(1280, 0)
    glVertex2f(0, 0)
    glEnd()

    #RUMPUT
    #TENGAH
    # glColor3ub(50, 205, 50)
    # glBegin(GL_QUADS)
    # glVertex2f(0, 120)
    # glVertex2f(1280, 120)
    # glVertex2f(1280, 100)
    # glVertex2f(0, 100)
    # glEnd()
    #ATAS
    glColor3ub(50, 205, 50)
    glBegin(GL_QUADS)
    glVertex2f(0, 220)
    glVertex2f(1280, 220)
    glVertex2f(1280, 200)
    glVertex2f(0, 200)
    glEnd()
    #BAWAH
    glColor3ub(50, 205, 50)
    glBegin(GL_QUADS)
    glVertex2f(0, 20)
    glVertex2f(1280, 20)
    glVertex2f(1280, 0)
    glVertex2f(0, 0)
    glEnd()
    
def kotaktengah(kcx):
    glPushMatrix()
    glColor3ub(64,64,64)
    glLineWidth(30)
    glBegin(GL_LINES)
    glVertex2f(0, kcx) 
    glVertex2f(12800, kcx)
    glEnd()
    glPopMatrix()

def GarisJalan(kck, kcy):
    global x
    glTranslated(x,0,0)
    glColor3ub(255, 255, 255)
    glLineWidth(15)
    glBegin(GL_LINES)
    glVertex2f(kck, kcy)
    glVertex2f(kck + 120, kcy)
    glEnd()

def gjalan():
    global x, kecepatan
    kotaktengah(110)
    kck = 20 # y pertama dari garis mid
    for i in range(100): #garis mid dibentuk sebanyak 7 menggunakan perulangan for
        GarisJalan(kck,110)
        kck += 120

def kota1():
    global pos_x_gkota1, pos_y_gkota1
    glColor3ub(160, 160, 160)
    glTranslated(pos_x_gkota1,pos_y_gkota1,0)

    #gimana apel bisa jatuh
    pos_x_gkota1 -= kecepatan

    #kalo dah sampe bawah bikin dari atas lagi
    if pos_x_gkota1 < -1135:
        pos_x_gkota1 = -100
    #gedung 1
    glBegin(GL_QUADS)
    glVertex2f(0, 210)
    glVertex2f(0, 400)
    glVertex2f(150, 400)
    glVertex2f(150, 210)

    glVertex2f(70, 400)
    glVertex2f(100, 430)
    glVertex2f(140, 430)
    glVertex2f(140, 400)
    glEnd()

    #gedung 2
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(150, 210)
    glVertex2f(150, 340)
    glVertex2f(280, 340)
    glVertex2f(280, 210)
    glEnd()

    #gedung 3
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(300, 210)
    glVertex2f(300, 500)
    glVertex2f(500, 500)
    glVertex2f(500, 210)

    glVertex2f(320, 500)
    glVertex2f(320, 550)
    glVertex2f(370, 550)
    glVertex2f(370, 500)

    glVertex2f(370, 500)
    glVertex2f(370, 518)
    glVertex2f(400, 518)
    glVertex2f(400, 500)
    glEnd()

    #gedung 4
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(500, 210)
    glVertex2f(500, 380)
    glVertex2f(600, 380)
    glVertex2f(600, 210)
    glEnd()  

    #gedung 5
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(600, 210)
    glVertex2f(600, 450)
    glVertex2f(730, 450)
    glVertex2f(730, 210)
    glEnd() 

    #gedung 6
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(780, 210)
    glVertex2f(780, 260)
    glVertex2f(880, 260)
    glVertex2f(880, 210)

    glVertex2f(760, 260)
    glVertex2f(780, 300)
    glVertex2f(880, 300)
    glVertex2f(900, 260)
    glEnd() 

    #gedung 7
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(900, 210)
    glVertex2f(900, 400)
    glVertex2f(1020, 400)
    glVertex2f(1020, 210)
    glEnd()

    #gedung 8
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1040, 210)
    glVertex2f(1040, 450)
    glVertex2f(1150, 450)
    glVertex2f(1150, 210)
    glEnd()

    #gedung 9
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1200, 210)
    glVertex2f(1200, 400)
    glVertex2f(1320, 400)
    glVertex2f(1320, 210)
    glEnd()

    #gedung 10
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1350, 210)
    glVertex2f(1350, 500)
    glVertex2f(1500, 500)
    glVertex2f(1500, 210)
    glEnd()

    #gedung 11
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1550, 210)
    glVertex2f(1550, 550)
    glVertex2f(1750, 550)
    glVertex2f(1750, 210)
    glEnd()

    #gedung 12
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1780, 210)
    glVertex2f(1780, 260)
    glVertex2f(1860, 260)
    glVertex2f(1860, 210)

    glVertex2f(1780, 260)
    glVertex2f(1800, 300)
    glVertex2f(1840, 300)
    glVertex2f(1860, 260)
    glEnd()

    #gedung 13
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1860, 210)
    glVertex2f(1860, 400)
    glVertex2f(2000, 400)
    glVertex2f(2000, 210)
    glEnd()

    #gedung 14
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(2020, 210)
    glVertex2f(2020, 500)
    glVertex2f(2200, 500)
    glVertex2f(2200, 210)
    glEnd()

    #gedung 15
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(2200, 210)
    glVertex2f(2200, 400)
    glVertex2f(2340, 400)
    glVertex2f(2340, 210)
    glEnd()

    #gedung 0
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(-10, 210)
    glVertex2f(-10, 400)
    glVertex2f(-130, 400)
    glVertex2f(-130, 210)
    glEnd()

def kota2():
    global pos_x_gkota2, pos_y_gkota2
    glColor3ub(160, 160, 160)
    glTranslated(pos_x_gkota2,pos_y_gkota2,0)

    #gimana apel bisa jatuh
    pos_x_gkota2 -= 0.5

    #kalo dah sampe bawah bikin dari atas lagi
    if pos_x_gkota2 < -1135:
        pos_x_gkota2 = 1900
    #gedung 1
    glBegin(GL_QUADS)
    glVertex2f(0, 210)
    glVertex2f(0, 400)
    glVertex2f(150, 400)
    glVertex2f(150, 210)

    glVertex2f(70, 400)
    glVertex2f(100, 430)
    glVertex2f(140, 430)
    glVertex2f(140, 400)
    glEnd()

    #gedung 2
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(150, 210)
    glVertex2f(150, 340)
    glVertex2f(280, 340)
    glVertex2f(280, 210)
    glEnd()

    #gedung 3
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(300, 210)
    glVertex2f(300, 500)
    glVertex2f(500, 500)
    glVertex2f(500, 210)

    glVertex2f(320, 500)
    glVertex2f(320, 550)
    glVertex2f(370, 550)
    glVertex2f(370, 500)

    glVertex2f(370, 500)
    glVertex2f(370, 518)
    glVertex2f(400, 518)
    glVertex2f(400, 500)
    glEnd()

    #gedung 4
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(500, 210)
    glVertex2f(500, 380)
    glVertex2f(600, 380)
    glVertex2f(600, 210)
    glEnd()  

    #gedung 5
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(600, 210)
    glVertex2f(600, 450)
    glVertex2f(730, 450)
    glVertex2f(730, 210)
    glEnd() 

    #gedung 6
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(780, 210)
    glVertex2f(780, 260)
    glVertex2f(880, 260)
    glVertex2f(880, 210)

    glVertex2f(760, 260)
    glVertex2f(780, 300)
    glVertex2f(880, 300)
    glVertex2f(900, 260)
    glEnd() 

    #gedung 7
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(900, 210)
    glVertex2f(900, 400)
    glVertex2f(1020, 400)
    glVertex2f(1020, 210)
    glEnd()

    #gedung 8
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1040, 210)
    glVertex2f(1040, 450)
    glVertex2f(1150, 450)
    glVertex2f(1150, 210)
    glEnd()

    #gedung 9
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1200, 210)
    glVertex2f(1200, 400)
    glVertex2f(1320, 400)
    glVertex2f(1320, 210)
    glEnd()

    #gedung 10
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1350, 210)
    glVertex2f(1350, 500)
    glVertex2f(1500, 500)
    glVertex2f(1500, 210)
    glEnd()

    #gedung 11
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1550, 210)
    glVertex2f(1550, 550)
    glVertex2f(1750, 550)
    glVertex2f(1750, 210)
    glEnd()

    #gedung 12
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1780, 210)
    glVertex2f(1780, 260)
    glVertex2f(1860, 260)
    glVertex2f(1860, 210)

    glVertex2f(1780, 260)
    glVertex2f(1800, 300)
    glVertex2f(1840, 300)
    glVertex2f(1860, 260)
    glEnd()

    #gedung 13
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(1860, 210)
    glVertex2f(1860, 400)
    glVertex2f(2000, 400)
    glVertex2f(2000, 210)
    glEnd()

    #gedung 14
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(2020, 210)
    glVertex2f(2020, 500)
    glVertex2f(2200, 500)
    glVertex2f(2200, 210)
    glEnd()

    #gedung 15
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(2200, 210)
    glVertex2f(2200, 400)
    glVertex2f(2340, 400)
    glVertex2f(2340, 210)
    glEnd()

    #gedung 0
    glColor3ub(160, 160, 160)
    glBegin(GL_QUADS)
    glVertex2f(-10, 210)
    glVertex2f(-10, 400)
    glVertex2f(-130, 400)
    glVertex2f(-130, 210)
    glEnd()

def pembatas():
    #PEMBATAS
    glColor3ub(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-12800, 210)
    glVertex2f(-12800, 225)
    glVertex2f(12800, 225)
    glVertex2f(1280, 210)
    glEnd()
    glColor3ub(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-12800, 10)
    glVertex2f(-12800, 25)
    glVertex2f(12800, 25)
    glVertex2f(12800, 10)
    glEnd()

def garisjalan():
    global pos_x_gjalan, pos_y_gjalan
    glTranslated(pos_x_gjalan,pos_y_gjalan,0)

    #gimana apel bisa jatuh
    pos_x_gjalan -= 0.5

    #kalo dah sampe bawah bikin dari atas lagi
    if pos_x_gjalan < -650:
        pos_x_gjalan = 100
    #ArenaBawah
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(50, 60)
    glVertex2f(50, 80)
    glVertex2f(170, 80)
    glVertex2f(170, 60)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(300, 60)
    glVertex2f(300, 80)
    glVertex2f(420, 80)
    glVertex2f(420, 60)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(550, 60)
    glVertex2f(550, 80)
    glVertex2f(670, 80)
    glVertex2f(670, 60)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(800, 60)
    glVertex2f(800, 80)
    glVertex2f(920, 80)
    glVertex2f(920, 60)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(1050, 60)
    glVertex2f(1050, 80)
    glVertex2f(1170, 80)
    glVertex2f(1170, 60)
    glEnd()

    #ArenaAtas
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(50, 140)
    glVertex2f(50, 160)
    glVertex2f(170, 160)
    glVertex2f(170, 140)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(300, 140)
    glVertex2f(300, 160)
    glVertex2f(420, 160)
    glVertex2f(420, 140)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(550, 140)
    glVertex2f(550, 160)
    glVertex2f(670, 160)
    glVertex2f(670, 140)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(800, 140)
    glVertex2f(800, 160)
    glVertex2f(920, 160)
    glVertex2f(920, 140)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(1050, 140)
    glVertex2f(1050, 160)
    glVertex2f(1170, 160)
    glVertex2f(1170, 140)
    glEnd()

def Awan():
    global pos_x_awan, pos_y_awan
    glTranslated(pos_x_awan,pos_y_awan,0)

    #gimana apel bisa jatuh
    pos_x_awan -= kecepatan

    #kalo dah sampe bawah bikin dari atas lagi
    if pos_x_awan < -650:
        pos_x_awan = 600
    #AWAN
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(100, 450)
    glVertex2f(200, 450)
    glVertex2f(200, 500)
    glVertex2f(100, 500)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(240, 600)
    glVertex2f(280, 600)
    glVertex2f(280, 580)
    glVertex2f(240, 580)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(500, 550)
    glVertex2f(650, 550)
    glVertex2f(650, 500)
    glVertex2f(500, 500)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(850, 600)
    glVertex2f(1050, 600)
    glVertex2f(1050, 550)
    glVertex2f(850, 550)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(950, 450)
    glVertex2f(1000, 450)
    glVertex2f(1000, 400)
    glVertex2f(950, 400)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(1060, 550)
    glVertex2f(1120, 550)
    glVertex2f(1120, 520)
    glVertex2f(1060, 520)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(1160, 450)
    glVertex2f(1220, 450)
    glVertex2f(1220, 420)
    glVertex2f(1160, 420)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(800, 400)
    glVertex2f(860, 400)
    glVertex2f(860, 370)
    glVertex2f(800, 370)
    glEnd()
    glColor3ub(255, 255, 255)
    glBegin(GL_QUADS)
    glVertex2f(380, 400)
    glVertex2f(450, 400)
    glVertex2f(450, 370)
    glVertex2f(380, 370)
    glEnd()

def PointSoal():
    #POINTSOAL
    glColor3ub(211, 211, 211)
    glBegin(GL_QUADS)
    glVertex2f(630, 110)
    glVertex2f(630, 140)
    glVertex2f(650, 140)
    glVertex2f(650, 110)
    glEnd()
    glColor3ub(255, 165, 0)
    glBegin(GL_QUADS)
    glVertex2f(610, 140)
    glVertex2f(670, 140)
    glVertex2f(670, 180)
    glVertex2f(610, 180)
    glEnd()

def PoinFinish():
    #POINTSOAL
    glColor3ub(211, 211, 211)
    glBegin(GL_QUADS)
    glVertex2f(900, 110)
    glVertex2f(1000, 140)
    glVertex2f(1000, 140)
    glVertex2f(900, 110)
    glEnd()

def timer(value):
    glutPostRedisplay()
    glutTimerFunc(20, timer, 10)
    glFlush()

def iterate():
    glViewport(0, 0, 1280, 720) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    gluOrtho2D(0, 1280, 0, 720) 
    glMatrixMode (GL_MODELVIEW) 
    glLoadIdentity()

def GameMulai():
    langit()
    Jalan()
    kota1()
    # kota2()
    pembatas()
    gjalan()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    GameMulai()
    Awan()
    glFlush()
    glutSwapBuffers()

def Main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(w,h)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("Test")
    glutDisplayFunc(showScreen)
    # glutMouseFunc(iniHandleMouse)
    # glutPassiveMotionFunc(mouseFunc)
    glutTimerFunc(20, timer, 10)
    # timer(0)
    glutIdleFunc(showScreen)
    glutMainLoop()

Main()