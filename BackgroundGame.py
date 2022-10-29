from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 1280,720

def background():
    glColor3ub(135, 206, 235)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 720)
    glVertex2f(1280, 720)
    glVertex2f(1280, 0)
    glEnd()

def iterate():
    glViewport(0, 0, 1280, 720) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()
    gluOrtho2D(-1280, 1280, -720, 720) 
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