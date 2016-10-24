#include <stdio.h>
#include <limits.h>

int main() 
{		
	int a = 10;
	switch(a){
		case 10: printf("10\n"); 
		case 11: printf("11\n");
		default: printf("default\n");
	}
	return 0;
}
