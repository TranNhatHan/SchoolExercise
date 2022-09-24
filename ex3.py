import os
import numpy as np

def readData(filename, folder = ""):
    dt = np.loadtxt(os.path.join(folder, filename), delimiter=",")
    X = dt[:, 0]
    y = dt[:, 1]
    X = np.stack([np.ones(y.shape[0]), X], axis=1)
    return X, y

def calculateLoss(X, y, w):
    h = np.dot(X, w)
    m = X.shape[0]
    J = (1/(2*m))*np.sum(np.square(h - y))
    return J

def gradientDescent(X, y, w = [0, 0], alpha = 0.01, n = 1500):
    temp = []
    m = X.shape[0]
    for i in range(n):
        w = w - ((alpha/m)*(np.dot(X, w)) - y).dot(X)
        temp.append(calculateLoss(X, y, w))
    return w, temp

if __name__ == "__main__":
    X, y = readData("ex1data1.txt")
    w, ll = gradientDescent(X, y)
    print("Giá trị vector trọng số tối ưu tìm được theo thuật toán Gradient Descent - w_optimal:", w)
    print("List chứa tất cả các giá trị của hàm mất mát tương ứng với các giá trị vector trọng số tại mỗi bước lặp:", ll)