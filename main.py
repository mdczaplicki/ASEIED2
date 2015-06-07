import functools

__author__ = 'Marek'
import numpy as np
from matplotlib.pyplot import plot, scatter, show, Circle, gcf, text, arrow
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
    init_d1 = np.copy(d1)
    init_d2 = np.copy(d2)

    a_priori_d1 = len(d1)/(len(d1 + d2))
    a_priori_d2 = len(d2)/(len(d1 + d2))

    n = int(input("How many new points?\n"))
    xd = [v * max(i[0] for i in d1 + d2) + v + min(i[0] for i in d1 + d2) - 1 for v in np.random.random(n)]
    xy = [v * max(i[1] for i in d1 + d2) + v + min(i[1] for i in d1 + d2) - 1 for v in np.random.random(n)]
    points = list(zip(xd, xy))

    b_points1 = []
    b_points2 = []

    new_d1 = []
    new_d2 = []

    for p, index in zip(points, range(len(points))):
        b_points1.append([])
        b_points2.append([])
        r = 0.1
        while len(b_points1[index] + b_points2[index]) < 3:
            for i in d1:
                if np.sqrt((i[0] - p[0])**2 + (i[1] - p[1])**2) < r and i not in b_points1[index]:
                    b_points1[index].append(i)
                    arrow(i[0], i[1], (p[0] - i[0]) * 0.5, (p[1] - i[1]) * 0.5)
                    plot(*zip(*[p, i]), ls='--')

            for i in d2:
                if np.sqrt((i[0] - p[0])**2 + (i[1] - p[1])**2) < r and i not in b_points2[index]:
                    b_points2[index].append(i)
                    arrow(i[0], i[1], (p[0] - i[0]) * 0.5, (p[1] - i[1]) * 0.5)
                    plot(*zip(*[p, i]), ls='--')
            r += 0.01
        fig = gcf()
        fig.gca().add_artist(Circle(p, r, linestyle='dotted', fill=False, capstyle='round', clip_on=False))

        if len(b_points1[index])/len(d1) * a_priori_d1 > len(b_points2[index])/len(d2) * a_priori_d2:
            new_d1.append(p)
            d1.append(p)  # should Bayes consider new added points?
        elif len(b_points1[index])/len(d1) * a_priori_d1 < len(b_points2[index])/len(d2) * a_priori_d2:
            new_d2.append(p)
            d2.append(p)  # should Bayes consider new added points?
        text(p[0] + 0.05, p[1] + 0.1, s=str(index))

    scatter(*zip(*points), c='black', s=200)
    try:
        scatter(*zip(*new_d1), c='pink', s=150)
    except TypeError:
        pass
    try:
        scatter(*zip(*new_d2), c='yellow', s=150)
    except TypeError:
        pass
    scatter(*zip(*init_d1), c='pink', s=200)
    scatter(*zip(*init_d2), c='yellow', s=200)
    show()


def main():
    while True:
        init = list(np.random.random_integers(0, 1000, 1000))
        try:
            print("======================================")
            print(init)
            n = int(input("======================================\n"
                          "Choose sorting method:\n"
                          "0. Exit\n"
                          "1. Bubble-sort\n"
                          "2. Selection-sort\n"
                          "3. Quick-sort\n"
                          "4. Naive Bayes Classifier\n"))
        except ValueError:
            continue
        if n == 1:
            start = time.time()
            print(bubble(list(np.copy(init))))
            end = time.time()
            print("Time of sorting:")
            print(end - start)
        elif n == 2:
            start = time.time()
            print(selection(list(np.copy(init))))
            end = time.time()
            print("Time of sorting:")
            print(end - start)
        elif n == 3:
            start = time.time()
            print(quick(init))
            end = time.time()
            print("Time of sorting:")
            print(end - start)
        elif n == 4:
            bayes()
        elif n == 0:
            break

if __name__ == "__main__":
    import sys
    sys.exit(main())
