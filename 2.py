import matplotlib.pyplot as plt
from math import sqrt
import random


def distance(a1,a2, b1, b2):
    c = 0
    c = sqrt((b1-a1)*(b1-a1) + (b2-a2)*(b2-a2))
    return c


def take_data():
    f = open('data.txt', 'r')
    a = []
    b = []

    for line in f:
        a.append(line[2] + line[3] + line[4] + line[5] + line[6] + line[7])
        b.append(line[12] + line[13] + line[14] + line[15] + line[16] + line[17])

    for i in range(len(a)):
        a[i] = float(a[i])
        b[i] = float(b[i])
    return a, b


a, b = take_data()

# массив с точками
points = []

i = 0
while i < len(a):
    d = {'x': a[i], 'y': b[i], 'part': 0}
    points.append(d)
    i = i + 1


centerX1 = random.random()*2 + 8
centerY1 = random.random()*8
centerX2 = random.random()*2 + 8
centerY2 = random.random()*8


#рисуем исходные данные
for i in points:
    plt.scatter(i['x'], i['y'], color='b')

plt.scatter(centerX1, centerY1, color='r')
plt.scatter(centerX2, centerY2, color='g')

plt.show()


for j in range(5):
    plt.clf()

    for i in points:
        if distance(i['x'], i['y'], centerX1, centerY1) > distance(i['x'], i['y'], centerX2, centerY2):
            i['part'] = 2
        else:
            i['part'] = 1

    for i in points:
        if i['part'] == 1:
            plt.scatter(i['x'], i['y'], color='r')
        else:
            plt.scatter(i['x'], i['y'], color='g')

    plt.show()

    #Пересчет центра масс
    centerX1 = 0
    centerY1 = 0
    centerX2 = 0
    centerY2 = 0
    centerType1 = 0
    centerType2 = 0

    for i in points:
        if i['part'] == 1:
            centerType1 += 1
            centerX1 += i['x']
            centerY1 += i['y']
        else:
            centerType2 += 1
            centerX2 += i['x']
            centerY2 += i['y']

    centerX1 = centerX1 / centerType1
    centerY1 = centerY1 / centerType1
    centerX2 = centerX2 / centerType2
    centerY2 = centerY2 / centerType2

