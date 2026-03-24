import math 

class Integracion:
    def __init__(self, error_aceptable=0.00001):
        self.error_aceptable = error_aceptable

    def gamma(self, x):
        if x == 1: return 1
        if x == 0.5: return math.sqrt(math.pi)
        if x % 1 == 0: return math.factorial(int(x) - 1)
        resol, act = 1, x - 1
        while act > 0:
            resol *= act
            act -= 1
        return resol * math.sqrt(math.pi)

    def doff(self, x, dof):
        c = (self.gamma((dof + 1) / 2))/math.sqrt(dof * math.pi) * self.gamma(dof / 2)
        return c * (1 + (x**2 / dof))**(-(dof + 1) / 2)

    def calcular_area(self, x, dof, num_seg):
        w = x / num_seg
        suma = self.doff(0, dof) + self.doff(x, dof)
        for i in range(1, num_seg):
            mult = 4 if i % 2 != 0 else 2
            suma += mult * self.f(i * w, dof)
        return (w / 3) * suma

    def integrar(self, x, dof):
        num_seg = 10
        area_ant = self.calcular_area(x, dof, num_seg)
        while True:
            num_seg *= 2
            area_nueva = self.calcular_area(x, dof, num_seg)
            if abs(area_ant - area_nueva) < self.error_aceptable:
                return round(area_nueva, 5)
            area_ant = area_nueva