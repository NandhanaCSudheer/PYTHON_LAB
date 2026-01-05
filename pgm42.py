class Publisher:
    def __init__(self,name):
        self.name=name
        print("Base class constructor invocation for ",self.name)
    
    def display(self):
        print(f"Published by: {self.name}")

class Book(Publisher):
    def __init__(self, name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
        print("Child class constructor invocation for ",self.title,"by ",self.author)

    def display(self):
        print("Book details: ")
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Publisher:{self.name}")

class Python(Book):
    def __init__(self,name,title,author,price,pageno):
        super().__init__(name,title,author)
        self.price=price
        self.pageno=pageno

    def display(self):
        print("Book details: ")
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Publisher:{self.name}")
        print(f"Price:{self.price}")
        print(f"No.of pages:{self.pageno}")

b=Python("Bloomsbury","Harry Potter","J.K Rowling",1500,3548)
b.display()