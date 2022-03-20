import numpy as np
def extract():
    samples = 349
    features = 4
    ####DATA EXTRACTION###
    data = open("data.txt", "r+")
    data = data.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")
        data[i] = data[i].split(",")
        for feature in data[i]:
            feature = float(feature)
    ####DATA EXTRACTION###

    #print(data)
    db = np.zeros((samples, features), dtype="float32")
    for i in range(samples):
        for j in range(features):
            #print(data[i][j])
            db[i, j] = data[i][j]
    return db