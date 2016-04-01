#!/usr/bin/python3

import threading
import time

import logging


def worker_1():
    print "worker_1"
def worker_2():
    print "worker_2"
    while True:
        print "worker_2"
        time.sleep(5)


if __name__ == "__main__":
    worker1 = threading.Thread(target=worker_1)
    worker2 = threading.Thread(target=worker_2)
    worker1.setDaemon(True)
    worker2.setDaemon(True)
    worker1.name = "worker1"
    worker2.name = "worker2"
    worker1.start()
    worker2.start()

    print("main finish")
