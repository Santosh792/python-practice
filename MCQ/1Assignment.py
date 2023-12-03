#MCQ Practice

#1)
class Book:
    def __init__(self,title,author):
        print("A book is created")
        self.hello=author
        self.title=title
    def __str__(self):
        return self.title
    def __del__(self):
         print("A book is destroyrd")
book=Book("Core python Programming","santosh")
print(book)
del book

#A book is created
#core python programming
# A book is destroyed
