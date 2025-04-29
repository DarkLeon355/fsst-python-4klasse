import math

class triangle():
    def __init__(self, a, b, c = None):
        self.a = a
        self.b = b
        self.c = c
        if not self.c:
            self.c = math.sqrt(self.a ** 2 + self.b ** 2)
        self.angles()
        self.circumference = self.circumference()
        self.area = self.area()


    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def circumference(self):
        return self.a + self.b + self.c

    def angles(self):
        self.gamma = 90
        self.alpha = math.degrees(math.asin(self.a/self.c))
        self.beta = 180 - self.alpha - self.gamma
        
    
    def __str__(self):
        return f"Triangle with sides a = {self.a}, b = {self.b}, c = {self.c}, angles alpha = {self.alpha}, beta = {self.beta}, gamma = {self.gamma} an area of {self.area} and a circumference of {self.circumference}"
