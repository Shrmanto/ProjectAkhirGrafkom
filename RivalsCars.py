from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random as rd, os, OpenGL.GLUT as glut, math
os.system('cls')
w, h = 600, 500

play = False
selesai = False
crash_Player = False

xy = 0
xc = 0
Cek_xy = 20

xPlayer = 0
yPlayer = 35

xMusuh = 0
yMusuh = 0

xRintangan = 50

grid_y_player = [0,125, 0,120]
yRPlayer = rd.randrange(50, 200)

jumlah_bintang = 1000
jedag, jedug = 1, 1

ScorePlayer = 0
kecepatan = 1

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
    
    jalan(), TextMenu(), start_game()

def GameOver():
    def kelapKelip():
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
        global jedag, jedug
        #G
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,450)
        glVertex2f(100,450)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(100,450)
        glVertex2f(100,350)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(100,350)
        glVertex2f(200,350)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,350)
        glVertex2f(200,400)
        glEnd()
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glLineWidth(10)     
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,400)
        glVertex2f(150,400)
        glEnd()

        #A
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,350)
        glVertex2f(250,450)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(250,450)
        glVertex2f(300,350)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(225,400)
        glVertex2f(275,400)
        glEnd()

        #M
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,350)
        glVertex2f(300,450)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,450)
        glVertex2f(350,400)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(350,400)
        glVertex2f(400,450)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,450)
        glVertex2f(400,350)
        glEnd()

        #E
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,450)
        glVertex2f(500,450)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,400)
        glVertex2f(500,400)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,350)
        glVertex2f(500,350)
        glEnd()

    def Over():
        #O
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(100,330)
        glVertex2f(200,330)
        glVertex2f(200,230)
        glVertex2f(100,230)
        glVertex2f(100,230)
        glEnd()

        #V
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(200,330)
        glVertex2f(250,230)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(250,230)
        glVertex2f(300,330)
        glEnd()

        #E
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,330)
        glVertex2f(300,230)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,330)
        glVertex2f(400,330)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,280)
        glVertex2f(400,280)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(300,230)
        glVertex2f(400,230)
        glEnd()

        #R
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,330)
        glVertex2f(400,230)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,330)
        glVertex2f(500,330)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(500,330)
        glVertex2f(500,280)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(500,280)
        glVertex2f(400,280)
        glEnd()
        glLineWidth(10)     
        glTranslated(0,rd.randrange(-jedag,jedug),0)
        glColor3f(rd.uniform(0.5,1),rd.uniform(0.5,1),rd.uniform(0.5,1))
        glBegin(GL_LINE_LOOP)
        glVertex2f(400,280)
        glVertex2f(500,230)
        glEnd()

    def Ulang():
        # drawTextBold("E N T E R  U N T U K  M E N G U L A N G",130,125)
        drawTextBold("Crate by Kelompok GrafKom",180,10)
    
    kelapKelip(), Ulang(), Game(), Over()

def Player(cx, cy):
    global xPlayer, yPlayer, xMusuh, yMusuh, crash_Player, yRPlayer

    # if xPlayer==xMusuh and yPlayer-50<=yMusuh<=yPlayer+50:
    #     crash_Player = True
    # if yPlayer in range(yRPlayer-50, yRPlayer+50) and xMusuh < -390:
        # crash_Player = True
    # glScaled(0.8, 0.8, 0)
    def circle1(cx,cy,r,num_segment):
        glBegin(GL_POLYGON)
        glColor3ub(96,96,96)
        for i in range(num_segment):
            theta= 2 *3.1415926*i/num_segment
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + cx, y + cy)
        glEnd()

    def circle2(cx,cy,r,num_segment):
        glBegin(GL_POLYGON)
        glColor3ub(96,96,96)
        for i in range(num_segment):
            theta= 2 *3.1415926*i/num_segment
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + cx, y + cy)
        glEnd()

    def circle3(cx,cy,r,num_segment):
        glBegin(GL_POLYGON)
        glColor3ub(255,255,255)
        for i in range(num_segment):
            theta= 2 *3.1415926*i/num_segment
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + cx, y + cy)
        glEnd()

    def circle4(cx,cy,r,num_segment):
        glBegin(GL_POLYGON)
        glColor3ub(255,255,255)
        for i in range(num_segment):
            theta= 2 *3.1415926*i/num_segment
            x = r * math.cos(theta)
            y = r * math.sin(theta)
            glVertex2f(x + cx, y + cy)
        glEnd()
    #bodyBelakang
    glColor3ub(255, 255, 0)
    glBegin(GL_POLYGON)
    glVertex2f(22+cx, 48+cy)#S
    glVertex2f(22+cx, 42+cy)#R
    glVertex2f(28+cx, 34+cy)#Q
    glVertex2f(40+cx, 28+cy)#P
    glVertex2f(45+cx, 28+cy)#O
    glVertex2f(65+cx, 28+cy)#G1
    glVertex2f(70+cx, 26+cy)#h1
    glVertex2f(98+cx, 26+cy)#a3
    glVertex2f(98+cx, 74+cy)#b3
    glVertex2f(69+cx, 74+cy)#e1
    glVertex2f(60+cx, 70+cy)#d1
    glVertex2f(45+cx, 60+cy)#c1
    glVertex2f(33+cx, 53+cy)#b1
    glVertex2f(26+cx, 53+cy)#w
    glVertex2f(25+cx, 53+cy)#v
    glVertex2f(24+cx, 52+cy)#u
    glVertex2f(24+cx, 48+cy)#t
    #bodyDepan
    glVertex2f(98+cx, 26+cy)#a3 
    glVertex2f(140+cx, 26+cy)#i1
    glVertex2f(161+cx, 26+cy)#m1
    glVertex2f(190+cx, 26+cy)#n1
    glVertex2f(194+cx, 27+cy)#z1
    glVertex2f(197+cx, 31+cy)#w1
    glVertex2f(193+cx, 30+cy)#v1
    glVertex2f(197+cx, 42+cy)#u1
    glVertex2f(196+cx, 44+cy)#t1
    glVertex2f(192+cx, 46+cy)#s1
    glVertex2f(193+cx, 49+cy)#r1
    glVertex2f(193+cx, 53+cy)#q1
    glVertex2f(186+cx, 56+cy)#p1
    glVertex2f(155+cx, 59+cy)#o1
    glVertex2f(146+cx, 63+cy)#k1
    glVertex2f(134+cx, 72+cy)#j1
    glVertex2f(129+cx, 74+cy)#f1
    glVertex2f(98+cx, 74+cy)#b3
    glEnd()
    #kacaDepan
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(134+cx, 72+cy)#j1
    glVertex2f(129+cx, 72+cy)#a2 
    glVertex2f(148+cx, 56+cy)#b2
    glVertex2f(155+cx, 59+cy)#o1
    glVertex2f(146+cx, 63+cy)#k1
    glEnd()
    glColor3ub(0, 0, 0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(134+cx, 72+cy)#j1
    glVertex2f(129+cx, 72+cy)#a2 
    glVertex2f(148+cx, 56+cy)#b2
    glVertex2f(129+cx, 72+cy)#a2 
    glVertex2f(148+cx, 56+cy)#b2
    glVertex2f(155+cx, 59+cy)#o1
    glVertex2f(146+cx, 63+cy)#k1
    glEnd()
    #kacaPintuDepan
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(125+cx, 72+cy)#c2
    glVertex2f(136+cx, 63+cy)#d2 
    glVertex2f(143+cx, 55+cy)#e2
    glVertex2f(99+cx, 55+cy)#d3
    glVertex2f(98+cx, 72+cy)#j2
    glEnd()
    glColor3ub(0, 0, 0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(125+cx, 72+cy)#c2
    glVertex2f(125+cx, 72+cy)#c2
    glVertex2f(136+cx, 63+cy)#d2 
    glVertex2f(136+cx, 63+cy)#d2 
    glVertex2f(143+cx, 55+cy)#e2
    glVertex2f(99+cx, 55+cy)#d3
    glVertex2f(98+cx, 72+cy)#j2
    glVertex2f(98+cx, 72+cy)#j2
    glEnd()
    #kacaPintuDBelakang
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(70+cx, 72+cy)#r2
    glVertex2f(94+cx, 72+cy)#k2 
    glVertex2f(95+cx, 56+cy)#c3
    glVertex2f(50+cx, 56+cy)#p2
    glVertex2f(65+cx, 69+cy)#q2
    glEnd()
    glColor3ub(0, 0, 0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(70+cx, 72+cy)#r2
    glVertex2f(94+cx, 72+cy)#k2 
    glVertex2f(94+cx, 72+cy)#k2 
    glVertex2f(95+cx, 56+cy)#c3
    glVertex2f(95+cx, 56+cy)#c3
    glVertex2f(50+cx, 56+cy)#p2
    glVertex2f(50+cx, 56+cy)#p2
    glVertex2f(65+cx, 69+cy)#q2
    glEnd()
    #PintuDepan
    glColor3ub(255, 255, 153)
    glBegin(GL_POLYGON)
    glVertex2f(99+cx, 55+cy)#d3
    glVertex2f(143+cx, 55+cy)#e2
    glVertex2f(143+cx, 33+cy)#f2
    glVertex2f(141+cx, 28+cy)#g2
    glVertex2f(98+cx, 28+cy)#h2
    glVertex2f(100+cx, 50+cy)#i2
    glEnd()
    glColor3ub(0, 0, 0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(99+cx, 55+cy)#d3
    glVertex2f(100+cx, 50+cy)#i2
    glVertex2f(100+cx, 50+cy)#i2
    glVertex2f(98+cx, 28+cy)#h2

    glVertex2f(143+cx, 55+cy)#e2
    glVertex2f(143+cx, 33+cy)#f2
    glVertex2f(143+cx, 33+cy)#f2
    glVertex2f(141+cx, 28+cy)#g2
    glEnd()
    #PintuBelakang
    glColor3ub(255, 255, 153)
    glBegin(GL_POLYGON)
    glVertex2f(50+cx, 56+cy)#p2
    glVertex2f(95+cx, 56+cy)#c3
    glVertex2f(96+cx, 49+cy)#l2
    glVertex2f(94+cx, 29+cy)#m2
    glVertex2f(64+cx, 29+cy)#n2
    glVertex2f(50+cx, 50+cy)#o2
    glEnd()
    glColor3ub(0, 0, 0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(95+cx, 56+cy)#c3
    glVertex2f(96+cx, 49+cy)#l2
    glVertex2f(96+cx, 49+cy)#l2
    glVertex2f(94+cx, 29+cy)#m2

    glVertex2f(50+cx, 56+cy)#p2
    glVertex2f(50+cx, 50+cy)#o2
    glVertex2f(50+cx, 50+cy)#o2
    glVertex2f(64+cx, 29+cy)#n2
    glEnd()

    #LampuDepan
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(192+cx, 46+cy)#s1
    glVertex2f(193+cx, 49+cy)#r1
    glVertex2f(193+cx, 53+cy)#q1
    glVertex2f(182+cx, 53+cy)#s2
    glVertex2f(180+cx, 50+cy)#t2
    glVertex2f(183+cx, 46+cy)#u2
    glEnd()
    #LampuBelakang
    glColor3ub(255, 255, 255)
    glBegin(GL_POLYGON)
    glVertex2f(24+cx, 52+cy)#u
    glVertex2f(24+cx, 48+cy)#t
    glVertex2f(30+cx, 48+cy)#z2
    glVertex2f(32+cx, 50+cy)#w2
    glVertex2f(32+cx, 52+cy)#v2
    glEnd()

    #BodyKitBawah
    glColor3ub(255, 153, 51)
    glBegin(GL_POLYGON)
    glVertex2f(40+cx, 28+cy)#P
    glVertex2f(45+cx, 28+cy)#O
    glVertex2f(65+cx, 28+cy)#G1
    glVertex2f(70+cx, 26+cy)#h1
    glVertex2f(98+cx, 26+cy)#a3
    glVertex2f(140+cx, 26+cy)#i1
    glVertex2f(161+cx, 26+cy)#m1
    glVertex2f(190+cx, 26+cy)#n1
    glVertex2f(194+cx, 27+cy)#z1
    glVertex2f(197+cx, 31+cy)#w1
    glVertex2f(193+cx, 30+cy)#v1
    glVertex2f(36+cx, 30+cy)#e3
    glEnd()

    circle1(55+cx,32+cy,12,360)
    circle3(55+cx,32+cy,7,360)
    circle2(150+cx,32+cy,12,360)
    circle4(150+cx,32+cy,7,360)

def Musuh(dx, dy):
    global xMusuh, yMusuh, yRPlayer, selesai, crash_Player, yPlayer, xPlayer

    # if not selesai:
    #     if dy > 200:
    #         dy = 200
    #     if dy < 110:
    #         dy = 110
    
    # xMusuh -= 2
    # if xMusuh < -600:
    #     yRPlayer = rd.randrange(yMusuh -150, yMusuh +75)
    #     yMusuh = yRPlayer
    #     xMusuh = 500

    # if yPlayer in range(yRPlayer-50, yRPlayer+50) and xMusuh < -390:
    #     crash_Player = True

    glColor3ub(37, 188, 143) 
    glBegin(GL_QUADS)
    glVertex2f(570+dx, 20+dy)#f3
    glVertex2f(620+dx, 20+dy)#g3
    glVertex2f(620+dx, 60+dy)#h1
    glVertex2f(570+dx, 60+dy)#i1
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

    Tepi(150), Pembatas(160), Pembatas(10), GarisTJalan(80), transMidJalan()

def kota(zx, vy):
    global xy, Cek_xy
    glPushMatrix()
    xy -= 0.5
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
    
    kota1(), kota2(),kota3(),kota4(),kota5(),kota6(),kota7(),kota8(),kota9(),kota10()

def salju():
    glPointSize(15)
    glColor3f(1.0, 1.0, 1.0) #RGB
    glBegin(GL_POINTS)
    y = 1000
    for i in range(jumlah_bintang):
        x = rd.randrange(-1000,1000)
        glVertex2f(x,y)
        if y != 1000:
            x = x
        y -= 50
    glEnd()

def Score_Player():
    drawText('SCORE : ',15,480,0,0,0)
    drawTextNum(ScorePlayer,15,460,0,0,0) 

def collisionMusuh():
    global yPlayer, yRPlayer, xMusuh, yMusuh, crash_Player
    
    xMusuh -= 2
    if xMusuh < -600:
        yRPlayer = rd.randrange(yMusuh -150, yMusuh +75)
        yMusuh = yRPlayer
        xMusuh = 500
        
    if yPlayer in range(yRPlayer-50, yRPlayer+50) and xMusuh < -390:
        crash_Player = True

    if not selesai:
        if yMusuh > 150:
            yMusuh = 150
        if yMusuh < 10:
            yMusuh = 10

def key_Mobil(key, x, y):
    global xPlayer, yPlayer, crash_Player, play
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
            xPlayer += 0
    elif key == GLUT_KEY_LEFT:
        if xPlayer-20 < 0:
            xPlayer -=0
        else:
            xPlayer -= 0

    # elif ord(key) == ord(b'\r'):
    #     play = False

    #     # crash_Player = False  

def inputMouse(button, state, x,y):
    global play

    if button == GLUT_LEFT_BUTTON:
        # if (x >= 200 and x <= 400) and (y >= 100 and y <=160):
        play = True

def playG():
    background()
    transKota()
    salju()
    Score_Player()
    jalan()
    # MobilPlayer(xPlayer, yPlayer)
    # Mobil(xPlayer, yPlayer)
    Player(xPlayer, yPlayer)
    Musuh(xMusuh, yMusuh)
    collisionMusuh()

def play_Game():
    global ScorePlayer, kecepatan, cek_Kecepatan
    if crash_Player == False:
        playG()
        # Musuh(xMusuh, yRPlayer)
        # Rintangan(yRPlayer)
        ScorePlayer += kecepatan

    if crash_Player == True:
        GameOver()

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
    glutKeyboardFunc(key_Mobil)
    glutIdleFunc(showScreen)
    glutMouseFunc(inputMouse)
    init()
    glutMainLoop()

Main()