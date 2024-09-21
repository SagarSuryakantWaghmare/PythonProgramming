print("Welcome to your library:")
class library:
    def __init__(self):
         self.books=[]
         self.noOfBook=0
    def addBooks(self,book):
         self.books.append(book)
         self.noOfBook=len(self.books)
    def showDetails(self):
         print(f"The no of books in the library {self.noOfBook} and the books are :")  
         for book in self.books:
              print(book)
l1=library()
l1.addBooks("Avengers")
# l1.showDetails()

l1.addBooks("Harry Potter")
l1.showDetails()
