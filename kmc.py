import numpy as np
from math import sqrt
from random import randint
from TrainingData import extract

###K MEANS CLUSTERING###
class KMC:
    def __init__(self):
        #get data
        self.db = extract()
        self.features = 4
        self.samples = 349
        #initialise value of k
        self.k = 4
        self.groups = []
        #initialise centriods and preveious sentriods
        self.centroids = []
        self.centroids_p = []
        for k in range(self.k):
            self.centroids_p.append(np.zeros((self.features), dtype="float64"))
        self.clust= []
    def getWords(self):
        words = []
        file = open("words.txt", "r+")
        for line in file:
            words.append(line.rstrip())
        return words
    def initialize(self):
        self.centers = []
        for i in range(self.k):
            self.centers.append(randint(0, self.samples-1))
        for i in range(len(self.db)):
            dists = []
            for k in range(self.k):
                sqrDist = 0
                K = self.centers[k]
                for j in range(len(self.db[i])):
                    sqrDist += (self.db[i][j] - self.db[K][j])**2
                dists.append(sqrt(sqrDist))
            #print(dists)
            self.clust.append(dists.index(min(dists)))
    #update center of clusters
    def update(self):
        for K in range(self.k):
            cen = np.zeros((self.features), dtype="float64")
            for i in range(len(self.db.T)):
                total = 0
                for j in range(len(self.db.T[i])):
                    if self.clust[i] == K:
                        total += self.db.T[i][j]
                cen[i] = total / len(self.db)
            self.centroids.append(cen)
        self.clust = []
        self.cluster()
    #recluster words
    def cluster(self):
        for i in range(len(self.db)):
            dists = []
            for k in range(self.k):
                sqrDist = 0
                for j in range(len(self.db[i])):
                    sqrDist += (self.db[i][j] - self.centroids[k][j])**2
                dists.append(sqrt(sqrDist))
            #print(dists)
            self.clust.append(dists.index(min(dists)))
        self.isConverged()
    #check if clusters are converged
    def isConverged(self):
        cnv = True
        for i in range(len(self.centroids)):
            for j in range(len(self.centroids[i])):
                if self.centroids[i][j] - self.centroids_p[i][j] > 0:
                    cnv = False
        if cnv:
            self.convert()
        else:
            self.convert()
            self.centroids_p = self.centroids
            self.centroids = []
            self.update()
    #return words in each cluster
    def convert(self):
        words = self.getWords()
        print(len(self.clust), len(words))
        #self.words = self.words.split(",")
        for k in range(self.k):
            self.groups.append([])
            for i in range(len(words)):
                if self.clust[i] == k and words[i] not in self.groups[k]:
                    self.groups[k].append(words[i])
        for group in self.groups:
            if len(group) > 0:
                print(group, "\n")
def cluster():
    kmc = KMC()
    kmc.initialize()
    kmc.update()
    kmc.isConverged()
cluster()