from multiprocessing.managers import BaseManager
from queue import Queue

class QueueManager(BaseManager): pass

def start_server():
    task_queue = Queue()
    result_queue = Queue()

    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)

    manager = QueueManager(address=('', 50000), authkey=b'abc')
    server = manager.get_server()
    print("Server is starting...")
    server.serve_forever()

if __name__ == '__main__':
    start_server()
