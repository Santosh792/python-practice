#1
'''try:
    print(10*(1/0))
    print(203/0)
    print(var*33)
except(ZeroDivisionError,NameError):
    print('Error')'''

#2)

'''class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author  # Added author attribute
        self.pages = pages

    def __str__(self):
        return "Title: %s, Author: %s" % (self.title, self.author)

    def __len__(self):
        return self.pages

book = Book("Core Python Programming", "Wesley J. Chun", 1077)
print(book)
d = len(book)
print("Pages:", d)

'''

'''class MultiplierClass:
    def __init__(self,factor):
        self.factor=factor
    def multiplier(self,argument):
        return argument * self.factor

def generate_multiplier(factor):
    return MultiplierClass(factor).multiplier
twice = generate_multiplier(2)
print(twice(5))'''


#Q
'''class Cow:
    species = 'mammal'

    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.species='birds'

mucy = Cow('Mucy', 3)

print(Cow.species)
print(mucy.species)'''



'''xyz = ('apple','apple','app')
abc = 'Assassination'
print(abc.replace('s','S',len(min(xyz))))'''

'''
You are asked to match a patter exactly at the beginning. Which of these function would you choose?
1) re.search
2) re.first
3) re.match
4) re compile
'''

'''def func1(var1=1,var2=2):
    print(var1,end=" ")
    print(var2, end=" ")
func1(100,None)
func1(var2=20,var1=10)
func1(var2=10)'''

'''for counter in 10,20,'string' , 30:
    print(" I fetched ", counter)'''


'''import re
message = "I thought a great thought today"
print(re.sub('thought','jump',message))'''
#sub=subsitition , on the place of thought , jump will subsitute

'''num = [1,123,121,12,110,11,10]
sorted(num)
print(num)
'''

'''
Which of the following command is used to open a file "c:\demo.txt" in append-mode?
1) op=open("c:\\demo.txt"'"a+")
2) op=open("c:\\demo.txt","rw+")
3) op=open("c:\\demo.txt","w+")
4) op=open("c:\\demo.txt")
'''

# open("c:\\demo.txt", "a+"): This command opens the file in append mode ("a+").
# The "a+" mode stands for append and read mode, which means that if the file exists,
# it will be opened for appending; if the file does not exist, a new file will be created.
# The file pointer is positioned at the end of the file, so any data written to the file
# will be added at the end.

'''
If user enter5.0  as input, Which of the following data type is assigned to the variable "var"?
var=input("Enter a value:")
1)Decimal
2)string
3)float
4)None
'''


 '''print(50+delta*10))'''


'''
which option is correct based on python
1)If argument passed is mutable then it follows pass by reference
2)Any mismatch in parameter number will throw an Attribute error
3)A return statement with no argument is not same as return None
4)Return statement inside the function is mandatory
'''








'''
choose correct options
1)If argument passed is mutable then it follows pass by reference
2)Any mismatch in parameter number will throw an Attribute error
3)A return statement with no argument is not same as return None
4)Return statement inside the function is a mandatory
'''

'''import re
num="The event starts in Jan"
print(re.split('"',num))'''

'''Score = [50,50,0,2,190,105,41,11,27,0,4]
print(Score.count(0))'''

'''palindrome = "malayalam"
print(palindrome.strip('mal'))'''

'''num1 = {1,11,15,66,78}
num2 = {11,66}
result = num1 and num2
print(result)'''

'''Assume that Ram has framed his regular expression like [Aa]bc for pattern matching.
Which of the following matches with the pattern mentioned above?
1) Aabc only
2) abc only
3) Abc only
4) Both abc and Abc
'''

'''
Assume the Raghu has framed his regular expression like Indic?a for the pattern matching. which of the 
following matches with the pattern mentioned above?
1)Indic?a
2)Indica Only
3)Indica, Indicca only
4)both India and Indica
'''



















# import re
# name = 'Ram_06at1982@gmail.com'
# print(re.findall('[\d]+',name))


#


# try:
#        access_proto()
# except AccessError,LoginError:

# a = ' PYTHON PROGRAM '
#
# print (a.lstrip('P'))
#
# import re
# num ="The event starts in Jan"
# print(re.split('"',num))

# import re
# a = "Malaaavikaa"
# print(re.sub('a{2}','*' ,a ,1))
#

# num = [1,123,121,12,110,11,10]
# sorted(num)
# print(num)













#1) Error 1











