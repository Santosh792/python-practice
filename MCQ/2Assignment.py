#Assignment2 MCQ
#Input1:
'''Tech="Python"
print(Tech*len(Tech))'''

#Input2:
'''Name=["santosh",'kumar','yadav','Babu']
print(Name[-2][2])'''

#Input3:
'''Company = 'Infosys' + \
           '\nTechnologies' + \
           '\nLimited'
print('Company')'''

#input4
'''def add(num1=2, num2=2):
    return (num1+num2)
print(add(4))'''

#input5
'''print(50+delta*10)'''
#error=?

#Input6
'''
import math
print(math.floor(5.7))
'''


#Input7
'''
var = (30)
print(var + 'hello')
'''

'''
age = 36
name = 'Santosh'
output = f"{age }"   " " f"{ name}"
output = f"{age } { name}"
print(output)
'''

'''
_=100
print(_)

'''

#Input8
'''x = -1
if (x == 1):
    print("do something")
elif (x == -1):
    pass
else:
    print("in else")'''

#Input9
'''import re
statement = 'Raj,x,1231,raj_01'
a=re.split(',',statement)
print(a[2])

import re
statement = 'Raj:x:1231:raj_01'
a=re.split(':',statement)
print(a[3])'''

#Input10
#Arrange in accending order
'''
Jython,IronPython,Pydev,Django
'''

'''
frameworks = ['Jython', 'IronPython', 'Pydev', 'Django']
sorted_frameworks = sorted(frameworks)

for framework in sorted_frameworks:
    print(framework)
    '''

'''name = ['santosh','shobha','rajni','raushan']
arrange=sorted(name)
for name in  arrange:
    print(name)'''


#Input11
'''Basicsalary = 55000.56
DA = 5000.34
print("My salary is %d" % (Basicsalary+DA))'''


Basicsalary = 55000.56
DA = 5000.34
print("My salary is %.2f" % (Basicsalary + DA))






























#Output1: TechTechTechTechTechTech
#Output2:d (-2 index refer from last which is 'yadav', 2nd indev is 'yadav' itself but start from front and zero)
#Output3: Company
#Output4: print(add(4)) its self act as num1. So it over ride num1 by it's calling value
#Output5: Nameerror
#Output6: 5
#Output7: Errror
#Output8: No Output
#Output11:My salary is 60000. %d(single place holder) or %.2f(two decimal placeholder)




