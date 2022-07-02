from math import *


#Forwards difference equation
def forward(f,x,h):

    return ((f(x+h)-f(x))/h)

#Backwards difference equation
def backward(f,x,h):

    return ((f(x)-f(x-h))/h)


#Central Difference equation
def central(f,x,h):
    
    return (f(x+h)-f(x-h))/(2*h)

#Richardson's Extrapolation
def Richardson(f0,arr,rows):

    h = [0.1/(2**i) for i in range(rows)]
    for i in range(rows):
        arr[i][0] = i+1
        arr[i][1] = h[i]
        arr[i][2] = backwards(f0,1,h[i])

    j = 3

    index = 0

    while j < 12:
        i = arr[index][0]
        if i == j-2:
            index +=1
            j = 3
        else:
            arr[index][j] = (1/(pow(4,j-2)-1))*((pow(4,j-2)*arr[index][j-1])-arr[index-1][j-1])
            j+=1
    return arr
