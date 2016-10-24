#include <stdio.h>
#include <limits.h>

#include "test1.h"
#include "test.h"

void test1(char *value) {
	value = (char *) calloc(10, 1);
}

#define TMP "Hello %s!"

int main() 
{	
	char tmp[100];
	sprintf(tmp, TMP);
	printf("%s", tmp);
	return 0;
}
