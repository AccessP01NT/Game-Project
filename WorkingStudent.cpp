#include "WorkingStudent.h"

void WorkingStudent::DetailsPerson()
{
	Employee::DetailsPerson();
	Student::DetailsPerson();
	cout << "same_institute: " << same_institute;
}
