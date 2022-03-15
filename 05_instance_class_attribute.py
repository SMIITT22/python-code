# class Employee:
#     company = "marvel"
#     salary = "55k"
       
# smit = Employee()
# jay = Employee()
# smit.salary = "40k"
# jay.salary = "45k"
# print(smit.salary)
# print(jay.salary)

#isme sabse pahle object/instance attribute ko priority milegi bad me class attribute ayega isi
#liye isme print 40k and 45k ho raha hai...

#example of class attribute priority case.

class Employee:
    company = "marvel"
    salary = "55k"
    

smit = Employee()
jay = Employee()
# smit.salary = "40k"
# jay.salary = "45k"
print(smit.salary)
print(jay.salary)

#abhi sirf 55k print hoga... 