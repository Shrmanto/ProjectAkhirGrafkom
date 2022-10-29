from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 1280,720

def background():
    #LANGIT
    glColor3ub(135, 206, 235)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 720)
    glVertex2f(1280, 720)
    glVertex2f(1280, 0)
    glEnd()

    #JALAN
    glColor3ub(105, 105, 105)
    glBegin(GL_QUADS)
    glVertex2f(0, 210)
    glVertex2f(1280, 210)
    glVertex2f(1280, 0)
    glVertex2f(0, 0)
    glEnd()

    #RUMPUT
    glColor3ub(50, 205, 50)
    glBegin(GL_QUADS)
    glVertex2f(0, 120)
    glVertex2f(1280, 120)
    glVertex2f(1280, 100)
    glVertex2f(0, 100)
    glEnd()
    glColor3ub(50, 205, 50)
    glBegin(GL_QUADS)
    glVertex2f(0, 220)
    glVertex2f(1280, 220)
    glVertex2f(1280, 200)
    glVertex2f(0, 200)
    glEnd()
    glColor3ub(50, 205, 50)
    glBegin(GL_QUADS)
    glVertex2f(0, 20)
    glVertex2f(1280, 20)
    glVertex2f(1280, 0)
    glVertex2f(0, 0)
    glEnd()



def iterate():
    glViewport(0, 0, 1280, 720) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    gluOrtho2D(0, 1280, 0, 720) 
    glMatrixMode (GL_MODELVIEW) 
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity()
    iterate()
    background()
    # glColor3ub(38, 38, 30)
    # square()
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
    # glutTimerFunc(50, update, 0)
    # timer(0)
    glutIdleFunc(showScreen)
    glutMainLoop()

Main()