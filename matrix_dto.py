from dataclasses import dataclass
from typing import List

@dataclass
class MatrixVectorMultiplicationTask:
    matrix_slice: List[List[float]]
    vector: List[List[float]]
    order: int
    
