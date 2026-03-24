import numpy as np

class CasoPrueba1():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.xk = 0
        self.xavg = 0
        self.yavg = 0
        self.n = 0

    def leerDatos(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]
        self.xk = 386
        self.xavg = np.average(self.x)
        self.yavg = np.average(self.y)
        self.n = len(self.x)

    def RealizarCalculo(self):

        B1 = ((sum(self.x)*sum(self.y))-(self.n*self.xavg*self.yavg))/((sum(np.pow(self.x,2)))-(self.n*(self.xavg**2)))
        B0 = self.yavg - B1
        rxy = (self.n*(sum(self.x)*sum(self.y))-(sum(self.x)*sum(self.y)))/((self.n*(sum(np.pow(self.x,2)))-(sum(self.x)**2))*((self.n*sum(np.pow(self.y,2)))-(sum(self.y)**2)))**(1/2)
        r2 = rxy*rxy
        Yk = B0+B1*self.xk