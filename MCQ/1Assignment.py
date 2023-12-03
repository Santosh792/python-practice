#MCQ Practice

#1)
'''class Book:
    def __init__(self,title,author):
        print("A book is created")
        #self.hello=author
        self.title=title
    def __str__(self):
        return self.title
    def __del__(self):
         print("A book is destroyrd")
book=Book("Core python Programming","santosh")
print(book)
del book'''

#A book is created
#core python programming
#A book is destroyed

#2)
''''class MultiplierClass:
    def __init__(self,factor):
        self.Factor=factor
    def multiplier(self,argument):
        return argument*self.Factor
    def hello(factor):
        return MultiplierClass(factor)
twice = hello(2)
print(twice(5))'''

'''class MultiplierClass:
    def __init__(self, factor):
        self.Factor = factor

    def multiplier(self, argument):
        return argument * self.Factor

    @staticmethod
    def hello(factor):
        return MultiplierClass(factor)

# Create an instance of MultiplierClass using the hello method
twice = MultiplierClass.hello(2)

# Use the multiplier method to get the output
print(twice.multiplier(5))'''
#Q3)
class Point:
    x=0
    y=0
    def __init__(self,x,y):
        Point.x=x
        Point.y=y
        self.x=x
        self.y=y
p1 = Point(1,2)
p2 = Point(3,4)
p2.x=2

#Output: