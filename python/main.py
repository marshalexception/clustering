from sklearn.metrics.pairwise import pairwise_distances
import sklearn.metrics as skm
from sklearn.cluster import AgglomerativeClustering
from numpy import genfromtxt
import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

from algorithms import kMedoid

# Pytest installieren: python -m pip install pytest

#-------------------------------------------------------
# Methode für besten Silhouettenkoeffizient (iterativ)


def best_silhouette(border, score, matrix, k):
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
    export(cur_c, 0, 'min', 'k-medoid')

#-------------------------------------------------------
# Export in .csv-Datei des Clusterings


def export(C, i, strategy, algorithm):
    name = str(strategy) + '_' + str(algorithm) + '_result_' + str(i) + '.csv'
    with open('..\\data\\output\\' + name, 'w', newline='') as file:
        header = ['Graph', 'Cluster']
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        for l in C:
            for p in C[l]:
                writer.writerow({'Graph': p, 'Cluster': l})
    file.close()
    print('Datei exportiert!')

#-------------------------------------------------------
# optimale Clusteranzahl für k-medoid finden


def find_best_k(DD, lb, ub):
    for k in range(lb, ub):
        print('k:', k)
        M, C = kMedoid.kMedoids(DD, k)
        labels = []
        for label in C:
            for point_idx in C[label]:
                labels.append(label)
        score = skm.silhouette_score(DD, labels, metric="euclidean")
        print('K-Medoid - silhouette-score:', score)

#-------------------------------------------------------
# Clusteringergebnisse ausgeben


def print_clustering(M, C):
    print('medoids:', M)
    print('clustering result:')
    for label in C:
        for point_idx in C[label]:
            print("Graph:", point_idx, "Cluster:", label)


#-------------------------------------------------------
# visuelle Darstellung des Clustering (fehlerhaft)


def plot(C):
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


#-------------------------------------------------------
# K-Medoid


def k_medoid():
    k = 4
    M, C = kMedoid.kMedoids(data_matrix, k)

    labels = []
    for label in C:
        for point_idx in C[label]:
            labels.append(label)

    # export(C, 0)
    # print_clustering(M, C)
    print(labels)
    print_clustering(M, C)
    score = skm.silhouette_score(data_matrix, labels, metric="euclidean")
    print('silhouette-score:', score)
    # print('calinski-harabaz-score:', skm.calinski_harabaz_score(data, labels))
    # print('davies-bouldin-score:', skm.davies_bouldin_score(data, labels))

    """interne Evaluation (Silhouette): optimales k und besten Koeffizientenwert finden"""
    # for i in range(0, 10):
    #   find_best_k(data_matrix, 2, 18)
    # best_silhouette(-0.0100, score, data_matrix, k)

    """externe Evaluation (Rand-Index): n Durchläufe (gleiche Anzahl k)"""
    n = 10
    silhouettes = []
    calinski_harabaz_scores = []
    for i in range(0, n):
      labels = []
      # M, C = kMedoid.kMedoids(data_matrix, k)
      # for label in C:
        #   for point_idx in C[label]:
          #     labels.append(label)
      # silhouettes.append(skm.silhouette_score(data_matrix, labels, metric="euclidean"))
      # calinski_harabaz_scores.append(skm.calinski_harabaz_score(data_matrix, labels))
      # export(C, i+1, 'min', 'k-medoid')
    # print('durchschnittlicher silhouette-score:', np.sum(silhouettes)/n)
    # print('durchschnittlicher calinski-harabaz-score:', np.sum(calinski_harabaz_scores)/n)

    # https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-of-clustering-1.html
    # https://stats.stackexchange.com/questions/15158/precision-and-recall-for-clustering
    # https://scikit-learn.org/stable/modules/clustering.html#fowlkes-mallows-scores


#-------------------------------------------------------
# AGNES


def agnes():
    data = data_matrix
    linked = linkage(data, method='centroid')
    linked_labels = fcluster(linked, t=1)
    # single, complete, average, weighted, centroid, median, ward
    # labelList = range(1, 6)

    # plt.figure(figsize=(20, 10))
    # dendrogram(linked, orientation='top', distance_sort='ascending')
    # print('AGNES - silhouette-score:', skm.silhouette_score(data, linked_labels, metric="euclidean"))
    # print('AGNES - calinski-harabaz-score:', skm.calinski_harabaz_score(data, linked_labels))

    cluster = AgglomerativeClustering(n_clusters=5, linkage='single').fit(data)
    dendrogram(cluster.children_, orientation='top', distance_sort='ascending')
    plt.show()
    # print('AGNES - silhouette-score:', skm.silhouette_score(data, cluster.labels_, metric="euclidean"))
    # print('AGNES - calinski-harabaz-score:', skm.calinski_harabaz_score(data, cluster.labels_))
    # https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html


#-------------------------------------------------------
## Main
# Data
data_vectors = genfromtxt('..\\data\\lenz\\vectors_lenz.txt', delimiter=";")
# bei vectors_5 nicht die ersten 5 Graphen sondern manuelle Auswahl
# Cluster (0,2), (1,4) und (3)
data_matrix = np.array(genfromtxt('..\\data\\symmetrized\\min_symmetrized_matrix_lenz.csv', delimiter=";"))

# Distanzmatrizen
D = pairwise_distances(data_vectors, metric='euclidean')
# DD = genfromtxt('..\\data\\symmetrized\\min_symmetrized_matrix_lenz.csv', delimiter=";")

# Algorithmen
k_medoid()
# agnes()
#-------------------------------------------------------