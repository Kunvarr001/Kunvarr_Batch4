#Assignment 5: Employee Management

class Employee:
    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.is_working = True

    def terminate_employee(self):
        self.is_working = False

    def is_currently_working(self):
        return self.is_working


class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def save_employee_to_database(self, employee):
        self.employees.append(employee)
        return True


class EmployeeReportCSV:
    def print_employee_detail_report_csv(self, employees):
        for emp in employees:
            status = "Working" if emp.is_currently_working() else "Terminated"
            print(f"{emp.employee_id},{emp.name},{emp.department},{status}")


class EmployeeReportXML:
    def print_employee_detail_report_xml(self, employees):
        print("<Employees>")
        for emp in employees:
            status = "Working" if emp.is_currently_working() else "Terminated"
            print(f"  <Employee>"
                  f"<ID>{emp.employee_id}</ID>"
                  f"<Name>{emp.name}</Name>"
                  f"<Department>{emp.department}</Department>"
                  f"<Status>{status}</Status>"
                  f"</Employee>")
        print("</Employees>")

if __name__ == "__main__":
    first_employee = Employee(1, "Alice", "HR")
    second_employee = Employee(2, "Bob", "IT")

    emp_database = EmployeeDatabase()
    emp_database.save_employee_to_database(first_employee)
    emp_database.save_employee_to_database(second_employee)

    second_employee.terminate_employee()

    csv_report = EmployeeReportCSV()
    csv_report.print_employee_detail_report_csv(emp_database.employees)

    xml_report = EmployeeReportXML()
    xml_report.print_employee_detail_report_xml(emp_database.employees)


"""
Mistakes / Issues in Original C# Code
    1. Violates SRP (Single Responsibility Principle): The Employee class is doing too much
    2. No method definitions provided
"""