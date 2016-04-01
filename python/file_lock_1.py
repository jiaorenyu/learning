#!/usr/bin/python

import time
from common_util import fcntl_lock

@fcntl_lock("/tmp/test.lock")
def test():
    time.sleep(10)


if __name__ == "__main__":
    print("first")
    test()
