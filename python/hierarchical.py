import matplotlib.pyplot as plt
from numpy import genfromtxt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.metrics import silhouette_score

data_matrix = genfromtxt('..\\data\\symmetrized\\avg_symmetrized_matrix_lenz.csv', delimiter=";")
data_vectors = genfromtxt('..\\data\\lenz\\vectors_lenz.txt', delimiter=";")

