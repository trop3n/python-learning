import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] - %(threadName)-10s : %(message)s')
def thread(name):
    logging.debug('Starting Thread '+ name)
    time.sleep(5)
    print("%s: %s" % (name, time.ctime(time.time())))
    logging.debug('Stopping Thread '+ name)
def check_state(thread):
    if thread.is_alive():
        print(f'Thread {thread.name} is alive.')
    else:
        print(f'Thread {thread.name} is not alive.')