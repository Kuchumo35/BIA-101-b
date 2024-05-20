class Income:
    def __init__(self, salary):
        self.salary = salary

class TaxComputation:
    tax_rates = [(300000, 0), (400000, 0.1), (650000, 0.15), (1000000, 0.20), (1500000, 0.25), (1500001, 0.30)]
    surcharge_threshold = 1000000
    surcharge_rate = 0.10

    @staticmethod
    def calculate_tax(income):
        total_income = income.salary 
        if total_income < TaxComputation.tax_rates[0][0]:
            raise ValueError("Income is below the minimum taxable limit and is exempt from tax.")
        
        tax = 0
        for rate in TaxComputation.tax_rates:
            if total_income <= rate[0]:
                tax += total_income * rate[1]
                break
            else:
                tax += (rate[0] - tax) * rate[1]

        if tax >= TaxComputation.surcharge_threshold:
            tax += tax * TaxComputation.surcharge_rate

        return tax

class Employee:
    def __init__(self, income, children=0, employee_type="regular", organization_type="government"):
        self.income = income
        self.children = children  
        self.employee_type = employee_type
        self.organization_type = organization_type

    def is_contract_employee(self):
        return self.employee_type == "contract"

class Deductions:
    pension_rate = 0.16
    provident_fund_rate = 0.10
    NPPF_max = 0.26
    GIS_max = 50000
    
    @staticmethod
    def calculate_deductions(employee, child_deduction_per_child):
        total_deductions = 0

        if not employee.is_contract_employee():
            nppf_deduction = employee.income.salary * (Deductions.pension_rate + Deductions.provident_fund_rate)
            total_deductions += min(nppf_deduction, Deductions.NPPF_max)

        total_deductions += employee.children * child_deduction_per_child
        total_deductions += min(employee.income.salary * 0.05, Deductions.GIS_max)

        return total_deductions

def run_tax_calculation(max_outputs=2):
    output_count = 0
    while output_count < max_outputs:
        salary = float(input("Enter salary: "))
        if salary >= TaxComputation.tax_rates[0][0]:
            break
        print("Income is below the minimum taxable limit and is exempt from tax.")
        print("Please enter a valid salary.")

        employee_type = input("Enter employee type (regular/contract): ").lower()
        organization_type = input("Enter organization type (government/private): ").lower()
        children = int(input("Enter number of children: "))
        child_deduction_per_child = float(input("Enter deduction per child (up to a max of Nu. 350,000 per child): "))
        total_child_deduction = 0

        for i in range(children):
            enrolled_for_education = input(f"Is child {i+1} enrolled for education? (yes/no): ").lower()
            if enrolled_for_education == "yes":
                total_child_deduction += child_deduction_per_child

        income = Income(salary)
        employee = Employee(income, children, employee_type, organization_type)
        total_deductions = Deductions.calculate_deductions(employee, child_deduction_per_child)
        taxable_income = income.salary - total_deductions
        tax = TaxComputation.calculate_tax(income)
        surcharge = tax * TaxComputation.surcharge_rate if tax >= TaxComputation.surcharge_threshold else 0
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

        output_count += 1

# Run the tax calculation up to 5 times
for _ in range(2):
    run_tax_calculation()
