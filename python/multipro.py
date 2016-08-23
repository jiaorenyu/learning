from multiprocessing import Process

import time

def f(name):
    time.sleep(5)
    print('hello')

if __name__ == '__main__':
    p = Process(target=f, args=('jiaorenyu',))
    p1 = Process(target=f, args=('jiaorenyu',))
    p.start()
    p1.start()
    p1.join()
    p.join()
