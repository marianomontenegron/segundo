import math 

class Integracion:
    def __init__(self, dof, x, error_aceptable=0.00001):
        self.error_aceptable = error_aceptable
        self.dof = dof
        self.x = x
        self.gamma = 0
        self.f_X = 0
        

    def gamma(self):
        if self.x == 1: return 1
        if self.x == 0.5: return math.sqrt(math.pi)
        if self.x % 1 == 0: return math.factorial(int(self.x) - 1)
        resol, act = 1, self.x - 1
        while act > 0:
            resol *= act
            act -= 1
        gamma = resol * math.sqrt(math.pi)
        return gamma

    def f_X(self):
        self.f_X = ((self.gamma((self.dof + 1) / 2))/math.sqrt(self.dof * math.pi) * self.gamma(self.dof / 2))*(1 + (self.x**2 / self.dof))**(-(self.dof + 1) / 2)
        return self.f_X 

    def calcular_area(self, num_seg):
        w = self.x / num_seg
        suma = self.f_X(0, self.dof) + self.f_X(self.x, self.dof)
        for i in range(1, num_seg):
            mult = 4 if i % 2 != 0 else 2
            suma += mult * self.f_X(i * w, self.dof)
        return (w / 3) * suma

    def integrar(self):
        num_seg = 10
        area_ant = self.calcular_area(self.x, self.dof, num_seg)
        while True:
            num_seg *= 2
            area_nueva = self.calcular_area(self.x, self.dof, num_seg)
            if abs(area_ant - area_nueva) < self.error_aceptable:
                return round(area_nueva, 5)
            area_ant = area_nueva