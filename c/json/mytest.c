#include "cJSON.h"
#include <stdio.h>

int main() {
	cJSON *root;
	
	root = cJSON_CreateObject();

	cJSON *js_body;

	cJSON_AddItemToObject(root, "body", js_body=cJSON_CreateObject());
	cJSON_AddStringToObject(js_body, "name", "jiaorenyu");
	cJSON_AddNumberToObject(js_body, "value", 600);
	
	char *s = cJSON_PrintUnformatted(root);

	cJSON_Delete(root);
	printf("%s", s);


	return 0;
}
