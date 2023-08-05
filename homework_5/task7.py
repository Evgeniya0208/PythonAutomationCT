# 7) Write a function called print_book_details that prints the details of a book. The function should take a positional argument title
# and two keyword arguments: author and publication_year. Assume that publication_year has a default value of None.
def print_book_details(title, author=None, publication_year=None):
    print(title, author, publication_year)


print_book_details("'Facebook nation :total information awareness'", author="Newton Lee", publication_year="2013")
