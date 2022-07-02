def Newton(f, fprime, x0):

    root = 0
    while True:
        root = x0 - (f(x0)/fprime(x0))

        if(abs(root-x0) <= 1*(10**-5)):
            break

        x0 = root
    
    return root

#Question 2

def Newton_systems(F, J, x0, tol):

    root = 0
    while True:
        root = x0 - np.dot(np.linalg.inv(J(x0)),F(x0))
        stopping_criteria = (np.linalg.norm(root-x0))/(np.linalg.norm(x0))
        if (stopping_criteria < tol):
            break
        x0 = root
    
    return root

F = lambda x: np.array([x[0]**3 - 3*x[0]*x[1]**2 - 1,
3*x[0]**2*x[1] - x[1]**3])

J = lambda x: np.array([[3*x[0]**2 - 3*x[1]**2, -6*x[0]*x[1]],
[6*x[0]*x[1], 3*x[0]**2 - 3*x[1]**2]])
x0 = np.array([-.6, .6])
tol = 1e-6
print(Newton_systems(F,J,x0,tol))

