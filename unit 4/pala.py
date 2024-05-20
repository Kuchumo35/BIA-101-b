class Employee:#It shows an individual employee together with their employment type and income information.
    def _init_(self, name, income, employee_type, organisation_type):# Initialize the Employee object with name, income, employee_type, and organisation_type
        self.name = name# Set the 'name' attribute of the Employee object to the provided name
        self.income = income# Set the 'income' attribute of the Employee object to the provided income
        self.employee_type = employee_type# Set the 'employee_type' attribute of the Employee object to the provided employee_type
        self.organisation_type = organisation_type# Set the 'organisation_type' attribute of the Employee object to the provided organisation_type
    

    def calculate_tax(self):# Defining a method to calculate the tax for the Income
        deductions = self.calculate_deductions()# Calling the calculate_deductions method to compute deductions for the Employee's Income
        taxable_income = self.income - deductions# Calculating the taxable income for the Employee's Income by subtracting deductions from the income
        tax = self.calculate_tax_rate(taxable_income)# Calculating the tax for the Employee based on their taxabletd income
        if tax >= 1000000:# If the calculated tax for the Employee exceeds or equals 1500000
            tax += tax * 0.10# Apply a 10% surcharge to the tax amount if it exceeds or equals 1500000
        return tax#It will return to the final tax amount
    

    def calculate_deductions(self):# Calculate deductions for the Employee
        deductions = 0#Deductions variable to 0

        # NPPF deduction
        if self.employee_type == 'Regular' and self.organisation_type!= 'Government':# If the employee type is 'Regular' and the organisation type is not 'Government'
            deductions += 0.10 * self.income#It will apply a 10% deduction to the income if the employee is Regular and the non-government organisation.
        # GIS deduction
        if self.employee_type == 'Regular' and self.organisation_type!= 'Government':#If the employee type is Regular and the organisation type is not 'Government'
            deductions += 0.05 * self.income#It will apply a 5% deduction to the income if the employee type is Regular and the government organisation

        # Education allowance deduction
        deductions += 350000#Add a fixed deduction of 350000

        # Other deductions
        deductions += 0.30 * self.income#It will apply a 30% deduction to the income

        return deductions#It will return to the total deductions calculated for the employee

    def calculate_tax_rate(self, taxable_income):#It will Calculate the tax rate based on the taxable income given
        if taxable_income <= 300000:#If the taxable income is less than or equal to 300,000
            return 0#It will return 0 tax rate 
        elif taxable_income <= 400000:#If the taxable income is less than or equal to 400,000
            return 0.10 * (taxable_income - 300000) #It will calculates the tax rate for taxable incomes falling within the range of 300,000 to 400,000.
                                                    #It applies a tax rate of 10% to the portion of income exceeding 300,000.
        elif taxable_income <= 650000:# If the taxable income is less than or equal to 650,000
            return 0.15 * (taxable_income - 400000) + 10000 #It will calculates the tax rate for taxable incomes falling within the range of 400,000 to 650,000. 
                                                            #It applies a tax rate of 15% to the portion of income exceeding 400,000, then adds a fixed tax amount of 10,000.
        elif taxable_income <= 1000000:# If the taxable income is less than or equal to 1,000,000
             return 0.10 * (taxable_income - 300000) #It will calculates the tax rate for taxable incomes falling within the range of 300,000 to 400,000.
                                                    #It applies a tax rate of 10% to the portion of income exceeding 300,000.
        elif taxable_income <= 650000:# If the taxable income is less than or equal to 650,000
            return 0.15 * (taxable_income - 400000) + 10000 #It will calculates the tax rate for taxable incomes falling within the range of 400,000 to 650,000. 
                                                            #It applies a tax rate of 15% to the portion of income exceeding 400,000, then adds a fixed tax amount of 10,000.
        elif taxable_income <= 1000000:# If the taxable income is less than or equal to 1,000,000
            return 0.20 * (taxable_income - 650000) + 35000#It will calculates the tax rate for taxable incomes falling within the range of 650,000 to 1,000,000. 
                                                            #It applies a tax rate of 20% to the portion of income exceeding 650,000, then adds a fixed tax amount of 35,000.
        elif taxable_income <= 1500000:#If the taxable income is less than or equal to 1,500,000
            return 0.25 * (taxable_income - 1000000) + 75000#It will calculates the tax rate for taxable incomes falling within the range of 1,000,000 to 1,500,000.
                                                            #It applies a tax rate of 25% to the portion of income exceeding 1,000,000, then adds a fixed tax amount of 75,000.
        else:
          return 0.30 * (taxable_income - 1500000) + 125000#It will calculates the tax rate for taxable incomes exceeding 1,500,000.
                                                            #It applies a tax rate of 30% to the portion of income exceeding 1,500,000, then adds a fixed tax amount of 125,000.

if _name_ == "_main_":
    name = input("What's your name?\n>>> ")# User to enter the employee's name.
    income = float(input("What's 
     annual income?\n>>>")) # Asks the user to input the employee's income and converts it to a floating-point number.
    employee_type = input("Enter the employee's type (Regular or Contract):\n>>> ")# Requests the user to specify the employee's type (Regular or Contract).
    organisation_type = input("Enter the organisation's type (Government or Private):\n>>> ")# Asks the user to indicate the type of the organisation (Government or Private).

    employee = Employee(name, income, employee_type, organisation_type)
    print(f"Total tax applicable at Nu.{income} is Nu.{employee.calculate_tax()}.")
    print(f"Tax for {name} is calculated.")
    print(f"Thank you for Using :")