class Book:
    def __init__(self, book_name, counts):
        self.book_name = book_name
        self.counts = counts
    def borrows(self):
        if(self.counts>0):
            self.counts-=1
            return True
        else:
            return False
    def returns(self):
        self.counts+=1
class Library:
    def __init__(self):
        self.avail_books_list = []
        self.members_list = []
    def new_membership(self, member):
        if member not in self.members_list:
            self.members_list.append(member)
        else:
            print(f"Member with name {member_name} already present")
    def cancel_membership(self, member):
        if member in self.members_list:
            self.members_list.remove(member)
        else:
            print("No such member exists")
    def add_new_book(self, book_name):
        if book_name not in self.avail_books_list:
            self.avail_books_list.append(book_name)
        else:
            print("Book already available")
class Member:
    def __init__(self, name):
        self.name = name
        self.books_taken = []
    def borrow_book(self, book):
        self.books_taken.append(book)
    def return_book(self,book):
        self.books_taken.remove(book)

#example
lib = Library()
book1 = Book('It ends with us',5)
book2 = Book('The Alchemist',3)
lib.add_new_book(book1)
lib.add_new_book(book2)
mem1 = Member('Kanchana')
mem2 = Member('Madhuri')
lib.members_list.append(mem1)
lib.members_list.append(mem2)
print(lib.members_list)

