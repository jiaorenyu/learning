#include <iostream>
#include <string>

using namespace std;


int main() {
	cout << "Hello World!" << endl;
	string test = "12334";
	cout << test << endl;
	test = "uuid:"+test;

	cout << test << endl;
	return 0;
}
