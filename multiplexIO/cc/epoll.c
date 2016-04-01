#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#include <sys/types.h>
#include <sys/stat.h>
#include <sys/epoll.h>

#define MAX_EVENTS 64

void register_fd(int epfd, int fd, uint32_t e) {
	struct epoll_event event;
	event.data.fd = fd;
	event.events = e;
	
	int ret = epoll_ctl(epfd, EPOLL_CTL_ADD, fd, &event);
	if (ret)
		perror("epoll_ctl");
}

int main(){
	int epfd, ret, fd;
	struct epoll_event event;
	struct epoll_event *events;
	int nr_events, i;
	
	epfd = epoll_create1(0);
	if (epfd < 0)
		perror("epoll_create1");
	fd = open("doc", O_RDWR);
//	register_fd(epfd, STDIN_FILENO, EPOLLIN);
	register_fd(epfd, STDIN_FILENO, EPOLLIN|EPOLLET);

	events = malloc(sizeof(struct epoll_event)*MAX_EVENTS);
	if (!events) {
		perror("malloc");
		return 1;
	}

	while(1) {
		nr_events = epoll_wait(epfd, events, MAX_EVENTS, -1);
		if(nr_events < 0) {
			perror("epoll_wait");
			free(events);
			return 1;
		}

		char buf[100];
		for (i=0; i<nr_events;i++) {
			if (events[i].data.fd == STDIN_FILENO) {
				printf("Hello World!\n");
			}

		}
	}
	free(events);

	return 0;
}
