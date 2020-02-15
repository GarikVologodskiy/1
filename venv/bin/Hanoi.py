def HanoiMove(numrings, b, c):
    if numrings > 0:
        HanoiMove(numrings-1, b, c)
        print(f"move disk {numrings} to the pole {b}, {2}")
        HanoiMove(numrings-1, c, b)
        print(f"move disk {numrings} to the pole {2}, {c}")
        HanoiMove(numrings - 1, b, c)
        HanoiMove(numrings - 1, c, b)

numrings = int(input())
b = 1
c = 3

HanoiMove(numrings, b, c)