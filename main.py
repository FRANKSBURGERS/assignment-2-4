# input statements
salary = float(input("Enter the salary: "))
numDependents = float(input("Enter the number of dependents: "))

# calculate taxes here
sateTaxes = salary * 0.065 
federalTaxes = salary * 0.28
dependentDeduction = salary * 0.025 * numDependents 

# Total take home pay after deductions 
totalWithholding = sateTaxes + federalTaxes + dependentDeduction
takeHomePay = salary - totalWithholding

# output statements
print("State Tax: $" + str(sateTaxes))
print("Federal Tax: $" + str(federalTaxes))
print("Dependent Deduction: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
