import numpy
import random

def exp3(n,M,m,l,V_0,sigma):
    g = 9.8
    temp = (1-(1/(2*g*l))*numpy.power((V_0*m)/(M+m),2))
    alpha_0 = numpy.arccos(temp)
    alpha = [random.uniform(alpha_0-sigma*alpha_0, alpha_0+sigma*alpha_0) for x in range(n)]
    V = ((M+m)/m)*numpy.sqrt(2*g*l*(1-numpy.cos(alpha)))
    return [numpy.average(V), numpy.std(V), alpha_0]

print(exp3(100,  1000, 0.01, 2, 800, 0.05))