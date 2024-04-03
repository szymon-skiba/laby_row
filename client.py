import sys
from multiprocessing.managers import BaseManager
from matrix_operations import MatrixReader
from matrix_dto import MatrixVectorMultiplicationTask 

class QueueManager(BaseManager): pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

def connect_to_server():
    m = QueueManager(address=('localhost', 50000), authkey=b'abc')
    m.connect()
    return m

def divide_matrix(matrix, num_splits):
    split_size = len(matrix) // num_splits
    return [matrix[i:i + split_size] for i in range(0, len(matrix), split_size)]

def client(matrix, vector, num_tasks):
    manager = connect_to_server()
    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()

    matrix_parts = divide_matrix(matrix, num_tasks)
    for order, part in enumerate(matrix_parts):
        task = MatrixVectorMultiplicationTask(matrix_slice=part, vector=vector, order=order)
        task_queue.put(task)

    final_result = [None] * num_tasks
    for _ in range(num_tasks):
        order, partial_result = result_queue.get()
        final_result[order] = partial_result

    final_result = [item for sublist in final_result for item in sublist] if final_result[0] is not None else final_result
    print("Final result:", final_result)

if __name__ == '__main__':

    num_tasks = 3
    fnameA = "A2.dat"
    fnameX = "X2.dat"
    matrix = MatrixReader.read(fnameA)
    vector = MatrixReader.read(fnameX)

    if not isinstance(vector[0], list):
        vector = [[x] for x in vector] 

    client(matrix, vector, num_tasks)
