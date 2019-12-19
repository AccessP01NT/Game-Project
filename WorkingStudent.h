#pragma once
#include "Employee.h"
#include"Student.h"
#include<iostream>
#include<string>
using namespace std;
class WorkingStudent :public Employee,public Student {
	bool same_institute;
public:
	WorkingStudent(string name, int age, long id, float salary,string institute,int average, bool same_institute):Person(name, age, id) ,Employee(name, age, id,salary),Student(name,age,id,institute,average), same_institute(same_institute){}
	void DetailsPerson();
};
