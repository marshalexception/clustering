import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib

from scipy.spatial.distance import pdist

data = genfromtxt('..\\data\\vectors.txt', delimiter=";")
linked = linkage(data, 'average')
f = fcluster(linked, t=1)
print(f)
# single, complete, average, weighted, centroid, median, ward
# labelList = range(1, 6)

# plt.figure(figsize=(20, 10))
dendrogram(linked, orientation='top', distance_sort='ascending')
plt.show()
# https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
