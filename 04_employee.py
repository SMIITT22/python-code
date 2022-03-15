# class Employee:
#     company = "marvel"
        
# smit = Employee()
# jay = Employee()
# print(smit.company)
# print(jay.company)
# Employee.company = "DC"
# print(smit.company)
# print(jay.company)

#upar vala jo hai vo "class attribute" k bare mai hai

#now lets see about "instance attribute"...
class Employee:
    company = "marvel"

smit = Employee()
jay = Employee()
smit.salary = "40k"
jay.salary = "45k"
print(smit.salary)
print(jay.salary) 