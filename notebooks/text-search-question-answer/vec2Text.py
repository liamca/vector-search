#!/usr/bin/env python
# coding: utf-8

import os
from os import listdir
from os.path import isfile, join
import glob

from pathlib import Path
import shutil
from shutil import rmtree

import gensim
import numpy as np
import math, random, collections, base64

from sklearn.cluster import KMeans

dataFile = './data/collection-small.tsv'
clusterCenterFile = 'cluster_centers_text.pkl'
testSamplesToTest = 500

def initializeVectorDictionary(dimensions):
    # Initialize vector dictionary
    vecDict = {}
    for d in range(dimensions):
        vecDict[str(d)] = []
    return vecDict

def convertFieldNumToString(dim):
    dimStr = str(dim)
    curStr = ''
    for i in range(len(dimStr)):
        curChar = dimStr[i]
        if curChar == '0':
            curStr += 'A'
        elif curChar == '1':
            curStr += 'B'
        elif curChar == '2':
            curStr += 'C'
        elif curChar == '3':
            curStr += 'D'
        elif curChar == '4':
            curStr += 'E'
        elif curChar == '5':
            curStr += 'F'
        elif curChar == '6':
            curStr += 'G'
        elif curChar == '7':
            curStr += 'H'
        elif curChar == '8':
            curStr += 'I'
        elif curChar == '9':
            curStr += 'J'
    return curStr

def convertVecToBucketStr(curVec, bucketRanges):
    vecStr = ''

    for d in range(len(curVec)):
        bucketVal = -1
        bucketCounter = 0
        for i in bucketRanges[d]:
            if curVec[d] < i:
                bucketVal = bucketCounter
                break
            bucketCounter+=1

        vecStr += convertFieldNumToString(d) + '_' + str(bucketVal).replace('-','~') + ' '

    return vecStr.strip()

# Find the closest cluster center index to a specified number (K)
def closest(lst, K):
    b = lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
    return lst.index(b)


def calculateWCSS(data):
    data = np.array(data).reshape(-1,1)  

    wcss = []
    for n in range(2, 21):
        kmeans = KMeans(n_clusters=n)
        kmeans.fit(X=data)
        wcss.append(kmeans.inertia_)

    return wcss

def optimalNumberOfClusters(wcss):
    x1, y1 = 2, wcss[0]
    x2, y2 = 20, wcss[len(wcss)-1]

    distances = []
    for i in range(len(wcss)):
        x0 = i+2
        y0 = wcss[i]
        numerator = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1)
        denominator = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
        distances.append(numerator/denominator)
    
    return distances.index(max(distances)) + 2

# Find the K-Means cluster centers for each dimension
def findClusterCenters(dimensions, vecDict):
    clusterCenters = {}
    counter = 0
    for d in range(dimensions):
        counter += 1
        if counter % 10 == 0:
            print ('Processed', counter, 'of', dimensions)
        numberOfClusters = optimalNumberOfClusters(calculateWCSS(vecDict[str(d)]))
        x = np.array(vecDict[str(d)])
        km = KMeans(n_clusters=numberOfClusters)
        km.fit(x.reshape(-1,1))  
        cluster_centers = km.cluster_centers_
        cluster_centers = sorted(cluster_centers.tolist())
        clusterList = []
        for cc in cluster_centers:
            clusterList.append(cc[0])
        clusterCenters[d] = clusterList
    return clusterCenters

def getFilesInDir(in_dir):
    return [os.path.join(dp, f) for dp, dn, filenames in os.walk(in_dir) for f in filenames]

def stringToBase64(content):
    return str(base64.b64encode(content.encode('ascii'))).replace("b'", "").replace("'", "")