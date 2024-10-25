size_file_Mb = 1.44
size_file = 1.44 * 1024 * 1024

countPages = 100
countString = 50
countSymbol = 25
size_symbol = 4

size_book = size_symbol * countSymbol * countString * countPages

countBook = int(size_file // size_book)
print("Количество книг, помещающихся на дискету:", countBook)
