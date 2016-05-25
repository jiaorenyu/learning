#!/usr/bin/python3
import time
from concurrent.futures import ThreadPoolExecutor

def test(sec):
    time.sleep(sec)
    return "hello"

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(test, 3)
        while not future.done():
            print("running")
            time.sleep(1)
        print(future.result())
    
