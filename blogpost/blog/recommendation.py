from .models import movies, meansize
import numpy as np
import pandas as pd

x = []
vectors = {}
y = []
ms = {}
###############################################################
def jaccard_sim(x, y):
	if len(x) == len(y):
		#eshterak
	    intersection = np.logical_and(x,y)
		#ejtema
	    union = np.logical_or(x,y)
	    similarity = intersection.sum()/ float(union.sum())
	    return similarity
		
###############################################################
def comp_distance(x, y,i,id):
	jacc_dist = jaccard_sim(x,y)
	return jacc_dist
###############################################################
def getKNN(id, K):

	distance = []
	#print(vectors)
	for i in vectors:
		if i != id:
			dist = comp_distance(vectors[i], vectors[id],i,id)
			distance.append((i, dist))
	distance = sorted(distance, key=lambda x: x[1], reverse=True)
	neighbors = []
	for j in range(K):
		neighbors.append(distance[j][0])
	return neighbors

###############################################################
def recommend(id):

	df = pd.DataFrame(list(movies.objects.values_list('vectors','movie_id')))
	df2 = pd.DataFrame(list(meansize.objects.values_list('movie_id','mean','size')))
	#print(df)
	y = df2.values.tolist()
	for i in y:
		ms[i[0]] = i[1], i[2]
	x = df.values.tolist()
	for i in x:
		vectors[i[1]] = list(map(int,i[0].split('|')))
	K = 500
	neighbors = getKNN(id, K)
	real_neighbors = []

	for i in neighbors:
		real_neighbors.append((i, ms[i][0] + ms[i][1]))
	real_neighbors = list(sorted(real_neighbors, key=lambda x: x[1], reverse=True))
	real=[]
	for i in real_neighbors:
		real.append(i[0])
	return real
