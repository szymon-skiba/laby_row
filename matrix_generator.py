import numpy as np
import sys

def generate_and_save_matrix(rows, cols, filename):
    matrix = np.random.randint(-100, 101, size=(rows, cols))
    
    with open(filename, 'w') as f:
        f.write(f"{rows}\n")
        f.write(f"{cols}\n")
        for row in matrix:
            for element in row:
                f.write(f"{element}\n")

def generate_and_save_vector(size, filename):
    vector = np.random.randint(1, 11, size=(size, 1))
    
    with open(filename, 'w') as f:
        f.write(f"{size}\n")
        for element in vector:
            f.write(f"{element[0]}\n")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py rows cols matrix_filename vector_filename")
        sys.exit(1)
    
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    matrix_filename = sys.argv[3]
    vector_filename = sys.argv[4]

    generate_and_save_matrix(rows, cols, matrix_filename)
    generate_and_save_vector(cols, vector_filename) 