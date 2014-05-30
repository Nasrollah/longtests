from math import sin, cos, tanh, pi, e, sqrt

def u(X):
    return 1.50*sin(0.750*X[1]) + 10.0*cos(0.6*X[0]) + 1.50*cos(0.750*X[1]) + 5.00

def v(X):
    return 6.0*X[1]*sin(0.6*X[0])

def p(X):
    return sin(X[0]*X[1]/pi) + sin(X[0]) + cos(X[1]) - 1.00

def rho(X):
    return 370.*sin(1.30*X[0]*X[1]/pi) - 180.*sin(1.70*X[0]) - 130.*cos(2.10*X[1]) + 520.

def ke(X):
    return 0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00

def eps(X):
    return -3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2

def forcing_u(X):
    return -0.297*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)*sin(0.6*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 0.0247500000000000*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*(3.6*X[1]*cos(0.6*X[0]) - 1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 24.0*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)*sin(0.6*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) - 2*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)*(3.6*X[1]*cos(0.6*X[0]) - 1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) - (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.843750000000000*sin(0.750*X[1]) + 3.6*cos(0.6*X[0]) - 0.843750000000000*cos(0.750*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 7.2*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*cos(0.6*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) - 1.29*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*(3.6*X[1]*cos(0.6*X[0]) - 1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))*sin(0.300*X[1])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 + 31.9200000000000*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*sin(0.6*X[0])*cos(0.700*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 - (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 26.4450000000000*sin(0.300*X[1])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*(3.6*X[1]*cos(0.6*X[0]) - 1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 12.0*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 54.5300000000000*cos(0.700*X[0])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*sin(0.6*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 6.0*(-1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))*X[1]*sin(0.6*X[0]) - 6.00*(1.50*sin(0.750*X[1]) + 10.0*cos(0.6*X[0]) + 1.50*cos(0.750*X[1]) + 5.00)*sin(0.6*X[0]) + X[1]*cos(X[0]*X[1]/pi)/pi - 261.629508970000*sin(1.30*X[0]*X[1]/pi) + 127.279220580000*sin(1.70*X[0]) + 0.843750000000000*sin(0.750*X[1]) + 3.60*cos(0.6*X[0]) + cos(X[0]) + 0.843750000000000*cos(0.750*X[1]) + 91.9238815300000*cos(2.10*X[1]) - 367.695526120000

def forcing_v(X):
    return 2.16*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*X[1]*sin(0.6*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 0.0247500000000000*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*(3.6*X[1]*cos(0.6*X[0]) - 1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 0.297*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)*sin(0.6*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) - 2*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)*(3.6*X[1]*cos(0.6*X[0]) - 1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) - 24.0*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)*sin(0.6*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) - 2.66*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*(3.6*X[1]*cos(0.6*X[0]) - 1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))*cos(0.700*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 - 15.4800000000000*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*sin(0.6*X[0])*sin(0.300*X[1])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 - 12.0*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 26.4450000000000*sin(0.300*X[1])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*sin(0.6*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) - (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 54.5300000000000*cos(0.700*X[0])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*(3.6*X[1]*cos(0.6*X[0]) - 1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 3.6*(1.50*sin(0.750*X[1]) + 10.0*cos(0.6*X[0]) + 1.50*cos(0.750*X[1]) + 5.00)*X[1]*cos(0.6*X[0]) + 36.0*X[1]*sin(0.6*X[0])**2 + 2.16*X[1]*sin(0.6*X[0]) + X[0]*cos(X[0]*X[1]/pi)/pi - 261.629508970000*sin(1.30*X[0]*X[1]/pi) + 127.279220580000*sin(1.70*X[0]) - sin(X[1]) + 91.9238815300000*cos(2.10*X[1]) - 367.69552612

def forcing_rho(X):
    return -78.0*(-37.0*X[0]*cos(1.30*X[0]*X[1]/pi)/pi - 21.0*sin(2.10*X[1]))*X[1]*sin(0.6*X[0]) - ((-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 1.00)*(-625.300000000000*X[0]**2*sin(1.30*X[0]*X[1]/pi)/pi**2 - 625.300000000000*X[1]**2*sin(1.30*X[0]*X[1]/pi)/pi**2 + 520.200000000000*sin(1.70*X[0]) + 573.300000000000*cos(2.10*X[1])) + (481.*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 306.*cos(1.70*X[0]))*(1.50*sin(0.750*X[1]) + 10.0*cos(0.6*X[0]) + 1.50*cos(0.750*X[1]) + 5.00) - (481.*X[1]*cos(1.30*X[0]*X[1]/pi)/pi - 306.*cos(1.70*X[0]))*(-0.0247500000000000*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 2*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 2.66*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*cos(0.700*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 + (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 54.5300000000000*cos(0.700*X[0])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)) + 13*(-37.0*X[0]*cos(1.30*X[0]*X[1]/pi)/pi - 21.0*sin(2.10*X[1]))*(-0.0247500000000000*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 2*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 1.29*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*sin(0.300*X[1])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 + (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 26.4450000000000*sin(0.300*X[1])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2))

def forcing_ke(X):
    return (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*(340.118361661000*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 340.118361661000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi + 193.040151213000*sin(2.10*X[1]) - 216.374674986000*cos(1.70*X[0]))/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) - (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*(12.96*X[1]**2*cos(0.6*X[0])**2 + 7.2*(-1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))*X[1]*cos(0.6*X[0]) + (-1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))**2 + 144.0*sin(0.6*X[0])**2)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 6.0*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*X[1]*sin(0.6*X[0]) - ((-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 1.00)*(-0.256*X[0]**2*cos(0.800*X[0]*X[1]/pi)/pi**2 - 0.256*X[1]**2*cos(0.800*X[0]*X[1]/pi)/pi**2 - 0.294*sin(0.700*X[1]) - 0.324*cos(0.600*X[0])) + (-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(1.50*sin(0.750*X[1]) + 10.0*cos(0.6*X[0]) + 1.50*cos(0.750*X[1]) + 5.00) - (-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(-0.0247500000000000*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 2*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 2.66*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*cos(0.700*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 + (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 54.5300000000000*cos(0.700*X[0])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)) - (-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(-0.0247500000000000*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 2*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 1.29*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*sin(0.300*X[1])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 + (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 26.4450000000000*sin(0.300*X[1])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)) - 3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2

def forcing_eps(X):
    return (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.000125*(1/((-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)))**3.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)*(340.118361661000*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 340.118361661000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi + 193.040151213000*sin(2.10*X[1]) - 216.374674986000*cos(1.70*X[0]))*tanh((4.242640686*X[1]*sin(0.6*X[0]) + 1.06066017150000*sin(0.750*X[1]) + 7.07106781000000*cos(0.6*X[0]) + 1.06066017150000*cos(0.750*X[1]) + 3.53553390500000)/((1.50*sin(0.750*X[1]) + 10.0*cos(0.6*X[0]) + 1.50*cos(0.750*X[1]) + 5.00)**2.00 - (4.242640686*X[1]*sin(0.6*X[0]) + 1.06066017150000*sin(0.750*X[1]) + 7.07106781000000*cos(0.6*X[0]) + 1.06066017150000*cos(0.750*X[1]) + 3.53553390500000)**2.00 + 36.0*(X[1]*sin(0.6*X[0]))**2.00)**0.500) - (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.000125*(1/((-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)))**3.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)*(12.96*X[1]**2*cos(0.6*X[0])**2 + 7.2*(-1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))*X[1]*cos(0.6*X[0]) + (-1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))**2 + 144.0*sin(0.6*X[0])**2) - 7.74*X[1]*sin(0.6*X[0])*sin(0.300*X[1]) - (e**(-((0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2))**2.00) - 1.00)*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00) - ((-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 1.00)*(1.86200000000000*sin(0.700*X[0]) - 0.387*cos(0.300*X[1])) - 2.66*(1.50*sin(0.750*X[1]) + 10.0*cos(0.6*X[0]) + 1.50*cos(0.750*X[1]) + 5.00)*cos(0.700*X[0]) + 1.29*(-0.0247500000000000*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 2*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 1.29*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*sin(0.300*X[1])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 + (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[0]*sin(0.800*X[0]*X[1]/pi)/pi + 0.420*cos(0.700*X[1]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 26.4450000000000*sin(0.300*X[1])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2))*sin(0.300*X[1]) + 2.66*(-0.0247500000000000*(e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) - 1)*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**1.50*e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 2*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2) + 2.66*(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*cos(0.700*X[0])/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2 + (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(-41.0*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)*(-0.320*X[1]*sin(0.800*X[0]*X[1]/pi)/pi - 0.540*sin(0.600*X[0]))/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**3.00 - 54.5300000000000*cos(0.700*X[0])/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2))*cos(0.700*X[0])

def P_ke(X):
    return (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*(12.96*X[1]**2*cos(0.6*X[0])**2 + 7.2*(-1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))*X[1]*cos(0.6*X[0]) + (-1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))**2 + 144.0*sin(0.6*X[0])**2)/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)

def P_eps(X):
    return (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.000125*(1/((-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)))**3.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)*(12.96*X[1]**2*cos(0.6*X[0])**2 + 7.2*(-1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))*X[1]*cos(0.6*X[0]) + (-1.12500000000000*sin(0.750*X[1]) + 1.12500000000000*cos(0.750*X[1]))**2 + 144.0*sin(0.6*X[0])**2)

def A_ke(X):
    return 3.80*sin(0.700*X[0]) - 4.30*cos(0.300*X[1]) - 13.2

def A_eps(X):
    return -(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2.00/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)

def B_ke(X):
    return -(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2*(340.118361661000*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 340.118361661000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi + 193.040151213000*sin(2.10*X[1]) - 216.374674986000*cos(1.70*X[0]))/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)

def B_eps(X):
    return -(-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.000125*(1/((-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)))**3.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)*(340.118361661000*X[0]*cos(1.30*X[0]*X[1]/pi)/pi + 340.118361661000*X[1]*cos(1.30*X[0]*X[1]/pi)/pi + 193.040151213000*sin(2.10*X[1]) - 216.374674986000*cos(1.70*X[0]))*tanh((4.242640686*X[1]*sin(0.6*X[0]) + 1.06066017150000*sin(0.750*X[1]) + 7.07106781000000*cos(0.6*X[0]) + 1.06066017150000*cos(0.750*X[1]) + 3.53553390500000)/((1.50*sin(0.750*X[1]) + 10.0*cos(0.6*X[0]) + 1.50*cos(0.750*X[1]) + 5.00)**2.00 - (4.242640686*X[1]*sin(0.6*X[0]) + 1.06066017150000*sin(0.750*X[1]) + 7.07106781000000*cos(0.6*X[0]) + 1.06066017150000*cos(0.750*X[1]) + 3.53553390500000)**2.00 + 36.0*(X[1]*sin(0.6*X[0]))**2.00)**0.500)

def EV(X):
    return (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)

def velocity(X):
    return [u(X), v(X)]

def forcing_velocity(X):
    return [forcing_u(X), forcing_v(X)]

def A_ke(X):
    return 3.80*sin(0.700*X[0]) - 4.30*cos(0.300*X[1]) - 13.2

def A_eps(X):
    return (e**(-((0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2))**2.00) - 1.00)*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)**2/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)

def d_eps(X):
    return -1.29*sin(0.300*X[1])

def f_1(X):
    return 0.000125*(1/((-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)))**3.00 + 1.00

def f_2(X):
    return -e**(-((0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00/(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2))**2.00) + 1.00

def f_mu(X):
    return (-e**(-0.0247500000000000*(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**0.500) + 1)**2.00*(20.5*(-3.80*sin(0.700*X[0]) + 4.30*cos(0.300*X[1]) + 13.2)/(0.600*sin(0.700*X[1]) + 0.400*cos(0.800*X[0]*X[1]/pi) + 0.900*cos(0.600*X[0]) + 1.00)**2.00 + 1.00)

def Y(X):
    return 1.50
