#ifndef _TEST_H_
#define _TEST_H_

#include "json/json.h"

using namespace std;

class JsonTest {
public:
	string path;
	
	JsonTest();
	JsonTest(const string &path);
	bool json_load();
};

#endif
