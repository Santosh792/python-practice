#1
'''try:
    print(10*(1/0))
    print(203/0)
    print(var*33)
except(ZeroDivisionError,NameError):
    print('Error')'''

#2)

class Book:
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































# import re
# name = 'Ram_06at1982@gmail.com'
# print(re.findall('[\d]+',name))


#
# xyz =("apple", "applets", "app",'ap')
# abc= "Semesters"
#
# sub ='e'
#
# print(abc.find(sub, len(min(xyz)),len(max(xyz))))

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











