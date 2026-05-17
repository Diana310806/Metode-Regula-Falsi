from .calculate_error import ErrorCalculator

class RegulaFalsi:
    def __init__(self, func, a, b, tol=0.0001, max_iter=100):
        self.func = func
        self.a = a
        self.b = b
        self.tol = tol
        self.max_iter = max_iter
        self.iterations = []

    def hitung_titik(self, a, b):
        fa = self.func(a)
        fb = self.func(b)
        return b - (fb * (b - a)) / (fb - fa)

    def solve(self):
        a, b = self.a, self.b
        prev_c = None

        for i in range(self.max_iter):
            c = self.hitung_titik(a, b)
            fa = self.func(a)
            fc = self.func(c)

            error = ErrorCalculator.relative_error(c, prev_c)

            self.iterations.append({
                "iterasi": i + 1,
                "a": a,
                "b": b,
                "c": c,
                "fc": fc,
                "error": error
            })

            if abs(fc) < self.tol:
                return c

            if fa * fc < 0:
                b = c
            else:
                a = c

            prev_c = c

        return c
    def get_iterations(self):
        return self.iterations