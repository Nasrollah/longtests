from math import sin, cos, tanh, pi

def u1(X):
    return sin(X[0]**2 + X[1]**2) + 0.500

def v1(X):
    return 0.100*cos(X[0]**2 + X[1]**2) + 0.0500

def p(X):
    return (0.200*cos(X[0] + X[1]) + 0.300)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)

def rho1(X):
    return 0.500*sin(X[0]**2 + X[1]**2) + 0.750

def ie1(X):
    return 0.500*cos(X[0] + X[1]) + 0.750

def vfrac1(X):
    return 0.800

def forcing_u1(X):
    return 2*(0.100*cos(X[0]**2 + X[1]**2) + 0.0500)*(0.400*sin(X[0]**2 + X[1]**2) + 0.600)*X[1]*cos(X[0]**2 + X[1]**2) + 2*(0.400*sin(X[0]**2 + X[1]**2) + 0.600)*(sin(X[0]**2 + X[1]**2) + 0.500)*X[0]*cos(X[0]**2 + X[1]**2) + 0.800*(0.200*cos(X[0] + X[1]) + 0.300)*X[0]*cos(X[0]**2 + X[1]**2) + 2.98666666666667*X[0]**2*sin(X[0]**2 + X[1]**2) + 0.0746666666666667*X[0]*X[1]*cos(X[0]**2 + X[1]**2) + 2.24*X[1]**2*sin(X[0]**2 + X[1]**2) - 0.160*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*sin(X[0] + X[1]) - 0.282842712400000*sin(X[0]**2 + X[1]**2) - 2.61333333333333*cos(X[0]**2 + X[1]**2) - 0.424264068600000

def forcing_v1(X):
    return -0.200*(0.100*cos(X[0]**2 + X[1]**2) + 0.0500)*(0.400*sin(X[0]**2 + X[1]**2) + 0.600)*X[1]*sin(X[0]**2 + X[1]**2) - 0.200*(0.400*sin(X[0]**2 + X[1]**2) + 0.600)*(sin(X[0]**2 + X[1]**2) + 0.500)*X[0]*sin(X[0]**2 + X[1]**2) + 0.800*(0.200*cos(X[0] + X[1]) + 0.300)*X[1]*cos(X[0]**2 + X[1]**2) + 0.224*X[0]**2*cos(X[0]**2 + X[1]**2) + 0.746666666666667*X[0]*X[1]*sin(X[0]**2 + X[1]**2) + 0.298666666666667*X[1]**2*cos(X[0]**2 + X[1]**2) - 0.160*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*sin(X[0] + X[1]) - 0.0215093790666667*sin(X[0]**2 + X[1]**2) - 0.424264068600000

def forcing_rho1(X):
    return (0.0800*cos(X[0]**2 + X[1]**2) + 0.0400)*X[1]*cos(X[0]**2 + X[1]**2) + 2.00*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*X[0]*cos(X[0]**2 + X[1]**2) - 0.200*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*X[1]*sin(X[0]**2 + X[1]**2) + (0.800*sin(X[0]**2 + X[1]**2) + 0.400)*X[0]*cos(X[0]**2 + X[1]**2)

def forcing_ie1(X):
    return 1.60*(0.200*cos(X[0] + X[1]) + 0.300)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*X[0]*cos(X[0]**2 + X[1]**2) - 0.160*(0.200*cos(X[0] + X[1]) + 0.300)*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*X[1]*sin(X[0]**2 + X[1]**2) - 0.500*(0.100*cos(X[0]**2 + X[1]**2) + 0.0500)*(0.400*sin(X[0]**2 + X[1]**2) + 0.600)*sin(X[0] + X[1]) - 0.500*(0.400*sin(X[0]**2 + X[1]**2) + 0.600)*(sin(X[0]**2 + X[1]**2) + 0.500)*sin(X[0] + X[1]) + 0.000800*cos(X[0] + X[1])

def velocity1(X):
   return [u1(X), v1(X)]

def forcing_velocity1(X):
   return [forcing_u1(X), forcing_v1(X)]

def u2(X):
    return sin(X[0]**2 + X[1]**2) + 0.500

def v2(X):
    return 0.100*cos(X[0]**2 + X[1]**2) + 0.0500

def rho2(X):
    return 3.00

def ie2(X):
    return 3.00*X[1]

def vfrac2(X):
    return 0.200

def forcing_u2(X):
    return 2*(0.0600*cos(X[0]**2 + X[1]**2) + 0.0300)*X[1]*cos(X[0]**2 + X[1]**2) + 0.200*(0.200*cos(X[0] + X[1]) + 0.300)*X[0]*cos(X[0]**2 + X[1]**2) + 2*(0.600*sin(X[0]**2 + X[1]**2) + 0.300)*X[0]*cos(X[0]**2 + X[1]**2) + 0.560*X[0]**2*sin(X[0]**2 + X[1]**2) + 0.560*X[1]**2*sin(X[0]**2 + X[1]**2) - 0.0400*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*sin(X[0] + X[1]) - 0.560*cos(X[0]**2 + X[1]**2) - 0.424264068600000

def forcing_v2(X):
    return -0.200*(0.0600*cos(X[0]**2 + X[1]**2) + 0.0300)*X[1]*sin(X[0]**2 + X[1]**2) + 0.200*(0.200*cos(X[0] + X[1]) + 0.300)*X[1]*cos(X[0]**2 + X[1]**2) - 0.200*(0.600*sin(X[0]**2 + X[1]**2) + 0.300)*X[0]*sin(X[0]**2 + X[1]**2) + 0.0560*X[0]**2*cos(X[0]**2 + X[1]**2) + 0.0560*X[1]**2*cos(X[0]**2 + X[1]**2) - 0.0400*(0.500*sin(X[0]**2 + X[1]**2) + 0.750)*sin(X[0] + X[1]) + 0.0560*sin(X[0]**2 + X[1]**2) - 0.424264068600000

def forcing_ie2(X):
    return 0.180*cos(X[0]**2 + X[1]**2) + 0.0900

def velocity2(X):
   return [u2(X), v2(X)]

def forcing_velocity2(X):
   return [forcing_u2(X), forcing_v2(X)]

