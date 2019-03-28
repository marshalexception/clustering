from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import silhouette_score
from numpy import genfromtxt
import matplotlib.pyplot as plt

"""Pytest installieren: python -m pip install pytest"""

from algorithms import kMedoid

# data = np.array([[1,1,1],[2,2,2], [10,10,10]])


def best_silhouette(border, score, matrix, k):
    """Methode für besten Silhouettenkoeffizient (iterativ)"""
    i = 1
    cur_score = score
    while cur_score < border:
        cur_labels = []
        cur_m, cur_c = kMedoid.kMedoids(matrix, k)
        for m in cur_m:
            print(m)
        for cur_label in cur_c:
            for point in cur_c[cur_label]:
                cur_labels.append(cur_label)
                print("Graph:", point, "Cluster:", cur_label)
        cur_score = silhouette_score(matrix, cur_labels, metric="euclidean")
        i = i + 1
        print(i, "_______")
    print(cur_score)


data = genfromtxt('..\\data\\pfister\\vectors_full.txt', delimiter=";")
"""bei vectors_5 nicht die ersten 5 Graphen sondern manuelle Auswahl
    Cluster (0,2), (1,4) und (3) """

"""Distanzmatrix"""
D = pairwise_distances(data, metric='euclidean')
DD = genfromtxt('..\\data\\pfister\\matrix_5.txt', delimiter=";")

"""K Cluster"""
k = 18
M, C = kMedoid.kMedoids(D, k)

labels = []

print('medoids:')
for point_idx in M:
    print(point_idx)

print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
        labels.append(label)
        print("Graph:", point_idx, "Cluster:", label)

score = silhouette_score(D, labels, metric="euclidean")
print(score)
for label in C:
    for point_idx in C[label]:
        plt.scatter(point_idx, label, s=50)
# plt.show()

best_silhouette(-0.112, score, D, k)

# 5:
# 25 (14): -0.069
# 88 (18): -0.119
# 110 (18): -0.112
