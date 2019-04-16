from sklearn.metrics.pairwise import pairwise_distances
import sklearn.metrics as skm
from numpy import genfromtxt
import matplotlib.pyplot as plt
import csv
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

from algorithms import kMedoid

# Pytest installieren: python -m pip install pytest


def best_silhouette(border, score, matrix, k):
    ### Methode für besten Silhouettenkoeffizient (iterativ) ###
    i = 1
    cur_score = score
    while cur_score < border:
        cur_labels = []
        cur_m, cur_c = kMedoid.kMedoids(matrix, k)
        # for m in cur_m:
            # print(m)
        for cur_label in cur_c:
            for point in cur_c[cur_label]:
                cur_labels.append(cur_label)
                print("Graph:", point, "Cluster:", cur_label)
        cur_score = skm.silhouette_score(matrix, cur_labels, metric="euclidean")
        i = i + 1
        print(i, "_______")
    print('K-Medoid - silhouette-score:', cur_score)
    print('calinski-harabaz-score:', skm.calinski_harabaz_score(matrix, cur_labels))
    # export(cur_c, i)


def export(C, i):
    ### Export in .csv-Datei des Clusterings ###
    name = 'result-' + str(i) + '.csv'
    with open('..\\data\\output\\' + name, 'w', newline='') as file:
        header = ['Graph', 'Cluster']
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        for l in C:
            for p in C[l]:
                writer.writerow({'Graph': p, 'Cluster': l})
    file.close()
    print('Datei exportiert!')


def find_best_k(DD, lb, ub):
    ### optimale Clusteranzahl für k-medoid finden ###
    for k in range(lb, ub):
        print('k:', k)
        M, C = kMedoid.kMedoids(DD, k)
        labels = []
        for label in C:
            for point_idx in C[label]:
                labels.append(label)
        score = skm.silhouette_score(DD, labels, metric="euclidean")
        print('K-Medoid - silhouette-score:', score)


def print_clustering(M, C):
    ### Clusteringergebnisse ausgeben ###
    print('medoids:', M)
    print('')
    print('clustering result:')
    for label in C:
        for point_idx in C[label]:
            print("Graph:", point_idx, "Cluster:", label)


def plot(C):
    ### visuelle Darstellung des Clustering (fehlerhaft) ###
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


"""K-Medoid"""


def k_medoid():
    k = 5
    M, C = kMedoid.kMedoids(DD, k)

    labels = []
    for label in C:
        for point_idx in C[label]:
            labels.append(label)

    score = skm.silhouette_score(DD, labels, metric="euclidean")
    print('silhouette-score:', score)
    # print('calinski-harabaz-score:', skm.calinski_harabaz_score(data, labels))
    # print('davies-bouldin-score:', skm.davies_bouldin_score(data, labels))

    """interne Evaluation (Silhouette): optimales k und besten Koeffizientenwert finden"""
    # find_best_k(DD, 2, 18)
    # best_silhouette(-1, score, DD, k)

    """externe Evaluation (Rand-Index): 10x durchlaufen lassen (gleiche Anzahl k)"""
    # for i in range(0, 10):
    #   M, C = kMedoid.kMedoids(DD, k)
    # export(C, i+1)

    # https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-clustering-1.html
    # https://stats.stackexchange.com/questions/15158/precision-and-recall-for-clustering
    # https://scikit-learn.org/stable/modules/clustering.html#fowlkes-mallows-scores


"""AGNES"""


def agnes():
    data = data_matrix
    linked = linkage(data, 'average')
    f = fcluster(linked, t=1)
    # single, complete, average, weighted, centroid, median, ward
    # labelList = range(1, 6)

    # plt.figure(figsize=(20, 10))
    dendrogram(linked, orientation='top', distance_sort='ascending')
    print('AGNES - silhouette-score:', skm.silhouette_score(data, f, metric="euclidean"))
    plt.show()
    # https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html


###################################
##### Data #####
data_vectors = genfromtxt('..\\data\\lenz\\vectors_lenz.txt', delimiter=";")
# bei vectors_5 nicht die ersten 5 Graphen sondern manuelle Auswahl
# Cluster (0,2), (1,4) und (3)
data_matrix = genfromtxt('..\\data\\symmetrized\\avg_symmetrized_matrix_lenz.csv', delimiter=";")
##### Distanzmatrizen #####
D = pairwise_distances(data_vectors, metric='euclidean')
DD = genfromtxt('..\\data\\symmetrized\\min_symmetrized_matrix_lenz.csv', delimiter=";")
##### Algorithmen #####
k_medoid()
agnes()
###################################