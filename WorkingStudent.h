#pragma once
#include "Employee.h"
#include"student.h"
#include<iostream>
#include<string>
using namespace std;
class WorkingStudent :public Employee,public student {
	bool same_institute;
public:
	WorkingStudent(string name, int age, long id, float salary,string institute,int average, bool same_institute):Person(name, age, id) ,Employee(name, age, id,salary),student(name,age,id,institute,average,same_institute), same_institute(same_institute){}
	void DetailsPerson();
};
