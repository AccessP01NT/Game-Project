import unittest
import Hakaton_Project


class Test_test1(unittest.TestCase):
    def test_isUserType(self):
        result=Hakaton_Project.isUserType("P")
        self.assertTrue(result)
    def test_isGender(self):
        result=Hakaton_Project.isGender("B")
        self.assertTrue(result)
    def test_Proper_ID(self):
        result=Hakaton_Project.Proper_ID("1234")
        self.assertTrue(result)
    def test_Proper_First_Or_Last_Name(self):
        result=Hakaton_Project.Proper_ID("$2")
        self.assertTrue(result)
    def test_Proper_Age(self):
        result=Hakaton_Project.Proper_Age(-1)
        self.assertTrue(result)
    def test_Check_User_Type_From_DB(self):
        result=Hakaton_Project.Check_User_Type_From_DB("L")
        self.assertTrue(result)
    
        


if __name__ == '__main__':
    unittest.main()
