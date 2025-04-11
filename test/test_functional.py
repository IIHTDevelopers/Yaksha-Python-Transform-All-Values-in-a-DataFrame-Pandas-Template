import unittest
import pandas as pd
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import os


class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")
                
    def test_increase_salary(self):
        """Test if the salary is increased correctly by 10%."""
        try:
            original_salary = self.analysis.df["Salary"].iloc[0]  # First employee salary before increment
            self.analysis.increase_salary()
            increased_salary = self.analysis.df["Salary"].iloc[0]  # First employee salary after increment
            obj = increased_salary == original_salary * 1.10  # Check if the salary increased by 10%
            self.test_obj.yakshaAssert("TestIncreaseSalary", obj, "functional")
            print("TestIncreaseSalary = Passed" if obj else "TestIncreaseSalary = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestIncreaseSalary", False, "functional")
            print("TestIncreaseSalary = Failed")

    def test_save_to_csv(self):
        """Test if the updated DataFrame is saved correctly to CSV."""
        try:
            self.analysis.save_to_csv("updated_employee_data.csv")
            obj = os.path.exists("updated_employee_data.csv")  # Check if the file is saved
            self.test_obj.yakshaAssert("TestSaveToCSV", obj, "functional")
            print("TestSaveToCSV = Passed" if obj else "TestSaveToCSV = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestSaveToCSV", False, "functional")
            print("TestSaveToCSV = Failed")
