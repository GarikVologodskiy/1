# 1.Если переменная a больше нуля и меньше 5-ти, то выведите 'Верно', иначе выведите 'Неверно'. Проверьте работу скрипта при a, равном 5, 0, -3, 2.
# a = int(input())
# if  5 > a > 0:
#     print('Correct')
# else:
#     print('Incorrect')

# Если переменная a больше 2-х и меньше 11-ти, или переменная b больше или равна 6-ти и меньше 14-ти, то выведите 'Верно',
# в противном случае выведите 'Неверно'.
# a = int(input())
# b = int(input())
# if 11 < a > 2 or 14 > b >= 6:
#     print('Correct')
# else:
#     print('Incorrect')

# Если переменная a равна или меньше 1, а переменная b больше или равна 3, то выведите сумму этих переменных,
# иначе выведите их разность (результат вычитания). Проверьте работу скрипта при a и b, равном 1 и 3, 0 и 6, 3 и 5.\
# a = int(input("a: "))
# b = int(input("b: "))
# if a <= 1 or b >= 3:
#     r1 = a+b
#     print(r1)
# else:
#     r2 = a-b
#     print(r2)

# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
# y = int(input("Input year: "))
# if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
#     print('YES')
# else:
#     print('NO')

# Даны три целых числа. Выведите значение наименьшего из них.
# a, b, c = int(input()), int(input()), int(input())
# if a < b:
#     print(a)
# elif b < c:
#     print(b)
# else:
#     print(c)

Даны
три
целых
числа.Определите, сколько
среди
них
совпадающих.Программа
должна
вывести
одно
из
чисел: 3(если
все
совпадают),
2(если
два
совпадает) или
0(если
все
числа
различны).
a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))
if a == b and b == c:
    print(3)
elif a == c or a == b or b == c:
    print(2)
else:
    print(1)

'''

if not (0 <= x1 < 8 and 0 <= y1 < 8):
    # if abs((x0 - x1) != (y1 - y0)):
    if abs((x0 != x1) and (y0 != y1)):
        print(x1, y1)
    else:
        print("Wrong move")

if not (0 <= x1 < 8 and 0 <= y1 < 8):
    # if abs((x0 - x1) != (y1 - y0)):
    if abs((x0 != x1) and (y0 != y1)):
        print(x1, y1)
    else:
        print("Wrong move")

if not (0 <= x1 < 8 and 0 <= y1 < 8):
    # if abs((x0 - x1) != (y1 - y0)):
    if abs((x0 != x1) and (y0 != y1)):
        print(x1, y1)
    else:
        print("Wrong move")

'''
'''
if ((x1 + y1 + x2 + y2) % 2 == 0) or x1 > 5:
    print('YEP')
else:
    print('NO')

if a > b:
    print(a)
    if a > 5:
        print("Root is:", (a**2)**0.5)
elif a == 0:
    print(0)
elif a > 44:
    print(44)
else:
    print(b)

d = {'a':1, 'b':3.4, 'c':5, 'd':6, 'e':8}
i = 1
for lines in  d:
    print(str(i), lines)
    i+=1
v = []
d = {'a':1, 'b':3.4, 'c':5, 'd':6, 'e':8}
for i, v in enumerate(d):
    print(i+1, v)

v = []
d = {'a':1, 'b':3.4, 'c':5, 'd':6, 'e':8}
nm = ()
for i in d.values():
    if i % 2 == 0:
        print(f" Value is: {i}")

print (type(a))
print (type(b))
print (type(c))
print (type(v))
print (type(d))
print (type(nm))
'''

# print (a)
# print (b)
# print (c)

### Chess ###
# Ладья#
# x0, y0 = int(input("x0: ")), int(input("y0: "))
# x1, y1 = int(input("x1: ")), int(input("y1: "))
#
# if 0 <= x1 <= 8 and 0 <= y1 <= 8:
#     if x0 == x1 or y0 == y1:
#         print(x1, y1)
#     else:
#         print("Wrong move")

# Слон#
# x0, y0 = int(input("x0: ")), int(input("y0: "))
# x1, y1 = int(input("x1: ")), int(input("y1: "))
#
# if 0 <= x1 <= 8 and 0 <= y1 <= 8:
#     if abs(x0 - x1) == abs(y0 - y1):
#         print(x1, y1)
#     else:
#         print("Wrong move")

# Король#
# x0, y0 = int(input("x0: ")), int(input("y0: "))
# x1, y1 = int(input("x1: ")), int(input("y1: "))
#
# if 0 <= x1 <= 8 and 0 <= y1 <= 8:
#     dx = abs(x0-x1)
#     dy = abs(y0-y1)
#     if -1 <= dx <= 1 or -1 <= dy <= 1:
#         print(x1, y1)
#     else:
#         print("Wrong move")

# #Ферзь#
# x0, y0 = int(input("x0: ")), int(input("y0: "))
# x1, y1 = int(input("x1: ")), int(input("y1: "))
#
# if 0 <= x1 < 8 and 0 <= y1 < 8:
#     if (x0 == x1 or y0 == y1) or (abs(x0 - x1) == abs(y0 - y1)):
#         print(x1, y1)
#     else:
#         print("Wrong move")

# Конь#
x0, y0 = int(input("x0: ")), int(input("y0: "))
x1, y1 = int(input("x1: ")), int(input("y1: "))

if 0 <= x1 <= 8 and 0 <= y1 <= 8:
    if (x0 - 1 == x1 or x0 + 1 == x1) and (y0 - 2 == y1 or y0 + 2 == y1):
        print('YES')
    elif (x0 - 2 == x1 or x0 + 1 == x1) and (y0 - 1 == y1 or y0 + 1 == y1):
        print('YES')
    else:
        print("Wrong move")

# Пешка#
x0, y0 = int(input("x0: ")), int(input("y0: "))
x1, y1 = int(input("x1: ")), int(input("y1: "))

if 0 <= x1 <= 8 and 0 <= y1 <= 8:
    # dx = abs(x0-x1)
    if x0 == x1:
        print(x1, y1)
    else:
        print("Wrong move")
# Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек.
# Программа получает на вход три числа: n, m, k и должна вывести YES или NO.

n, m, k = int(input("n: ")), int(input("m: ")), int(input("k: "))
if ((k % n == 0) or (k % m == 0)) and (k < n * m):
    print('YES')
else:
    print('NO')

# Яша плавал в бассейне размером N × M метров и устал.
# В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков (не обязательно от ближайшего)
# и y метров от одного из коротких бортиков. Какое минимальное расстояние должен проплыть
# Яша, чтобы выбраться из бассейна на бортик? Программа получает на вход числа N, M, x, y. Программа должна вывести число метров,
# которое нужно проплыть Яше до бортика.

n, m, x, y = int(input("n: ")), int(input("m: ")), int(input("x: ")), int(input("y: "))
n, m = min(n, m), max(n, m)
if x > n / 2:
    x = n - x
elif y > m:
    y = m - y
if x < y / 2:
    print(f" {x} m.")
else:
    print(f" {y} m.")


# Дан ряд  10. С помощью цикла for и оператора if проверьте есть ли в ряду элемент со значением, равным 4.
# Если есть - посчитайте сумму элементов массива. Если нет - ничего делать не надо.
# def rangefind():
#     m = [1,2,3,4,5,6,7,8,9,10,11]
#     print(sum(m))
#     s = 0
#     for i in m:
#         if i == 4:
#             for j in m:
#                 s += j
#             print(s)
# rangefind()

# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди введенных чисел и выведите это количество.
# Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

# n = [1000, 2, 3, 40, 5, 0, 0, 7, 8, 9, 0]
# c = 0
# for i in n:
#     if i == 0:
#         c += 1
# print(c)

# Кролики размножаются!!!#
# def fib_rabbit():
#     n = int(input("n: "))
#     j = 1
#     list = []
#     if n == 0:
#         return 0
#     else:
#         f1, f2 = 0, 1
#         for i in range(2, n + 1):
#             # (f1-1) + (f2-2)
#             f1, f2 = f2, f1+f2
#             # n -= 1
#             list.append(f2)
#             print(f" Месяц: {j}, Количество кроликов: {f2}")
#             j += 1
#         print(f" Общее количество кроликов: {sum(list)}")
#
# fib_rabbit()

# n = int(input())
# if n == 0:
#     print(0)
# else:
#     a, b = 0, 1
#     for i in range(2, n + 1):

# i = 0
# while i < n < 2
# f_sum = f1+f2
# f1 = f2
# f2 = f_sum
# i=i+1
#
# while n>0
# f1, f2 = f2, f1 + f2
# n-=1

# x = int(input("x: "))
# y = int(input("y: "))
# day = 1
# while x < y:
#     x *= 1.1
#     day += 1
# print(f"Дней: {day}")

# def Fib(n):
#     if n <= 1:
#         return n
#     else:
#         return Fib(n-1) + Fib(n-2)
# print(Fib(9))

def FibGen(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


data = list(FibGen(9))
print(data)

# b = "sfdsdfsd dfsdf sdfsdfds"
# # # e = b.split()
# # # print(e)
# #
# lst = [1, 2, 5, 9, 4, 13, 4, 10]
# # for i in lst:
# #     if i % 2 ==1:
# #         print(i, end = ' ')
#
# # b = "sfdsdfsd, dfsdf sdfsdfds"
# # for i in b.split():
# #     print(i)
#
# newlst = [c for c in lst if c % 2 == 1]
# print(newlst)

# a = []
# for i in range(1, 15):
#     a.append(i)
#     break
#     print(i, end=' ')
# print()
# print(a)

# c = [1, 2, 3, 4, 5, "F"]
# cn = [c for c in input().split()]
# print(cn)

# r = [7, 7, 8, 9]
# for i in range(len(r)):
#     print(r[i], end = ' ')

# a = []
# r = [7, 7, 8, 9]
# a = ['red', 'blue', 'green']
# b = (', '.join(a))
# r.append(a)
# print(r)
# print(b)

# list = [2, 3, 4, 5]
# s = 0
# for i in list:
#     s+=i
# print(s)

# lst = [5, 10, 4, 17, 19]
# s = 0
# for i in lst:
#     if i == 4:
#         for j in lst:
#             s += j
# print(s)

# def rangefind():
#     m = [1,2,3,4,5,6,7,8,9,10,11]
#     print(sum(m))
#     s = 0
#     for i in m:
#         if i == 4:
#             for j in m:
#                 s += j
#             print(s)
# rangefind()

# m = (1,2,3,4,5,6,7,8,9,10,11)
# print(sum(m))

# list_1 = [2, 3, 4, 5]
# list_2 = [2, 3, 4, 5]
#
# sum1, sum2 = sum(list_1), sum(list_2)
# if sum1 == sum2:
#     print('yes')
# else:
#     print('no')

# lst = [1, 2, 5, 4, 9, 7, 6, 4, 3, 8]
# for i in range(1, len(lst)):
#     if lst[i] > lst[i-1]:
#         print(lst[i], end = ' ')

# lst = [1, 4, 1, 2, 5, 10, 10]
# c = 0
# for i in range(len(lst)):
#     if lst[i] != lst[i-1]:
#        c+=1
# print(c)

# lst = [1, 4, 1, 2, 5, 10, 15, 15, 2, 5, 99, 101, 400]
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         if i != j and lst[i] == lst[j]:
#             break
#     else:
#         print(lst[i], end = ' ')


# f_list = [f1, f2, f3, f4, f5, f6, f7, f8]

n = 8
x = []
y = []

for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

f = 1
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            f = 0
        else:
            f = 1
if f:
    print('NO')
else:
    print('YES')

# # d = {'dict': 1, 'dictionary': 2}
# # q = dict.fromkeys(['a', 'b', 'c'], 4)
# # print(q)
#
# p = {}
# s = "hi i am here 6 7 8 9"
# s = s.split()
#
# p['one'] = s[0]
# p['two'] = s[1]
# p['t'] = s[2]
# p['f'] = s[3]
# p['mmm'] = s[4:]
#
# for i in s[4:]:
#     p['mmm'].append(int(i))
# print(p)
#
# # print(s)
# # print(p)
# #
# # del p['two']
# # print(p)
# # print(p.get('two', 'not found'))
#
# for k, v in p.items():
#     print(k, v)
#
# for k in p.popitem():
#     print(k, v)
#
# # {key:value for item in list if conditional}
# s = [1, 2, 3, 4, 5, 6, 8, 7, 10, 4]
# d = {a: b**2 for a in range(7) for b in range(10) if b not in s}
# print(d)


# Дан массив $arr. С помощью цикла foreach запишите английские названия в массив $en, а русские - в массив $ru.
# {'green':'зеленый', 'red':'красный', 'blue':'голубой'}

# arr = {'green':'зеленый', 'red':'красный', 'blue':'голубой'}
# ru = []
# en = []
# for k, v in arr.items():
#     en.append(k)
#     ru.append(v)
# print(f" ru: {ru}, en: {en}")

# Знаешь ли ты, сколько месяцев в году?
# — 12.
# А как их зовут?
# — Январь, февраль, март, апрель, май, июнь, июль, август, сентябрь, октябрь, ноябрь, декабрь.
# помогите девочке найти весенние месяцы

# months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
# spring_monthsd = {a: a for a in range(13) for a in months[2:5]}
# spring_monthsm = []
# for k, v in spring_monthsd.items():
#     spring_monthsm.append(v)
# print(spring_monthsd)
# print(spring_monthsm)

# Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.

# n = int(input())
# words = {}
# for i in range(n):
#     f, s = input().split()
#     words[f] = s
#     words[s] = f
#
# print(words[input()])

# n = int(input())
# p = dict(input().split() for i in range(n))
# c = input()
# for key, value in p.items():
#     if c == key:
#         print(key)
#     elif c == value:
#         print(value)

arr = {'Коля': '200', 'Вася': '300', 'Петя': '400'}
for k, v in arr.items():
    print(f" {k} - зарплата {v} долларов.")


# def E(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# for i in range (1, 11):
#     print(i, E(i))

# def Loc():
#     # local
#     a, b, c = 1, 2, 3
#     # w = 11
#     print(a, b, c, w)
#
# # global
# w = 8
# Loc()

# lambda arg1,arg2..: выражение
# rt = lambda x: x ** 2
# print(rt(7))

# Составьте словарь  дней недели. С помощью цикла for  выведите все дни недели, а выходные дни удалите.
# def Dict_day():
#     days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday',  5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
#     for k, v in days.items():
#         if k != 6 and k != 7:
#             print(v, end='; ')
#
# Dict_day()

# def Func(a, b, c):
#     a, b, *c = [6, 7, 'ddd', 8, 9, 10]
#     print(a, b, c)
# Func()

# def A(*args):
#     s = 0
#     for i in args:
#         s+=i
#     return s
# print(A(1, 2, 4, 5))

# def A(**kwargs):
#     print(kwargs)
# A(a=1, b=2, c=7)

# def A(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
#
#
# A(a=1, b=2, c=7)

# def A(*args, **kwargs):
#     print(args, kwargs)
#
#
# A(1, 2, 3, 4, a=1, b=2, c=7)

# С помощью цикла for заполните массив числами от 1 до 100. То есть у вас должен получится массив [1, 2, 3... 100].
def R(*args):
    a = []
    for i in range(1, 101):
        a.append(i)
    print(a)


R()

# def a(x):
#     if x < 4:
#         print("up:", x)
#         a(x + 1)
#         print("down:", x)
# a(1)
# r1->r2->r3->r4(не выполнено)->r3->r2->r1

# def f(x):
#     if x == 1:
#         return 1
#     print(x)
#     return f(x-1)*x
#     print(x)
#
# print(f(4))

# a = [1, [3, [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]
#
#
# def Rn(one, lev=1):
#     print(*one, 'lev=', lev)
#     for i in one:
#         if type(i) == list:
#             Rn(i, lev + 1)
#
#
# Rn(a)

# a = []
# n = 5
# m = 6
# for i in range(n):
#     a.append([])
#     for j in range(m):
#         if (i + j) % 2 == 0:
#             a[i].append('.')
#         else:
#             a[i].append('*')
# for row in a:
#     print(' '.join(row))

# def IsPal(x):
#     if len(x) <= 1:
#         return True
#     else:
#         x[0] == x[-1] and IsPal(x[1:-1])
#
# print(IsPal('вав'))

# def p(x):
#     if len(x) <= 1:
#         return True
#     if x[0] != x[-1]:
#         return False
#     return p(x[1:-1])
#
# print(p('ваав'))

# Дан массив с числами. Выведите последовательно его элементы используя рекурсию и не используя цикл
# arr = [1, 2, 3, 5, 6, 0, 11, 46, 34, 78]
#
# def Arr(x):
#     while x < len(arr):
#         print(arr[x])
#         x += 1
#     Arr(x)
#
# Arr(0)

# Дано число. Сложите его цифры. Если сумма получилась более 9-ти, опять сложите его цифры. И так, пока сумма не станет однозначным числом (9 и менее).
a = 233


def SumDigit(n):
    x = sum(int(d) for d in str(n))
    if x < 9:
        return x
    else:
        SumDigit(x)


res = SumDigit(a)
print(res)

# фибоначчи рекурсия
# def Fib(n):
#     if n <= 1:
#         return n
#     else:
#         return Fib(n-1) + Fib(n-2)
#
#
# print(Fib(9))

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
        help_pole = 7 - b - c  # вспомогательный столб
        HanoiMove(numrings - 1, b, help_pole)
        print(f"move disk {numrings} to the pole {b}")
        HanoiMove(numrings - 1, help_pole, c)
        print(f"move disk {numrings} to the pole {c}")


HanoiMove(3, 1, 3)