import numpy as np

def pass_triangles():
    with open("p102_triangles.txt") as f:
        data = f.readlines()

    array = np.zeros((len(data), 6))
    for i, d in enumerate(data):
        d = d.strip()
        d = d.split(",")

        array[i] = np.array([int(x) for x in d])
    return array

def bary(data):
    a = ((data[:, 3] - data[:, 5])*(-data[:,4]) + (data[:, 4] - data[:, 2])*(-data[:, 5]))/((data[:, 3] - data[:, 5])*(data[:, 0] - data[:, 4]) + (data[:, 4] - data[:, 2])*(data[:,1] - data[:, 5]))
    b = ((data[:, 5] - data[:, 1])*(-data[:, 4])+ (data[:, 0] - data[:, 4])*(-data[:, 5]))/((data[:, 3] - data[:, 5])*(data[:, 0] - data[:, 4]) + (data[:, 4] - data[:, 2])*(data[:,1] - data[:, 5]))
    c = 1 - a - b
    return a,b,c

data = pass_triangles()
a,b,c = bary(data)

print("done")