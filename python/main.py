from sklearn.metrics.pairwise import pairwise_distances
import sklearn.metrics as skm
#from sklearn.metrics import silhouette_score
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
        cur_score = skm.silhouette_score(matrix, cur_labels, metric="euclidean")
        i = i + 1
        print(i, "_______")
    print(cur_score)


data = genfromtxt('..\\data\\pfister\\vectors_5.txt', delimiter=";")
"""bei vectors_5 nicht die ersten 5 Graphen sondern manuelle Auswahl
    Cluster (0,2), (1,4) und (3) """

"""Distanzmatrix"""
D = pairwise_distances(data, metric='euclidean')
# print(D)
DD = genfromtxt('..\\data\\symmetrized\\avg_symmetrized_matrix_lenz.csv', delimiter=";")
# print(DD)
"""K Cluster"""
k = 3
M, C = kMedoid.kMedoids(DD, k)

labels = []

print('medoids:', M)


print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
        labels.append(label)
        print("Graph:", point_idx, "Cluster:", label)

score = skm.silhouette_score(DD, labels, metric="euclidean")
print('silhouette-score:', score)

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

# best_silhouette(0.06498913421018607, score, DD, k)

# eval:
# avg   0.1001063545848603 (k = 2)      0.06498913421018607 (k = 3)
# min   0.09179591158425277 (k = 2)     0.05667220812087653 (k = 3)
# max   0.0920887877300312  (k = 2)     0.04712664926968676 (k = 3)

# https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-clustering-1.html
# https://stats.stackexchange.com/questions/15158/precision-and-recall-for-clustering
