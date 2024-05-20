class Income:
    def __init__(self, salary):
        # Initialize income attributes
        self.salary = salary


class TaxCalculator:
    tax_brackets = [
        # Income Threshold, Tax Rate
        (300000, 0),
        (400000, 0.1),
        (650000, 0.15),
        (1000000, 0.20),
        (1500000, 0.25),
        (1500001, 0.30)
    ]

    surcharge_threshold = 1000000
    surcharge_rate = 0.10

    def calculate_tax(income):
        total_income = income.salary 

        # Exception handling for income below the lowest tax bracket
        if total_income < TaxCalculator.tax_brackets[0][0]:
            raise ValueError("Income is below the minimum taxable limit and is exempt from tax.")
            
        # Calculation of tax based on tax brackets
        tax = 0
        for bracket in TaxCalculator.tax_brackets:
            if total_income <= bracket[0]:
                tax += total_income * bracket[1]
                break
            else:
                tax += (bracket[0] - tax) * bracket[1]

        # Apply surcharge if applicable
        if tax >= TaxCalculator.surcharge_threshold:
            tax += tax * TaxCalculator.surcharge_rate

        return tax


class Employee:
    def __init__(self, income, children=0, employee_type="regular", organization_type="government"):
        # Initialize employee attributes
        self.income = income
        self.children = children  
        self.employee_type = employee_type
        self.organization_type = organization_type

    def is_contract_employee(self):
        return self.employee_type == "contract"


class Deductions:
    pension_rate = 0.16 # Pension contribution rate
    provident_fund_rate = 0.10  # Provident Fund contribution rate
    NPPF_max = 0.26  # Maximum deductible for NPPF #( add provident rate and pension fund)
    GIS_max = 50000  # Maximum deductible for GIS

    
    def calculate_deductions(employee, child_deduction_per_child):
        total_deductions = 0

        if not employee.is_contract_employee():
            nppf_deduction = employee.income.salary * (Deductions.pension_rate + Deductions.provident_fund_rate)
            total_deductions += min(nppf_deduction, Deductions.NPPF_max)

        # Tax deductions for children
        total_deductions += employee.children * child_deduction_per_child

        # Deduct GIS if applicable
        total_deductions += min(employee.income.salary * 0.05, Deductions.GIS_max)

        return total_deductions


def run_tax_calculation():
    # Exception handling for income below the lowest tax bracket
    while True:
        salary = float(input("Enter salary: "))
        if salary >= TaxCalculator.tax_brackets[0][0]:
            break
        print("Income is below the minimum taxable limit and is exempt from tax.")
        print("Please enter a valid salary.")

    #  user input for employee type and children
    employee_type = input("Enter employee type (regular/contract): ").lower()
    organization_type = input("Enter organization type (government/private): ").lower()
    children = int(input("Enter number of children: "))
    child_deduction_per_child = float(input("Enter deduction per child (up to a max of Nu. 350,000 per child): "))
    total_child_deduction = 0

    # Loop through each child to ask if they are enrolled for education or not
    for i in range(children):
        enrolled_for_education = input(f"Is child {i+1} enrolled for education? (yes/no): ").lower()
        if enrolled_for_education == "yes":
            total_child_deduction += child_deduction_per_child

    # Define individual's income
    income = Income(salary)

    # Define employee type and organization type
    employee = Employee(income, children, employee_type, organization_type)

    # Calculate deductions
    total_deductions = Deductions.calculate_deductions(employee, child_deduction_per_child)

    # Calculate taxable income
    taxable_income = income.salary - total_deductions

    # Calculate tax
    tax = TaxCalculator.calculate_tax(income)

    # Calculate surcharge
    surcharge = tax * TaxCalculator.surcharge_rate if tax >= TaxCalculator.surcharge_threshold else 0

    # Calculate total tax payable
    total_tax_payable = tax + surcharge

    print(" ")
    print("Income Details:")
    print(" ")
    print(f"Salary: Nu. {income.salary}")

    print(" ")
    print("Deductions:")
    print(" ")
    print(f"NPPF Deduction: Nu. {min(income.salary * 0.1, Deductions.NPPF_max)}")
    print(f"Child Deduction: Nu. {total_child_deduction}")
    print(f"GIS Deduction: Nu. {min(income.salary * 0.05, Deductions.GIS_max)}")

    print(" ")
    print("Tax Calculation:")
    print(" ")
    print(f"Total Adjusted Gross Income: Nu. {taxable_income}")
    print(f"Tax Payable: Nu. {tax}")
    print(f"Surcharge (10% of Tax): Nu. {surcharge}")
    print(f"Total Tax Payable: Nu. {total_tax_payable}")


run_tax_calculation()
