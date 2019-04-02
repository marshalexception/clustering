from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import silhouette_score
from numpy import genfromtxt
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

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


data = genfromtxt('..\\data\\pfister\\vectors_25.txt', delimiter=";")
"""bei vectors_5 nicht die ersten 5 Graphen sondern manuelle Auswahl
    Cluster (0,2), (1,4) und (3) """

"""Distanzmatrix"""
D = pairwise_distances(data, metric='euclidean')
print(D)
DD = genfromtxt('..\\data\\pfister\\matrix_25.txt', delimiter=";")
print(DD)
tmp = 1 - DD
print(tmp)
"""K Cluster"""
k = 14
M, C = kMedoid.kMedoids(tmp, k)

labels = []

print('medoids:', M)


print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
        labels.append(label)
        print("Graph:", point_idx, "Cluster:", label)

score = silhouette_score(tmp, labels, metric="euclidean")
print(score)
for label in C:
    for point_idx in C[label]:
        if label == 0:
            plt.scatter(point_idx, label, s=50, c='red')
        elif label == 1:
            plt.scatter(point_idx, label, s=50, c='blue')
        elif label == 2:
            plt.scatter(point_idx, label, s=50, c='green')
        else:
            plt.scatter(point_idx, label, s=50)
# plt.xlabel("Graph")
# plt.ylabel("Cluster")
# plt.show()

# dendrogram(D)

best_silhouette(-0.104, score, tmp, k)

# 5:
# 25 (15): -0.0767      -0.0067
# 88 (18): -0.109
# 110 (18): -0.109

# https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-clustering-1.html
# https://stats.stackexchange.com/questions/15158/precision-and-recall-for-clustering
