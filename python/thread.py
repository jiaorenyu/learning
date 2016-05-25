#!/usr/bin/python3

import threading
import time

import logging

logger = logging.getLogger()
log_path = "logs/thread.log"
logging.basicConfig(level=logging.DEBUG, format="mt=%(asctime)s^msg=%(message)s", datefmt="%Y%m%d-%H:%M:%S", filename=log_path)

def worker_1(msg):
    time.sleep(2)
    logger.info("worker_1")
    logger.info(msg)
    
def worker_2():
    logger.info("worker_2")
    while True:
        logger.info("worker_2")
        time.sleep(1)


if __name__ == "__main__":
    worker1 = threading.Thread(target=worker_1("hello"))
    worker2 = threading.Thread(target=worker_2)
    worker1.setDaemon(True)
    worker2.setDaemon(True)
    worker1.name = "worker1"
    worker2.name = "worker2"
    worker1.start()
    worker2.start()
    worker1.join()

    print("main finish")
