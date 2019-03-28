import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans


data = genfromtxt('..\\data\\pfister\\vectors_new.txt', delimiter=";")
linked = linkage(data, 'single')

labelList = range(1, 90)

plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.show()