import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy.cluster.hierarchy import dendrogram, linkage

from scipy.spatial.distance import pdist

data = genfromtxt('..\\data\\pfister\\matrix_full.txt', delimiter=";")
print(data)
print(pdist(data))
linked = linkage(data, 'average')
# single, complete, average, weighted, centroid, median, ward

# labelList = range(1, 6)

plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='ascending')
plt.show()

# https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
