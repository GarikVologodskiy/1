jabas = int(input("How much frogs of each color sitting on the tussocks?: "))
# kochki = ['G' for _ in range(jabas)]
# kochki.append('')
# for i in range(jabas):
# kochki.append('R')
# etalon = kochki.copy()
# etalon.reverse()
# movenum = 0
# def indexlast(lst, *arg):
# start = 0
# stop = len(lst)
# found = -1
# if len(arg) > 0:
# str = arg[0]
# if len(arg) >= 2:
# start = arg[1]
# if len(arg) >= 3:
# stop = arg[2]
# for i in range(start, stop):
# if lst[i] == str:
# found = i
# return found
# def move(color, jumps, step):
# global movenum
# if kochki == etalon:
# return
# if jumps == jabas:
# step = 0
# if color == 'G':
# for i in range(1,jumps+1):
# free = kochki.index('')
# sour = indexlast(kochki,'G',0,free + 1)
# dest = free
# kochki[dest] = kochki[sour]
# kochki[sour] = ''
# movenum += 1
# print("Move # ",movenum," :", kochki)
# if kochki[-1] == 'G' and kochki[0] == 'R':
# step = -1
# move('R', jumps + step,step)
# else:
# for i in range(1,jumps+1):
# free = kochki.index('')
# sour = kochki.index('R',free)
# dest = free
# kochki[dest] = kochki[sour]
# kochki[sour] = ''
# movenum += 1
# print("Move # ",movenum," :", kochki)
# if kochki[-1] == 'G' and kochki[0] == 'R':
# step = -1
# move('G', jumps + step,step)
#
# print("Start:",kochki)
# move('G',1,1)
# input()
# print("Finish",kochki)
[Пт 14 фев 19: 33:50] Aklexey_ > hanoy


# import sys
# sys.setrecursionlimit(4000)
# numrings = int(input("Enter count of rings: "))
# a = [i for i in range(numrings, 0, -1)]
# b = []
# c = []
# etalon = a.copy()
# sticks = ["A", "B", "C"]
# row = 0
#
# def move(p1, p2, p3):
# global sticks
# global row
# row += 1
# if c == etalon:
# return
# if len(p1) > 0:
# p3.append(p1.pop())
# print(sticks[0],"->",sticks[2])
# if len(p1) > 0:
# p2.append(p1.pop())
# print(sticks[0], "->", sticks[1])
# if len(p3) > 0:
# p2.append(p3.pop())
# print(sticks[2], "->", sticks[1])
# if len(p1) > 0 and (len(p3) == 0 or p3[-1] > p1[-1]):
# p3.append(p1.pop())
# print(sticks[0], "->", sticks[2])
# elif len(p3) > 0:
# p1.append(p3.pop())
# print(sticks[2], "->", sticks[0])
# print("Row:", row, a, b, c)
# sticks = [sticks[1], sticks[2], sticks[0]]
# move(p2, p3, p1)
#
# print("Start:", a, b, c)
# move(a, b, c)
# print("Finish:", a, b, c)

# jabas = int(input("How much frogs of each color sitting on the tussocks?: "))
# kochki = ['G' for _ in range(jabas)]
# kochki.append('')
# for i in range(jabas):
# #    kochki.append('R')
# etalon = kochki.copy()
# etalon.reverse()

# def frogs():


# numrings = int(input("Enter count of rings: "))
# a = [i for i in range(numrings, 0, -1)]
# b = []
# c = []
# etalon = a.copy()
# sticks = ["A", "B", "C"]
# row = 0

def HanoiMove(numrings, b, c):
    if numrings > 0:
        HanoiMove(numrings - 1, b, c)
        print(f"move disk {numrings} to the pole {b}")
        HanoiMove(numrings - 1, c, b)
        print(f"move disk {numrings} to the pole {c}")
        HanoiMove(numrings - 1, b, c)
        HanoiMove(numrings - 1, c, b)

        # help_pole = 7 - b - c #вспомогательный столб
        # HanoiMove(numrings-1, b, help_pole)
        # print(f"move disk {numrings} to the pole {b}")
        # HanoiMove(numrings-1, help_pole, c)
        # print(f"move disk {numrings} to the pole {c}")


numrings = int(input("Enter count of rings: "))
b, c = 1, 3
HanoiMove(numrings, b, c)

# with open('C:\\Users\\student\\Documents\\text.txt', 'w') as f:
#     f.write('Hello, man! It\'s me! Let\'s do it! You can do it, mate!')
# with open('C:\\Users\\student\\Documents\\text.txt', 'r') as f:
#     data = f.readlines()
#     print(*data)

# with open('C:\\Users\\student\\Documents\\test.txt', 'wt', encoding='utf-8') as inFile:
#     num = int(input())
#     line = str('1 / ' + str(num) + ' = ' + str(1 / num))
#     print(line)
#     inFile.write(line)

# a = 100
# b = 1
# try:
#     c = a / b
# except:
#     pass
#     c = 0
#     print('Incorrect dividing')

a = 100
b = 'a'
try:
    c = a / b
except (ZeroDivisionError):
    # pass
    print(ZeroDivisionError)
except (TypeError):
    print(TypeError)
else:
    print(c)

# with open('C:\\Users\\student\\Documents\\test.txt', 'r', encoding='utf-8') as inFile:
#     a = []
#     try:
#         for i in inFile:
#             a.append(int(i))
#     except ValueError:
#         print('Not a number')
#     except Exception:
#         print('Not define')
#     else:
#         print('Everything is good')
#     finally:
#         print('File is closed')

# import turtle
#
# window = turtle.Screen()
# window.setup(1800+3, 900+3)
# window.bgcolor("blue")
# window.screensize(1200, 800)
#
# pen = turtle.Turtle()
# pen.color('red')
#
# for i in [-400, -200, 0, 200, 400]:
#     #     pen.setpos(x=i, y=0)
#     pen.circle(radius = 100)
#     pen.forward(500)
#     pen.circle(radius = 100)
#     window.mainloop()

# проверка
# на
# папку
# isdir()
# import os
#
# path = 'C:\\Games'
# print(os.listdir(path))
# for i in os.listdir(path):
#     print(i, type(i), path + '\\' + i, os.path.isdir(path + '\\' + i))
#
# проверка
# на
# файл
# isfile()
# import os
#
# path = 'C:\\Users\\student\\Downloads'
# print(os.listdir(path))
# for i in os.listdir(path):
#     print(i, type(i), path + '\\' + i, os.path.isfile(path + '\\' + i))
#
# рекурсивный
# поиск
# import os
#
# path = 'C:\\Games'
#
#
# def f(path, level=1):
#     print('Level=', level, 'Content: ', os.listdir(path))
#     for line in os.listdir(path):
#         # если является папкой, спускаемся
#         if os.path.isdir(path + '\\' + line):
#             print('Спускаемся', path + '\\' + line)
#             f(path + '\\' + line, level + 1)
#             print('Возвращаемся в', path)
#
#
# f(path)
#
# рекурсивный
# поиск
# по
# имени

# import os
# path = 'C:\\Users\\student'
#
# def f(path, level=1):
#     try:
#         print('Level=', level, 'Content: ', os.listdir(path))
#         for line in os.listdir(path):
#             if os.path.isfile(path + '\\' + line):
#                 print('Спускаемся', path + '\\' + line)
#     except:
#         print('No access')
#     else:
#         f(path + '\\' + line, level + 1)
#         print('Возвращаемся в', path)
#     finally:
#         print('Scanning is over')
#
# f(path)

# with open('C:\\Users\\student\\Documents\\test.txt', 'r', encoding='utf-8') as inFile:
#     a = []
#     try:
#         for i in inFile:
#             a.append(int(i))
#     except ValueError:
#         print('Not a number')
#     except Exception:
#         print('Not define')
#     else:
#         print('Everything is good')
#     finally:
#         print('File is closed')


import os

path = 'C:\\Users\\student\\Documents\\1'
name = 'test.txt'


def f(name, path):
    for root, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

        # for line in os.listdir(path):
        #     if os.path.isfile(path + '\\' + line):
        #         if name in line:

        # print('Спускаемся', path + '\\' + line)
    # except:
    #     print('No access')
    # else:
    #     f(path + '\\' + line, level + 1)
    #     print('Возвращаемся в', path)
    # finally:
    #     print('Scanning is over')


f(name, path)

# import os
# path = 'C:\\Users\\student\\Documents\\1'
#
# def f(path, level=1, name = 'text.txt'):
#     print('Level=', level, 'Content: ', os.listdir(path))
#     for line in os.listdir(path):
#         if os.path.isfile(path + '\\' + line):
#             if name in line:
#                 # return os.path.join(line, name)
#                 return line
#             print('Спускаемся', path + '\\' + line)
#             f(path + '\\' + line, level + 1)
#             print('Возвращаемся в', path)
#
# f(path)