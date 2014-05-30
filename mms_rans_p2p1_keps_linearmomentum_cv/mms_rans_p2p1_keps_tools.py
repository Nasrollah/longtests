from math import sin, cos, tanh, pi

def u(X):
    return 0.600*sin(X[1]) + cos(X[0]) + 2.50

def v(X):
    return X[1]*sin(X[0])

def p(X):
    return sin(X[0]*X[1]/pi) + sin(X[0]) + cos(X[1]) - 1.00

def temperature(X):
    return 3.70*sin(1.30*X[0]*X[1]/pi) - 1.80*sin(1.70*X[0]) - 1.30*cos(2.10*X[1]) + 5.20

def rho(X):
    return 37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0

def ke(X):
    return 0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900

def eps(X):
    return 1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20

def forcing_u(X):
    return 0.600*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*X[1]*sin(X[0])*cos(X[1]) - (-0.600*sin(X[1]) + cos(X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (0.600*sin(X[1]) + cos(X[0]) + 2.50)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*sin(X[0]) + 2*(48.1*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 30.6*cos(1.70*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*sin(X[0])/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - 2*(1.02*X[1]*cos(0.600*X[0]*X[1]/pi)/pi - 2.66*cos(0.700*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*sin(X[0])/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 + 4*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*sin(X[0])/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (48.1*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 27.3*sin(2.10*X[1]))*(X[1]*cos(X[0]) + 0.600*cos(X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) + (1.02*X[0]*cos(0.600*X[0]*X[1]/pi)/pi - 3.44*sin(0.800*X[1]))*(X[1]*cos(X[0]) + 0.600*cos(X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 - 2*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(X[1]*cos(X[0]) + 0.600*cos(X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) + 2*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*cos(X[0])/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (32.0666666666667*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 20.4*cos(1.70*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900) + (48.1*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 30.6*cos(1.70*X[0]))*(0.400*sin(0.700*X[1]) + 0.266666666666667*cos(0.800*X[0]*X[1]/pi) + 0.600*cos(0.600*X[0]) + 0.600) - (-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(24.6666666666667*sin(1.30*X[0]*X[1]/pi) - 12.0*sin(1.70*X[0]) - 8.66666666666667*cos(2.10*X[1]) + 41.3333333333333) + (-0.213333333333333*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.360*sin(0.600*X[0]))*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0) + X[1]*cos(X[0]*X[1]/pi)/pi - 26.1629508970000*sin(1.30*X[0]*X[1]/pi) + 12.7279220580000*sin(1.70*X[0]) + 0.420*sin(X[1]) + 1.70*cos(X[0]) + 9.19238815300000*cos(2.10*X[1]) - 43.8406204220000

def forcing_v(X):
    return (0.600*sin(X[1]) + cos(X[0]) + 2.50)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*X[1]*cos(X[0]) + (0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*X[1]*sin(X[0])/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) + (37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*X[1]*sin(X[0])**2 - (48.1*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 30.6*cos(1.70*X[0]))*(X[1]*cos(X[0]) + 0.600*cos(X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) + (1.02*X[1]*cos(0.600*X[0]*X[1]/pi)/pi - 2.66*cos(0.700*X[0]))*(X[1]*cos(X[0]) + 0.600*cos(X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 - 2*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(X[1]*cos(X[0]) + 0.600*cos(X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - 2*(48.1*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 27.3*sin(2.10*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*sin(X[0])/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) + 2*(1.02*X[0]*cos(0.600*X[0]*X[1]/pi)/pi - 3.44*sin(0.800*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*sin(X[0])/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 - 4*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*sin(X[0])/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (32.0666666666667*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 18.2*sin(2.10*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900) + (48.1*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 27.3*sin(2.10*X[1]))*(0.400*sin(0.700*X[1]) + 0.266666666666667*cos(0.800*X[0]*X[1]/pi) + 0.600*cos(0.600*X[0]) + 0.600) - (-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(24.6666666666667*sin(1.30*X[0]*X[1]/pi) - 12.0*sin(1.70*X[0]) - 8.66666666666667*cos(2.10*X[1]) + 41.3333333333333) + (-0.213333333333333*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.280*cos(0.700*X[1]))*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0) + 0.700*X[1]*sin(X[0]) + X[0]*cos(X[0]*X[1]/pi)/pi - 26.1629508970000*sin(1.30*X[0]*X[1]/pi) + 12.7279220580000*sin(1.70*X[0]) - sin(X[1]) + 9.19238815300000*cos(2.10*X[1]) - 43.8406204220000

def forcing_temperature(X):
    return (4.81*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 2.73*sin(2.10*X[1]))*X[1]*sin(X[0]) - ((0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) + 1.00)*(-6.25300000000000*X[0]**2*sin(1.30*X[0]*X[1]/pi)/pi**2 - 6.25300000000000*X[1]**2*sin(1.30*X[0]*X[1]/pi)/pi**2 + 5.20200000000000*sin(1.70*X[0]) + 5.73300000000000*cos(2.10*X[1])) + (0.600*sin(X[1]) + cos(X[0]) + 2.50)*(4.81*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 3.06*cos(1.70*X[0])) - (4.81*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 3.06*cos(1.70*X[0]))*((48.1*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 30.6*cos(1.70*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (1.02*X[1]*cos(0.600*X[0]*X[1]/pi)/pi - 2.66*cos(0.700*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 + 2*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)) - (4.81*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 2.73*sin(2.10*X[1]))*((48.1*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 27.3*sin(2.10*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (1.02*X[0]*cos(0.600*X[0]*X[1]/pi)/pi - 3.44*sin(0.800*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 + 2*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20))

def forcing_ke(X):
    return (-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*X[1]*sin(X[0]) + (0.600*sin(X[1]) + cos(X[0]) + 2.50)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0) - (0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*(X[1]**2*cos(X[0])**2 + 1.20*X[1]*cos(X[0])*cos(X[1]) + 4*sin(X[0])**2 + 0.360*cos(X[1])**2)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - ((0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) + 0.700)*(-0.256*X[0]**2*cos(0.800*X[0]*X[1]/pi)/pi**2 - 0.256*X[1]**2*cos(0.800*X[0]*X[1]/pi)/pi**2 - 0.294*sin(0.700*X[1]) - 0.324*cos(0.600*X[0])) - (-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*((48.1*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 30.6*cos(1.70*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (1.02*X[1]*cos(0.600*X[0]*X[1]/pi)/pi - 2.66*cos(0.700*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 + 2*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)) - (-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*((48.1*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 27.3*sin(2.10*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (1.02*X[0]*cos(0.600*X[0]*X[1]/pi)/pi - 3.44*sin(0.800*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 + 2*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)) + (0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(34.0118361661000*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 34.0118361661000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi + 19.3040151213000*sin(2.10*X[1]) - 21.6374674986000*cos(1.70*X[0]))/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) + (37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)

def forcing_eps(X):
    return (1.02*X[0]*cos(0.600*X[0]*X[1]/pi)/pi - 3.44*sin(0.800*X[1]))*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*X[1]*sin(X[0]) + (0.600*sin(X[1]) + cos(X[0]) + 2.50)*(1.02*X[1]*cos(0.600*X[0]*X[1]/pi)/pi - 2.66*cos(0.700*X[0]))*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0) - (0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*(X[1]**2*cos(X[0])**2 + 1.20*X[1]*cos(X[0])*cos(X[1]) + 4*sin(X[0])**2 + 0.360*cos(X[1])**2) + (0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(34.0118361661000*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 34.0118361661000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi + 19.3040151213000*sin(2.10*X[1]) - 21.6374674986000*cos(1.70*X[0]))*tanh((0.707106781000000*X[1]*sin(X[0]) + 0.424264068600000*sin(X[1]) + 0.707106781000000*cos(X[0]) + 1.76776695250000)/((0.600*sin(X[1]) + cos(X[0]) + 2.50)**2.00 - (0.707106781000000*X[1]*sin(X[0]) + 0.424264068600000*sin(X[1]) + 0.707106781000000*cos(X[0]) + 1.76776695250000)**2.00 + (X[1]*sin(X[0]))**2.00)**0.500) - ((0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) + 0.700)*(-0.612*X[0]**2*sin(0.600*X[0]*X[1]/pi)/pi**2 - 0.612*X[1]**2*sin(0.600*X[0]*X[1]/pi)/pi**2 + 1.86200000000000*sin(0.700*X[0]) - 2.75200000000000*cos(0.800*X[1])) - (1.02*X[1]*cos(0.600*X[0]*X[1]/pi)/pi - 2.66*cos(0.700*X[0]))*((48.1*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 30.6*cos(1.70*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (1.02*X[1]*cos(0.600*X[0]*X[1]/pi)/pi - 2.66*cos(0.700*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 + 2*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)) - (1.02*X[0]*cos(0.600*X[0]*X[1]/pi)/pi - 3.44*sin(0.800*X[1]))*((48.1*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 27.3*sin(2.10*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20) - (1.02*X[0]*cos(0.600*X[0]*X[1]/pi)/pi - 3.44*sin(0.800*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2 + 2*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)) + (37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)

def P_ke(X):
    return (0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*(X[1]**2*cos(X[0])**2 + 1.20*X[1]*cos(X[0])*cos(X[1]) + 4*sin(X[0])**2 + 0.360*cos(X[1])**2)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)

def P_eps(X):
    return (0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)*(X[1]**2*cos(X[0])**2 + 1.20*X[1]*cos(X[0])*cos(X[1]) + 4*sin(X[0])**2 + 0.360*cos(X[1])**2)

def A_ke(X):
    return (-37.0*sin(1.30*X[0]*X[1]/pi) + 18.0*sin(1.70*X[0]) + 13.0*cos(2.10*X[1]) - 62.0)*(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)

def A_eps(X):
    return (-37.0*sin(1.30*X[0]*X[1]/pi) + 18.0*sin(1.70*X[0]) + 13.0*cos(2.10*X[1]) - 62.0)*(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)**2.00/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)

def B_ke(X):
    return -(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(34.0118361661000*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 34.0118361661000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi + 19.3040151213000*sin(2.10*X[1]) - 21.6374674986000*cos(1.70*X[0]))/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)

def B_eps(X):
    return -(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)*(34.0118361661000*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 34.0118361661000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi + 19.3040151213000*sin(2.10*X[1]) - 21.6374674986000*cos(1.70*X[0]))*tanh((0.707106781000000*X[1]*sin(X[0]) + 0.424264068600000*sin(X[1]) + 0.707106781000000*cos(X[0]) + 1.76776695250000)/((0.600*sin(X[1]) + cos(X[0]) + 2.50)**2.00 - (0.707106781000000*X[1]*sin(X[0]) + 0.424264068600000*sin(X[1]) + 0.707106781000000*cos(X[0]) + 1.76776695250000)**2.00 + (X[1]*sin(X[0]))**2.00)**0.500)

def EV(X):
    return (0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 0.900)**2*(37.0*sin(1.30*X[0]*X[1]/pi) - 18.0*sin(1.70*X[0]) - 13.0*cos(2.10*X[1]) + 62.0)/(1.70*sin(0.600*X[0]*X[1]/pi) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.800*X[1]) + 8.20)

def velocity(X):
   return [u(X), v(X)]

def forcing_velocity(X):
   return [forcing_u(X), forcing_v(X)]