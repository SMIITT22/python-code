# a = 12
# b = 34

# print("the sum of a and b is", a + b )

# uper ki jo simple process hai usko hum "procedure oriented programming"


# hum ab is uper ke code ko OOP me likhenge...

class Number:
    def sum(self):
        return self.a +self.b

num = Number()
num.a = 12
num.b = 34
s = num.sum()
print(s)


# class kabhi bhi memory nahi leta, us par jab object ko instantiotion karaya jata hai tab hi memory ka use hota hai

'''
PascalCase 
EmployeeName -->PascalCase 

camelCase
isNumeric, isFloatOrInt -->camelCase
'''