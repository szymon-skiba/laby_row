import numpy as np
import sys

def generate_and_save_matrix(rows, cols, filename):
    matrix = np.random.uniform(-100, 101, size=(rows, cols))
    
    with open(filename, 'w') as f:
        f.write(f"{rows}\n")
        f.write(f"{cols}\n")
        for row in matrix:
            for element in row:
                f.write(f"{element}\n")

def generate_and_save_vector(size, filename):
    vector = np.random.uniform(1, 11, size=(size, 1))
    
    with open(filename, 'w') as f:
        f.write(f"{size}\n")
        f.write(f"{1}\n")
        for element in vector:
            f.write(f"{element[0]}\n")

def run_gen(rows, cols, matrix_filename, vector_filename):
    generate_and_save_matrix(rows, cols, matrix_filename)
    generate_and_save_vector(cols, vector_filename) 