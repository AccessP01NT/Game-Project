#include <string.h>
#include <iostream>
using namespace std;
class Person
{
private:
	string name;
	int age;
	long id;
public:
	Person();
	Person(string, int, long);
	virtual void DetailsPerson();
	~Person();
};

