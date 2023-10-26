# Inisialisasi data
book_dic = {}
borrowed_dic = {}

# User
def borrow_book(username, book, book_dic, borrowed_dic):
    if book in book_dic and book not in borrowed_dic.get(username, []):
        borrowed_dic.setdefault(username, []).append(book)
        book_dic[book] = 0
        return f"Selamat, {username} telah meminjam buku '{book}'."
    elif book in borrowed_dic.get(username, []):
        return f"{username} sudah meminjam buku '{book}'."
    else:
        return f"Buku '{book}' tidak tersedia."

def return_book(username, book, book_dic, borrowed_dic):
    if book in borrowed_dic.get(username, []):
        borrowed_dic[username].remove(book)
        book_dic[book] = 1
        return f"{username} telah mengembalikan buku '{book}'."
    else:
        return f"{username} belum meminjam buku '{book}'."

# Admin
def add_book(book, book_dic):
    book_dic[book] = 1
    return f"'{book}' telah terdaftar."

def view_books(book_dic):
    book_status = {book: 'Tersedia' if status == 1 else 'Dipinjam' for book, status in book_dic.items()}
    return book_status

def update_book(book_name, new_status, book_dic):
    if book_name in book_dic:
        book_dic[book_name] = new_status
        return f"Status buku '{book_name}' adalah {'Tersedia' if new_status == 1 else 'Dipinjam'}."
    else:
        return f"Buku '{book_name}' tidak ditemukan."

def delete_book(book_name, book_dic):
    if book_name in book_dic:
        del book_dic[book_name]
        return f"Buku '{book_name}' telah dihapus dari daftar."
    else:
        return f"Buku '{book_name}' tidak ditemukan."

# Fitur 'find'
def find_book(book_name, book_dic):
    matching_books = [book for book in book_dic if book_name.lower() in book.lower()]
    return matching_books

# Fitur 'edit'
def edit_book(book_name, new_book_name, book_dic):
    if book_name in book_dic:
        book_dic[new_book_name] = book_dic.pop(book_name)
        return f"Nama buku '{book_name}' telah diubah menjadi '{new_book_name}'."
    else:
        return f"Buku '{book_name}' tidak ditemukan."

# # Contoh penggunaan
# add_book("Harry Potter", book_dic)
# add_book("Lord of the Rings", book_dic)
# add_book("The Hobbit", book_dic)

# print(view_books(book_dic))
# print(borrow_book("User1", "Harry Potter", book_dic, borrowed_dic))
# print(borrow_book("User2", "Harry Potter", book_dic, borrowed_dic))
# print(view_books(book_dic))
# print(return_book("User1", "Harry Potter", book_dic, borrowed_dic))
# print(delete_book("The Hobbit", book_dic))
# print(view_books(book_dic))

# print(find_book("harry", book_dic))
# print(edit_book("Harry Potter", "HP Series", book_dic))
# print(view_books(book_dic))
