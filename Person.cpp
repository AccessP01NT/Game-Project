#include "Person.h"
#include <string>
#include <iostream>
using namespace std;


Person::Person()
{
	cin >> name;
	while (name.length() > 10) {
		cout << "Enter name again less than 10 letters:" << endl;
		cin >> this->name;
	}
	this->name = name;
	this->age = age;
	this->id = id;
}

Person::Person(string name, int age, long id):name(name), age(age), id(id)
{
	while (this->name.length() > 10) {
		cout << "Enter name again less than 10 letters:" << endl;
		cin >> this->name;
	}
}

void Person::DetailsPerson()
{
	cout << "Name:" << this->name << endl;
	cout << "age:" << this->age << endl;
	cout << "id:" << this->id << endl;

}


Person::~Person()
{
}
