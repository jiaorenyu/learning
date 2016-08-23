#include "test1.h"
#include "test.h"


int test() 
{	
	data *mytest;
	mytest = (data *)calloc(1, sizeof(data));

	mytest->a = 10;
	
	printf("%d", mytest->a);

	free(mytest);

	return 0;
}
