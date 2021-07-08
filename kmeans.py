# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                         #
# Nazev: Implementace k-means algoritmu                   #
# Autor: Pavel Bednar (xbedna73)                          #
# Skola: FIT VUT v Brne                                   #
# Pouziti: Program vypocitava jednotlive stredy a obsah   #
#          shluku metodou k-means s euklidovskou          #
#          metrikou. Pro zmenu parametru algoritmu        #
#          mente promenne points a means                  #
# Jazyk: Python 3.8                                       #
# Datum vytvoreni: 2020-04-13                             #
#                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import numpy as np

max_itr = 10 # maximalni pocet iteraci (aby program nepracoval vecne)

points = [[0,1,4],
          [-1,1,3],
          [-1,-1,3],
          [1,0,4],
          [4,0,0],
          [5,1,1],
          [5,-1,-1],
          [6,0,0],
          [1,4,0],
          [2,3,1],
          [0,4,2],
          [-1,5,1]]

means = [[-3,-1,-3],
         [-1,-1,1],
         [-1,1,-4]]

print('K-MEANS ALGORITMUS')
print()
print('vychozi stredy shluku: ', end='')
print(means)
print('vychozi body: ', end='')
print(points)

# iteruji algoritmem
for itr in range(max_itr):
    im = 0
    dist = []  # 3 pole s vzdalenostmi bodu od jednotlivych stredu

    #spocitam vzdalenost
    for m in means:
        distn = []
        ip = 0
        for pt in points:
            p1 = np.array(points[ip])
            p2 = np.array(means[im])

            p1p2dist = np.sqrt(np.sum((p1 - p2)**2, axis=0))
            p1p2dist = round(p1p2dist, 2)
            distn.append(p1p2dist)

            ip += 1
        dist.append(distn)
        im += 1

    # spocitam minima
    minims = {} # pole s cisly do jakeho clusteru se konkretni prvek priradil
    for i in range(len(points)):
        pm = {}
        for j in range(len(means)):
            pm[j] = dist[j][i]
            j += 1
        minim = min(pm.values())
        minim = list(pm.keys())[list(pm.values()).index(minim)]
        minims[i] = minim

    mean0 = []
    mean1 = []
    mean2 = []

    for i in range(len(points)):
        if minims[i] == 0:
            mean0.append(i)
        if minims[i] == 1:
            mean1.append(i)
        if minims[i] == 2:
            mean2.append(i)

    newmean0 = []
    newmean1 = []
    newmean2 = []

    for i in range(len(mean0)):
        newmean0.append(points[mean0.pop()])
    for i in range(len(mean1)):
        newmean1.append(points[mean1.pop()])
    for i in range(len(mean2)):
        newmean2.append(points[mean2.pop()])

    show_mean0 = newmean0
    show_mean1 = newmean1
    show_mean2 = newmean2

    newmean0 = np.round(np.mean(newmean0, axis=0), decimals=2)
    newmean0 = newmean0.tolist()
    newmean1 = np.round(np.mean(newmean1, axis=0), decimals=2)
    newmean1 = newmean1.tolist()
    newmean2 = np.round(np.mean(newmean2, axis=0), decimals=2)
    newmean2 = newmean2.tolist()

    # ukoncujici podminka
    if newmean0 in means and newmean1 in means and newmean2 in means:
        print()
        print('nastala konvergence!')
        exit(0)

    tmean0 = newmean0
    tmean1 = newmean1
    tmean2 = newmean2
    means.pop()
    means.pop()
    means.pop()
    means.append(newmean0)
    means.append(newmean1)
    means.append(newmean2)

    print()
    print(str(itr + 1) + '. pruchod: ')
    print('  shluky:')
    print('    S1: ', end='')
    print(show_mean0)
    print('    S2: ', end='')
    print(show_mean1)
    print('    S3: ', end='')
    print(show_mean2)
    print('  ', end='')
    print('stredy shluku:')
    print('    S1: ', end='')
    print(tmean0)
    print('    S2: ', end='')
    print(tmean1)
    print('    S3: ', end='')
    print(tmean2)

    if itr + 1 == max_itr:
        print('bylo dosazeno maximalniho poctu iteraci! (' + str(max_itr) + ')')

exit(0)
