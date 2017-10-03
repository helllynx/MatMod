import numpy
import random

def exp2(n,M,m,l,V_0,sigma):
    g = 9.8
    temp = (1-(m*numpy.power(V_0,2))/(2*g*l*(M+m)))
    alpha_0 = numpy.arccos(temp)
    alpha = [random.uniform(alpha_0-sigma*alpha_0, alpha_0+sigma*alpha_0) for x in range(n)]
    V = numpy.sqrt(2*(M+m)*g*l*(1-numpy.cos(alpha))/m)
    return [numpy.average(V), numpy.std(V), alpha_0]

print(exp2(100,  1000, 0.01, 2, 800, 0.05))