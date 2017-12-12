import numpy
import sys
from numpy.linalg import solve,inv
import io

def adjustResponseFactor(file_content, degree = 9):

    lines = file_content.split("\n")
    lines = numpy.array(lines)
    
    Z = numpy.array([])
    Y = numpy.array([])
    Yerror = numpy.array([])
    for line in range(0,len(lines)-1):
        current_line = lines[line].split(',')
        Z = numpy.append(Z,float(current_line[0]))
        Y = numpy.append(Y,float(current_line[1]))
        Yerror = numpy.append(Yerror,float(current_line[2]))
    
    # Matrix X, each colunm like [1 z z^2 z^3 ... z^n] ...
    X = numpy.vstack([Z**j for j in range(degree)]).T

    # Variance of Y
    VY = numpy.zeros((len(Y),len(Y)),float)
    numpy.fill_diagonal(VY,Yerror**2)


    # Variance of A 
    VA = inv(numpy.dot(numpy.dot(X.T,inv(VY)),X)) 

    # Coefficients
    A = numpy.dot(numpy.dot(numpy.dot(VA,X.T),inv(VY)),Y)

    # square root of VA diagonal gives the A errors
    coefficients_errors = numpy.sqrt(numpy.diagonal(VA))

    # atomic numbers
    Zadjusted = numpy.array(range(11,43)) 

    # Response Factor adjusted
    Xadjusted = numpy.vstack([Zadjusted**j for j in range(degree)]).T
    Yadjusted = numpy.dot(Xadjusted,A)

    # covariance matrix of Yadjusted (CYadjusted)
    CYadjusted = numpy.dot(numpy.dot(Xadjusted,VA),Xadjusted.T)

    # error
    YadjustedError =  numpy.sqrt(numpy.diagonal(CYadjusted))

    # return
    s = io.BytesIO()
    response_factor_numpy = numpy.vstack((Zadjusted.astype(int),Yadjusted,YadjustedError)).T
    numpy.savetxt(s,response_factor_numpy,delimiter=",")
    numpy.savetxt('/tmp/teste.csv',response_factor_numpy,delimiter=",")
    response_factor = s.getvalue()
    
    return({'response_factor': response_factor, 'coefficients': A, 'coefficients_errors': coefficients_errors})


