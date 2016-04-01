#!/usr/bin/python

import select
import sys

if __name__ == "__main__":
	ep = select.epoll()
#	ep.register(sys.stdin, select.EPOLLIN)
	ep.register(sys.stdin, select.EPOLLIN|select.EPOLLET)
	while True:
		result = ep.poll()
		for fd,events in result:
			if events == select.EPOLLIN:
				print("EPOLLIN")
