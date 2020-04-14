import pandas as pd
from datetime import datetime
import math

class Cluster:

    def __init__(self, i, group_no):
        self.no = group_no
        self.minTime = df['timestamp'][i]
        self.maxTime = df['timestamp'][i]
        self.devices = [df['device_id'][i]]
        self.coor = [[df['longitude'][i], df['latitude'][i]]]
        df['cluster'][i] = group.no

# Is i is near any cluster
def nearby(i, cluster):
    for loc in cluster.coor:
        if math.sqrt(math.pow(loc[0] - df['longitude'][i],2) \
        + math.pow(loc[1] - df['latitude'][i],2)) <= 0.1:
            return True
    return False

# Time distance between i,j
def time(i, cluster):
    return df['timestamp'][i] in range(cluster.minTime, cluster.maxTime)\
    or (df['timestamp'][i] - cluster.minTime).total_seconds() < 180 \
    or (cluster.maxTime - df['timestamp'][i]).total_seconds() < 180

# Return True if i and j are different devices
def device(i, cluster):
    return df['device_id'][i] not in cluster.devices

def isInGroup(i, cluster):
    if device(i, cluster):
        return False
    if time(i, cluster):
        return False
    if nearby(i, cluster):
        return False
    return True

def appendTo(i, cluster):
    if df['timestamp'][i] < cluster.minTime:
        cluster.minTime = df['timestamp'][i]
    elif df['timestamp'][i] > cluster.maxTime:
        cluster.maxTime = df['timestamp'][i]
    cluster.devices.append(df['device_id'][i])
    cluster.coor.append([df['longitude'][i], df['latitude'][i]])
    df['cluster'][i] = cluster.no
