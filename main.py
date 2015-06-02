import functools

__author__ = 'Marek'
import numpy as np
from matplotlib.pyplot import plot, scatter, show
import time


def bubble(list_in) -> list:
    n = len(list_in)
    while n > 1:
        for i in range(n - 1):
            if list_in[i] > list_in[i+1]:
                list_in[i], list_in[i+1] = list_in[i+1], list_in[i]
                n = len(list_in)
        n -= 1
    return list_in


def selection(list_in) -> list:
    for i in range(len(list_in) - 1):
        mini = i
        for j in range(i + 1, len(list_in)):
            if list_in[j] <= list_in[mini]:
                mini = j
        list_in[i], list_in[mini] = list_in[mini], list_in[i]
    return list_in

quick = lambda list_in: (quick([y for y in list_in[1:] if y < list_in[0]]) + list_in[:1] +
                         quick([y for y in list_in[1:] if y >= list_in[0]])) if len(list_in) > 1 else list_in


def bayes():
    d1 = [(float(i[0]), float(i[1])) for i in [d.replace('\n', '').replace(',', '.').split('|')
                                               for d in open('data1.csv').readlines()]]
    d2 = [(float(i[0]), float(i[1])) for i in [d.replace('\n', '').replace(',', '.').split('|')
                                               for d in open('data2.csv').readlines()]]
    n = int(input("How many new points?\n"))
    xd = [v * max(i[0] for i in d1 + d2) + min(i[0] for i in d1 + d2) for v in np.random.random(n)]
    xy = [v * max(i[1] for i in d1 + d2) + min(i[1] for i in d1 + d2) for v in np.random.random(n)]
    points = zip(xd, xy)

    b_points1 = []
    b_points2 = []

    r = 1
    for p, index in zip(points, range(len(points))):
        b_points1.append([])
        b_points2.append([])
        for i in d1:
            if np.sqrt(i[0]**2 + p[0]**2) < r:
                b_points1[index].append(i)
        for i in d2:
            if np.sqrt(i[0]**2 + p[0]**2) < r:
                b_points1[index].append(i)




    scatter(*zip(*points), c='green', s=50)
    scatter(*zip(*d1), c='red')
    scatter(*zip(*d2), c='blue')
    show()

def main():
    bayes()
    # while True:
    #     init = list(np.random.random_integers(0, 1000, 1000))
    #     try:
    #         print("======================================")
    #         print(init)
    #         n = int(input("======================================\n"
    #                       "Choose sorting method:\n"
    #                       "0. Exit\n"
    #                       "1. Bubble-sort\n"
    #                       "2. Selection-sort\n"
    #                       "3. Quick-sort\n"))
    #     except ValueError:
    #         continue
    #     if n == 1:
    #         start = time.time()
    #         print(bubble(list(np.copy(init))))
    #         end = time.time()
    #         print("Time of sorting:")
    #         print(end - start)
    #     elif n == 2:
    #         start = time.time()
    #         print(selection(list(np.copy(init))))
    #         end = time.time()
    #         print("Time of sorting:")
    #         print(end - start)
    #     elif n == 3:
    #         start = time.time()
    #         print(quick(init))
    #         end = time.time()
    #         print("Time of sorting:")
    #         print(end - start)
    #     elif n == 0:
    #         break

if __name__ == "__main__":
    import sys
    sys.exit(main())
