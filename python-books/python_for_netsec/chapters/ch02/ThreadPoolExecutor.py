from concurrent.futures import ThreadPoolExecutor, as_completed
from random import randint
import threading

def execute(name):
    value = randint(0, 1000)
    thread_name = threading.current_thread().name
    print(f'I am {thread_name} and my value is {value}')