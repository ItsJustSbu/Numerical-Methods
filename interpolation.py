def linear_interpolation(f,x0,x1,x):
    """
    Linear Interpolation uses 2 points (x0,f(x0)) and (x1,f(x1)) to approximate values between
    x0 and x1 by using a straight line.
    This interpolation method does not work well for non-linear functions

    """

    slope = (f(x1)-f(x0)) / (x1-x0)
    interpolation = f(x0) + (slope*(x-x0)) 
    return "the value using linear interpolation is {0}".format(interpolation)

def quadratic_interpolation(f,x0,x1,x2,x):
    """
    Quadratic Interpolation uses 3 points (x0,f(x0)) and (x1,f(x1)) and (x2,f(x2)) to approximate values between
    x0 and x2 by using a parabola
    This interpolation method introduces more points as well as a curvature which improves the approximation compared to
    the Linear Interpolation

    """

    a0 = f(x0)
    a1 = ( f(x1) - f(x0)) / (x1-x0)
    a2 = (((f(x2)-f(x1))/(x2-x1)) - a1) /(x2-x0)
    interpolation = a0 + (a1*(x1-x0)) + (a2*(x-x0)*(x-x1))
    return "the value using Quadratic interpolation is {0}".format(interpolation)


#Question 5
def Newton_interpolation_coefficients(x,y):

    difference_table = np.zeros([len(x),len(x)])

    difference_table[:,0] = y

    for j in range(1,len(x)):
        for i in range(len(x) - j):
            difference_table[i][j] = (difference_table[i+1][j-1] - difference_table[i][j-1]) / (x[i+j]-x[i])
    
    coefficients = difference_table[0,:]

    return coefficients


