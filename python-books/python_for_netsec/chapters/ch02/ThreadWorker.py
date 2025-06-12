import threading
class ThreadWorker(threading.thread):
    def __init__(self):
        super(ThreadWorker, self).__init__()
    def run(self):
        for i in range(10):
            print(i)