import numpy as np

class LN():

    # x = points
    # grade = grau da regressao
    @staticmethod
    def matrixA(x,grade):
        m = grade
        if m < 1:
            return False
        a = np.zeros([len(x),grade+1])
        power = np.ones([grade+1, len(x)])
        i = 0
        for m in range(grade, 0, -1):
            power[i] = x**m
            i += 1
        return power.T

    @staticmethod
    def getStraightPoints(): 
        a = [[-11.8641761,11.07774611],[ -8.35057905,5.52953481],[ -5.42371688,-0.36535486],[ -1.07914586,-5.74814041],[  1.80143787,-13.15684397],[  5.16456358,-16.28595922],[  0.0666563,-10.20591306],[ -2.79651765,-4.09899559],[ -6.94007135,2.80478077],[ -9.68200684,7.56668553]]
        return a