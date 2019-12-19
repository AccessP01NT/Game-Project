#include "WorkingStudent.h"

void WorkingStudent::DetailsPerson()
{
	Employee::DetailsPerson();
	student::DetailsPerson();
	cout << "same_institute: " << same_institute;
}
