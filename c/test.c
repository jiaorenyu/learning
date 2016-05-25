#include <stdio.h>
#include <limits.h>

#define ERROR_LOG(module) fprintf(stderr, "error: "#module"\n");

#define PRINT1()	\
{	\
	printf("a\n");\
	printf("b\n");\
}


#define PRINT2()	\
do \
{	\
	printf("a\n");\
	printf("b\n");\
}while(0)

#define PRINT(a) \
	do { \
		printf("%s: %d\n", #a, a); \
		printf("%s: %d\n", #a, a); \
	}while(0)


int main() 
{
	int a = 0;
	int b = 1;
	printf("%f\n", INT_MIN*1.0);
	printf("%f\n", INT_MIN+0.000000001);

	return 0;
}
