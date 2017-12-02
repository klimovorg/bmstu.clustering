###Алгоритм кратчайшего незамкнутого пути (КНП)
###1: Найти пару точек (i, j) с наименьшим ρij и соединить их ребром;
###2: пока в выборке остаются изолированные точки
###3: найти изолированную точку, ближайшую к некоторой неизолированной;
###4: соединить эти две точки ребром;
###5: удалить K − 1 самых длинных рёбер;

import matplotlib.pyplot as plt
from math import sqrt


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
    return a,b

a,b = take_data()


#кол-во точек
N = len(a)

def distance(a1,a2, b1, b2):
    c = 0
    c = sqrt((b1-a1)*(b1-a1) + (b2-a2)*(b2-a2))
    return c


def flag1(id):
    for p in points:
        if (id == p['id']):
            p['flag'] = 1


def printit():
    for li in links:
        for p in points:
            if (p['id'] == li['t2']):
                x2 = p['x']
                y2 = p['y']
        for p in points:
            if (p['id'] == li['t1']):
                x1 = p['x']
                y1 = p['y']
        plt.plot([x1, x2], [y1, y2], color='g')
    plt.show()


def delmaxdistancelink():
    linkss = []
    maxD = 0
    for li in links:
        for p in points:
            if (p['id'] == li['t2']):
                x2 = p['x']
                y2 = p['y']
        for p in points:
            if (p['id'] == li['t1']):
                x1 = p['x']
                y1 = p['y']
        if (distance(x1,y1,x2,y2) > maxD):
            maxD = distance(x1,y1,x2,y2)
            maxLI = li
    for li in links:
        if (maxLI != li):
            linkss.append(li)
    return linkss

print('Рассчеn начался')

#массив с точками
points = []
#массив связей
links = []


#наполняем массив с точками
print('Наполняем массив с точками')
i = 0
while i < N:
    d = {'id': i, 'x': a[i], 'y': b[i], 'part': 0, 'flag': 0 }
    points.append(d)
    i = i+1

#соединяем пару точек с наименьшем растоянием
n = 1
while n < 2:
    smallest = 1000
    smallest1 = {'id':0, 'x': 0, 'y': 0}
    smallest2 = {'id':0, 'x': 1.1, 'y': 1.1}
    for p1 in points:
        for p2 in points:
            if (distance(p1['x'], p1['y'], p2['x'], p2['y']) < smallest and
                        p1['x'] != p2['x'] and
                        p1['y'] != p2['y'] and
                    (p1['flag'] == 0 or p2['flag'] == 0)):
                smallest = distance(p1['x'], p1['y'], p2['x'], p2['y'])
                smallest1 = {'id': p1['id'], 'x': p1['x'], 'y': p1['y']}
                smallest2 = {'id': p2['id'], 'x': p2['x'], 'y': p2['y']}

    links.append({'t1': smallest1['id'], 't2': smallest2['id']})
    flag1(smallest1['id'])
    flag1(smallest2['id'])
    n = n + 1


#соед остальные точки
print('Выполняется соединение')
n = 1
while n < N:
    smallest = 1000
    smallest1 = {'id':0, 'x': 0, 'y': 0}
    smallest2 = {'id':0, 'x': 1.1, 'y': 1.1}
    for p1 in points:
        for p2 in points:
            if (distance(p1['x'], p1['y'], p2['x'], p2['y']) < smallest and
                        p1['x'] != p2['x'] and
                        p1['y'] != p2['y'] and
                        p1['flag'] == 0 and
                        p2['flag'] == 1):
                smallest = distance(p1['x'], p1['y'], p2['x'], p2['y'])
                smallest1 = {'id': p1['id'], 'x': p1['x'], 'y': p1['y']}
                smallest2 = {'id': p2['id'], 'x': p2['x'], 'y': p2['y']}

    links.append({'t1': smallest1['id'], 't2': smallest2['id']})
    flag1(smallest1['id'])
    flag1(smallest2['id'])
    n = n + 1

for p in points:
    plt.scatter(p['x'], p['y'], color='g')

#удаляем самую длинную связь
links = delmaxdistancelink()

print('Рассчет окончен')


print('Вывод графика')
printit()