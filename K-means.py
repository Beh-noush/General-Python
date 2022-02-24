import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets

def generate_data(n, d,  k):
  '''
  generates n data points belonging to k Gaussian clusters
  Inputs
  ------
  n: int
    size of the dataset
    
  d: int
    dimension of the data points (number of features)
    
  k: int
    number of clusters
    
  Returns
  -------
  tuple of size 2, with the first entity being an array of shape (n,d), containing the features, and the second entity an array of size (n) containing the labels of all data.
  '''
  return datasets.make_blobs(n,  num_features = d, centers = [(1,1), (3,3)] , random_state = 0)

def find_distance(data, means):
  '''
  
  Inputs
  --------
  data:
  
  means:
  
  Returns
  --------
  
  '''
  
  num_data = data.shape[0]
  num_clusters = len(means)
  dist_array = np.zeros(num_data, num_clusters) #an array to store the distance between each data point and each estimated mean value.
  for i in range(num_data):
    for j in range(num_clusters):
      dist_array[i][j] = np.linalg.norm(data[i] - means[j]) 
  return dist_array 
  
def cluster_distances(means):
  '''
  gives the distance of cluster centers from the origin
  Inputs
  ------
  means: list
         list of numpy arrays of shape(num_features)
  Returns
  ------
         list of float numbers, which represent distances of the cluster means from the origin
  '''
  return np.array([np.linalg.norm(mean) for mean in means])
  
  
  
def assign_label(data, means):
  '''
  assigns labels to the samples in a given dataset, data.
  '''
  Inputs
  -------
  data: numpy array of shape (batch_size, num_features) or (batch_size, num_features+1)
  means: a list of k numpy array of shape (num_features)
    
  Returns
  --------
       numpy array of shape (batch_size, num_features+1)
  '''
  distance_array = find_distance(data,means)
  closest_cluster = np.argmin(distance_array, axis = 1)
  return np.concatenate((data, closest_cluster.reshape(-1,1)), axis = 1)


def find_mean(data, num_clusters):
  '''
  finds the means of k clusters to which data points belong
  Inputs
  -------
  data:numpy array of shape  (batch_size, num_features+1)
    
  num_clusters: int
    number of clusters
  Returns
  -------
     outputs a list of k numpy arrays of shape(num_features)
  '''
  for n_clus in num_clusters:
    means[n_clus] = np.mean(data[np.where(data[:,-1] == n_clus)], axis = 0)
  return means  






def k_means(data, k):
  '''
  returns k arrays of shape (num_features) as the means of k clusters.
  
  Inputss
  ---------
  data:
     array of size (batch_size, num_features)
     
  k:   int
     number of clusters to learn
     
  Returns
  ----------
     k arrays of shape (num_features) as the means of k clusters
  '''
  batch_size, num_feat = data.shape[0], data.shape[1]
  data = np.concatenate(data, np.zeros(batch_size)) #We added one column to put the returned label of the data
  mean_values = [np.array(num_features).uniform(-1,1) for i in range(k)]
  dist_1 = cluster_distances(mean_values)
  
  converge = False
  while not converge:
    data = assign_label(data[:,:num_feat+1], means) # Notice: this data has shape (batch_size, num_features+1)!
    mean_values = find_mean(data, k)
    dist_2 = cluster_distances(mean_values)    
    converge = True not in np.linalg.norm(dist_2 - dist_1)/dist_1>.01
    dist_1 = dist2
  return (means, data)
  


def plot_k_means(data,k):
  pass
  
data,labels =  generate_data(120, 2,  3)
