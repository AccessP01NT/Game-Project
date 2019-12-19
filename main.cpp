#include "Person.h"
#include <string>
#include "Student.h"
#include "Employee.h"
#include "WorkingSudent.h"
#define size 4
int main() {
	int type,age,average;
	long id;
	float salary;
	string name, institute;
	Person* arr[size];
	for (int i = 0; i < size; i++) {
		cout << "Enter you Person type: 1-Person 2-Student 3-Employee 4-Working Student" << endl;
		cin >> type;
		if (type == 1) {
			cout << "Name:" << name << endl;
			cin >> name;
			cout << "age:" << age << endl;
			cin >> age;
			cout << "id:" << id << endl;
			cin >> id;
			arr[i] = new Person(name, age, id);
		}
		else if (type == 2) {
			cout << "Name:" << name << endl;
			cin >> name;
			cout << "age:" << age << endl;
			cin >> age;
			cout << "id:" << id << endl;
			cin >> id;
			cout << "institute:" << institute << endl;
			cin >> institute;
			cout << "average:" << institute << endl;
			cin >> average;
			arr[i] = new Student(name, age, id, institute, average);
		}
		else if (type == 3) {
			cout << "Name:" << name << endl;
			cin >> name;
			cout << "age:" << age << endl;
			cin >> age;
			cout << "id:" << id << endl;
			cin >> id;
			cout << "salary:" << institute << endl;
			cin >> salary;
			arr[i] = new Employee(name, age, id, salary);
		}
		else if (type == 4) {
			exit(1);
		}
	}
	for (int i = 0; i < size; i++) {
		arr[i]->DetailsPerson();
	}
	system("pause");
}