#include <iostream>
#include <string>

#include <stdio.h>
#include <ctype.h>
#include <string.h>

#include <sstream>

using namespace std;

int main() {
	int deal_id_int = 975;
	stringstream ss;
	ss << deal_id_int;
	string deal_id = ss.str();
	
	cout << deal_id << endl;
	return 0;
}
