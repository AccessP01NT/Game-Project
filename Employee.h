#pragma once
#include<iostream>
#include"Person.h"
#include<string>
using namespace std;
class Employee:virtual public Person {
	float salary;
public:
	Employee(string name,int age,long id, float salary):Person( name, age,id), salary(salary){}
	virtual void DetailsPerson();
};
