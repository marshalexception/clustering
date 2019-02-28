from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

#need to install pytest: python -m pip install pytest

from algorithms import kMedoid

# 3 points in dataset
data = np.array([[1,1,1],
                [2,2,2],
                [10,10,10]])

# distance matrix
D = pairwise_distances(data, metric='euclidean')

# split into 2 clusters
M, C = kMedoid.kMedoids(D, 2)

print('medoids:')
for point_idx in M:
    print( data[point_idx] )

print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
       print('label {0}:　{1}'.format(label, data[point_idx]))

######################################

num_clusters = 0
mat = np.array([[0, 2, 6, 10, 9], [2, 0, 5, 9, 8], [6, 5, 0, 4, 5], [10, 9, 4, 0, 3], [9, 8, 5, 3, 0]])
all_elements = ['a', 'b', 'c', 'd', 'e']
dissimilarity_matrix = pd.DataFrame(mat, index=all_elements, columns=all_elements)

