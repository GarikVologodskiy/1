def HanoiMove(numrings, b, c):
    if numrings > 0:
        help_pole = 6 - b - c  # вспомогательный столб
        HanoiMove(numrings-1, b, help_pole)
        print(f"move disk {numrings} to the pole {b}")
        HanoiMove(numrings-1, help_pole, c)
        print(f"move disk {numrings} to the pole, {c}")
        # HanoiMove(numrings - 1, c, b)
    return numrings, b, c

numrings = int(input())
b = 1
c = 3

HanoiMove(numrings, b, c)


#         help_pole = 6 - b - c  # вспомогательный столб
#         HanoiMove(numrings - 1, b, help_pole)
#         print(f"move disk {numrings} to the pole {b}")
#         HanoiMove(numrings - 1, help_pole, c)
#         print(f"move disk {numrings} to the pole {c}")
#
#
# def Hanoi(n, x, y):
#     if n > 0:
#         Hanoi(n-1, x, y)
#         print(n, x, 2)
#         Hanoi(n-1, y, x)
#         print(n, 2, y)
#         Hanoi(n - 1, y, x)
#         Hanoi(n - 1, x, y)
#     return n, x, y
#
# n = int(input())
# x = 1
# y = 3
# Hanoi(n, x, y)
#
#
# # numrings = int(input("Enter count of rings: "))
# # a = [i for i in range(numrings, 0, -1)]
# # b = []
# # c = []
# # etalon = a.copy()
# # sticks = ["A", "B", "C"]
# # row = 0
#
# def HanoiMove(numrings, b, c):
#     if numrings > 0:
#         help_pole = 7 - b - c  # вспомогательный столб
#         HanoiMove(numrings - 1, b, help_pole)
#         print(f"move disk {numrings} to the pole {b}")
#         HanoiMove(numrings - 1, help_pole, c)
#         print(f"move disk {numrings} to the pole {c}")
#
#
# HanoiMove(3, 1, 3)