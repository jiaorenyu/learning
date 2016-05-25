#include "test.h"

#include <stdio.h>

#include <iostream>
#include <fstream>

using namespace std;



JsonTest::JsonTest() {
}

JsonTest::JsonTest(const string &path) {
	this->path = path;
}


bool JsonTest::json_load() {
	return true;
}



int main() {
	std::ifstream t("test.json");  
	std::string str((std::istreambuf_iterator<char>(t)),  
			                 std::istreambuf_iterator<char>()); 

	Json::Reader reader;

	Json::Value value;

	if (reader.parse(str, value))
	{
		Json::Value root=value;

//printf("%s \n",root.toStyledString().c_str());

		Json::Value order = root["order"];
		Json::Value spots = order["2856"]["campaigns"]["458"]["spots"];
		Json::Value impTime = spots["8600"]["impTime"];

		for (int i=0; i<impTime.size(); ++i) {
			cout << impTime[i] << endl;
		}

		for (Json::Value::iterator it =	impTime.begin(); it!=impTime.end(); ++it) {
			cout << (*it).asString() << endl;
		}

	} else {
		cout << "error" << endl;
	}
	return 0;
}
