import numpy as np
import pygame as pg
import math
import csv

pg.init()

win = pg.display.set_mode((1600, 900))
clock = pg.time.Clock()
pg.display.set_caption("simulation")

running = True

g = 9.81

dt = 0.001

m1 = 1
l1 = 1
x1 = 0
y1 = 0
t1 = (math.pi)/4
v1 = 0
a1 = 0

m2 = 1
l2 = 1
x2 = 0
y2 = 0
t2 = (-1 * math.pi) / 4
v2 = 0
a2 = 0

delta_theta = math.pi/180

time = 0

final_data = []

while running:
    
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
    
    thetaDiff = t1 - t2
    sinThetaDiff = math.sin(thetaDiff)
    cosThetaDiff = math.cos(thetaDiff)

    bottom = (m1 + m2) - m2 * cosThetaDiff**2

    a1 = (-sinThetaDiff * m2 * (v2**2 * l2 + (l1 * v1**2 * cosThetaDiff)) + g * (m2 * math.sin(t2) * cosThetaDiff - (math.sin(t1) * (m1 + m2)))) / (l1 * bottom)
    a2 = (sinThetaDiff * (v1**2 * l1 * (m1 + m2) + (l2 * v2**2 * m2 * cosThetaDiff)) - g * (m1 + m2) * (math.sin(t2) - (cosThetaDiff * math.sin(t1)))) / (l2 * bottom)

    v1 = v1 + (a1 * dt)
    v2 = v2 + (a2 * dt)

    t1 = t1 + (v1 * dt)
    t2 = t2 + (v2 * dt)

    x1 = l1 * math.sin(t1)
    x2 = x1 + (l2 * math.sin(t2))

    y1 = -l1 * math.cos(t1)
    y2 = y1 - (l2 * math.cos(t2))

    win.fill((0, 0, 0))

    pg.draw.line(win, (0, 0, 255), (800, 450), (800 + (x1*100) ,  450 - (y1*100)), 2)
    pg.draw.line(win, (0, 0, 255), (800 + (x1*100) ,  450 - (y1*100)), (800 + (x2*100) ,  450 - (y2*100)), 2)

    pg.draw.circle(win, (255, 255, 255), (800 + (x1*100), 450 - (y1*100)), 10)
    pg.draw.circle(win, (255, 255, 255), (800 + (x2*100), 450 - (y2*100)), 10)

    pg.display.update()

    dt = clock.tick(60) / 1000

'''def pendulumsim(theta1, theta2):

    thetaDiff = t1 - t2
    sinThetaDiff = math.sin(thetaDiff)
    cosThetaDiff = math.cos(thetaDiff)

    bottom = (m1 + m2) - m2 * cosThetaDiff**2

    a1 = (-sinThetaDiff * m2 * (v2**2 * l2 + (l1 * v1**2 * cosThetaDiff)) + g * (m2 * math.sin(t2) * cosThetaDiff - (math.sin(t1) * (m1 + m2)))) / (l1 * bottom)
    a2 = (sinThetaDiff * (v1**2 * l1 * (m1 + m2) + (l2 * v2**2 * m2 * cosThetaDiff)) - g * (m1 + m2) * (math.sin(t2) - (cosThetaDiff * math.sin(t1)))) / (l2 * bottom)

    v1 = v1 + (a1 * dt / math.sqrt(g))
    v2 = v2 + (a2 * dt / math.sqrt(g))

    t1 = t1 + (v1 * dt / math.sqrt(g))
    t2 = t2 + (v2 * dt / math.sqrt(g))

    x1 = l1 * math.sin(t1)
    x2 = x1 + (l2 * math.sin(t2))

    y1 = -l1 * math.cos(t1)
    y2 = y1 - (l2 * math.cos(t2))

    time += dt

for i in range(50000):

    thetaDiff = t1 - t2
    sinThetaDiff = math.sin(thetaDiff)
    cosThetaDiff = math.cos(thetaDiff)

    bottom = (m1 + m2) - m2 * cosThetaDiff**2

    a1 = (-sinThetaDiff * m2 * (v2**2 * l2 + (l1 * v1**2 * cosThetaDiff)) + g * (m2 * math.sin(t2) * cosThetaDiff - (math.sin(t1) * (m1 + m2)))) / (l1 * bottom)
    a2 = (sinThetaDiff * (v1**2 * l1 * (m1 + m2) + (l2 * v2**2 * m2 * cosThetaDiff)) - g * (m1 + m2) * (math.sin(t2) - (cosThetaDiff * math.sin(t1)))) / (l2 * bottom)

    v1 = v1 + (a1 * dt / math.sqrt(g))
    v2 = v2 + (a2 * dt / math.sqrt(g))

    t1 = t1 + (v1 * dt / math.sqrt(g))
    t2 = t2 + (v2 * dt / math.sqrt(g))

    x1 = l1 * math.sin(t1)
    x2 = x1 + (l2 * math.sin(t2))

    y1 = -l1 * math.cos(t1)
    y2 = y1 - (l2 * math.cos(t2))

    time += dt

    final_data.append([t1, t2, v1, v2, time])


with open('litValue.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(final_data)'''

#commented latter code is useful for analysis purposes whilst uncommented code displays simualtion