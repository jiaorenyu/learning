#include <stdio.h>

#include "hiredis/hiredis.h"

int main() {
	redisContext *c = redisConnect("127.0.0.1", 6379);
	if (c==NULL || c->err) {
		if(c) {
			printf("Error: %s\n", c->errstr);
		} else {
			printf(" can't allocate redis context\n");
		}
	}
	
	redisReply *reply;
	reply = redisCommand(c, "set a %d", 10); 
	freeReplyObject(reply);
	reply = redisCommand(c, "get a"); 
	
	printf(" value: %s", reply->str);
	freeReplyObject(reply);

	return 0;
}
