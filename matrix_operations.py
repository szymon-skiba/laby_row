import math, sys, time

class MatrixReader:
    @staticmethod
    def read(fname):
        with open(fname, "r") as f:
            nr = int(f.readline())
            nc = int(f.readline())

            A = [[0] * nc for _ in range(nr)]
            r = 0
            c = 0
            for _ in range(nr * nc):
                A[r][c] = float(f.readline())
                c += 1
                if c == nc:
                    c = 0
                    r += 1

        return A

class MatrixMultiplier:
    @staticmethod
    def multiply(A, X):
        nrows = len(A)
        ncols = len(A[0])
        y = []
        for i in range(nrows):
            s = 0
            for c in range(ncols):
                s += A[i][c] * X[c][0]
                # time.sleep(0.1)
            y.append(s)
        return y
