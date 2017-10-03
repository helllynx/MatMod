import numpy
import random

def exp1(n,h,M,V_0,sigma):
    """
    :param n: number of experiments
    :param h: height of the stand of the gun
    :param M: mathematical expectation
    :param V_0: starting speed
    :param sigma: dispersion in percent
    :return: average speed and standard deviation
    """
    g = 9.8
    L_0 = numpy.sqrt((numpy.power(V_0,2)*h*2)/g)
    L = [random.uniform(L_0-L_0*sigma, L_0+L_0*sigma) for x in range(n)]
    V = numpy.sqrt((numpy.float_power(L, 2)*g)/(h*2))
    return [numpy.average(V), numpy.std(V), L_0]


print(exp1(100, 1, 360, 800, 0.05))