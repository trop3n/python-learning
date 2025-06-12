import multiprocessing
import logging
import time

logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s] - %(threadName)-10s : %(message)s')
def thread(name):
    logging.debug('Starting Process ' + name)
    time.sleep(5)
    print("%s: %s" % (name, time.ctime(time.time())))
    logging.debug('Stopping Process '+ name)
def check_state(process):
    if process.is_alive():
        print(f'Process {process.name} is alive.')
    else:
        print(f'Process {process.name} is not alive.')