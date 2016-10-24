#include <time.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <string.h>

int trig_file(const char *filename) {
	return 1;
	struct stat cur_stat;

	stat(filename, &cur_stat);

	if (cur_stat.st_mtime != 0) {
		return 1;
	} else {
		return 0;
	}
}

int main() {
	char value[3] = {'\0'};
	printf("%s\n", value);
	return 0;
}
