#include <stdio.h>
#include <limits.h>

#include "test1.h"
#include "test.h"

void test1(char *value) {
	value = (char *) calloc(10, 1);
}


int main() 
{	
	char *value;
	test1(value);
	free(value);
	return 0;
}
