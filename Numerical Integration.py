#Trapezoidal Formula

def trapezoidal_formula(f,n,a,b):
    x0 = a
    xn = b
    h = (b-a)/n
    sum = 0
    for i in range(n):
        if i == 0:
            sum=sum+ f(x0)
        else:
           sum=sum+ 2*(f(x0 + i*h))
    sum= sum+ f(xn)
    return (h/2)*sum

#Midpoint formula

def midpoint(f,n,a,b):

    h = (b-a)/n
    integral_approx = 0
    for i in range(n):
        integral_approx+= f(a+(h/2)+i*h)
    return h*integral_approx


#Double integration using Midpoint rule
def double_integral(f,a,b,c,d,n_x,n_y):
    hx = (b-a)/n_x
    hy = (d-c)/n_y
    x0 = a
    y0 = c
    integral_approx = 0
    for i in range(n_x+1):
        for j in range(n_y+1):
            xi = x0 + i*hx
            yj = y0 + j*hy
            if (xi == x0 or yj == y0):
                integral_approx += (hx/2)*(hy/2)*f(xi,yj)
            elif(xi == b or yj==d):
                integral_approx += (hx/2)*(hy/2)*f(xi,yj)
            else:
                integral_approx += 2*(hx/2)*(hy/2)*f(xi,yj)
    return integral_approx
