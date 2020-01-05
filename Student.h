#ifndef _Student
#define _Student
#include <iostream>
#include <string>
#include "Person.h"
using namespace std;

class Student:virtual public Person{
private:
	int average;
	string institute;
public:
	Student(string name, int age, long id,string institute,int average) :Person(name, age, id), institute(institute), average(average){}
	virtual void DetailsPerson();
	
};


	


#endif