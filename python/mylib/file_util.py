#!/usr/bin/python

import fcntl
import logging


def fcntl_lock(lock):
    def dec(func):
        def new_func(*arg, **kws):
            fp = open(lock, "w")
            try:
                fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError as e:
                logging.warning("{0} is already running.\nmessage: ".format(func, e))
                exit(1)
            func(*arg, **kws)
        return new_func
    return dec

def get_set(fn):
    ids = set()
    fp = open(fn, "r")
    for line in fp:
        line.strip()
        ids.add(line)
    fp.close()

    return ids

