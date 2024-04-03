import sys
from multiprocessing import Process, current_process
from multiprocessing.managers import BaseManager
from matrix_operations import MatrixMultiplier 
from matrix_dto import MatrixVectorMultiplicationTask

class QueueManager(BaseManager): pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

def connect_to_server():
    m = QueueManager(address=('localhost', 50000), authkey=b'abc')
    m.connect()
    return m

def calculate_product(task):

    matrix_slice = task.matrix_slice
    vector = task.vector
    order = task.order
    
    print(f"Process {current_process().name} has started a task {order}.")

    # Use the unpacked matrix slice and vector for multiplication
    result = MatrixMultiplier.multiply(matrix_slice, vector)
    
    print(f"Process {current_process().name} has completed a task.")
    
    # Return both the result and the order for proper result assembly
    return (order, result)

def worker():
    manager = connect_to_server()
    task_queue = manager.get_task_queue()
    result_queue = manager.get_result_queue()

    while True:
        task = task_queue.get()
        if task is None:
            task_queue.put(None)  
            break
        result = calculate_product(task)
        result_queue.put(result)

if __name__ == '__main__':
    num_workers = 100  # Default number of worker processes
    if len(sys.argv) > 1:
        try:
            num_workers = int(sys.argv[1])  # Allow dynamic setting of the number of workers
        except ValueError:
            print("Usage: python worker_program.py [num_workers]")
            sys.exit(1)

    worker_processes = [Process(target=worker) for _ in range(num_workers)]
    for p in worker_processes:
        p.start()
    for p in worker_processes:
        p.join()
