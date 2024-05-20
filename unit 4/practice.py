# Income tax calculation

class Employee:
    def __init__(self, name, position, organization_type, monthly_salary):
        self.name = name
        self.position = position
        self.organization_type = organization_type
        self.monthly_salary = monthly_salary

    def calculate_tax(self):
        # Assuming only salary income for simplicity
        taxable_income = self.monthly_salary * 12  # Annual income
        if taxable_income < 300000:
            return "No tax due"
        
        tax_slabs = {
            (300000, 0),
            (400000, 10000),  # 10% on income over 300k
            (650000, 15000 + 10000),  # 15% on income over 400k
            (1000000, 25000 + 15000),  # 20% on income over 650k
            (1500000, 37500 + 25000),  # 25% on income over 1M
            (float('inf'), 45000 + 37500)  # 30% on income over 1.5M
        }

        tax_due = 0
        for lower_bound, rate in tax_slabs:
            if taxable_income > lower_bound:
                tax_due += (taxable_income - lower_bound) * rate / 100
            else:
                break
        
        # Apply surcharge if applicable
        if tax_due >= 100000:
            tax_due += tax_due * 0.10  # 10% surcharge
        
        return f"Tax Due: {tax_due}"

# Example usage
employee1 = Employee("John Doe", "Regular", "Private", 60000)
print(employee1.calculate_tax())

employee2 = Employee("Jane Smith", "Contract", "Government", 70000)
print(employee2.calculate_tax())

