import numpy as np

def Power_Method(A, x0, iteration):
    
    eigenvalue = 0
    eigenvector = x0
    i = 0
    while i < iteration:

        u0 = x0/np.linalg.norm(x0)
        eigenvector = np.matmul(A,u0)
        eigenvalue = np.matmul(np.transpose(u0),eigenvector)
        x0 = eigenvector
        i +=1

    return "the dorminant eigenvalue is: {0}, and the dorminant eigenvector is: {1}".format(eigenvalue,eigenvector)

A = np.array([[1,5],[5,6]])
x0 = np.array([[1,1]]).T

print(Power_Method(A,x0,2))

def Inverse_Power_Method(A,x0, iteration):

    eigenvalue = 0
    eigenvector = x0
    i = 0
    while i < iteration:

        u0 = x0/np.linalg.norm(x0)
        eigenvector = np.matmul(np.linalg.inv(A),u0)
        eigenvalue = np.matmul(np.transpose(u0),eigenvector)
        x0 = eigenvector
        i +=1

    return "the smallest eigenvalue is: {0}, and the smallest eigenvector is: {1}".format(eigenvalue,eigenvector)