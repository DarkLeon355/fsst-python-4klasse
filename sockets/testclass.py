

class myclass:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.l = [a, n]
    def info(self):
        print(f"{self.a}, {self.n}, {self.l}")