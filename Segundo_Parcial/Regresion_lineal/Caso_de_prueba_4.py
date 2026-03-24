import numpy as np

class CasoPrueba4():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.xk = 0
        self.xavg = 0
        self.yavg = 0
        self.n = 0

    def leerDatos(self):
        self.x = [163,765,141,166,137,355,136,1206,433,1130]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]
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