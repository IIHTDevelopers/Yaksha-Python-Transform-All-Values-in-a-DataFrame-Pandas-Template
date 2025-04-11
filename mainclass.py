import pandas as pd

class EmployeeDataAnalysis:
    def __init__(self, file_path):
        pass
        """Load CSV data into a Pandas DataFrame."""
        # self.df = pd.read_csv(file_path)

    def display_head(self):
        pass
        """Return the first 5 rows of the DataFrame."""
        # return self.df.head()

    def dataframe_info(self):
        pass
        """Return DataFrame column names and data types."""
        # return self.df.info()

    def increase_salary(self):
        pass
        """Increase salary by 10% using the apply function."""
        # self.df['Salary'] = self.df['Salary'].apply(lambda x: x * 1.10)
        # return self.df

    def save_to_csv(self, output_file="updated_employee_data.csv"):
        pass
        """Save the updated DataFrame to a new CSV file."""
        # self.df.to_csv(output_file, index=False)

