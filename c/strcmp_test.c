#include <stdio.h>
#include <string.h>

int main(void)
{
	char* s1="mobile";
	char* s2="Mobile";

	int result = strcmp(s1,s2);
	printf("Result: %d", result);

	return 0;
}
