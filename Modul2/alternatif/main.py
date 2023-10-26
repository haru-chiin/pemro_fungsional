from praktikum import *

def main():
    book_dic = {"Buku A": 1, "Buku B": 1, "Buku C": 1}  # 1 represents available, 0 represents borrowed
    borrowed_dic = {}
    guest = {}
    admin_username = "admin"
    admin_password = "adminpass"

    while True:
        print("\nMenu Utama:")
        print("1. Login sebagai User")
        print("2. Login sebagai Admin")
        print("3. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            if username not in borrowed_dic:
                borrowed_dic[username] = []
                guest[username] = [username]

            if password == "pass":
                while True:
                    print("\nMenu User:")
                    print("1. Pinjam Buku")
                    print("2. Kembalikan Buku")
                    print("3. Cari Buku")
                    print("4. Lihat Daftar Buku")
                    print("5. Kembali ke Menu Utama")

                    user_choice = input("Pilih menu: ")

                    if user_choice == "1":
                        book_name = input("Masukkan nama buku yang ingin dipinjam: ")
                        borrow_book(username, book_name, book_dic, borrowed_dic)
                    elif user_choice == "2":
                        book_name = input("Masukkan nama buku yang ingin dikembalikan: ")
                        return_book(username, book_name, book_dic, borrowed_dic)
                    elif user_choice == "3":
                        search_term = input("Masukkan kata kunci pencarian: ")
                        found_books = find_book(search_term, book_dic)
                        print("Hasil pencarian:")
                        for book in found_books:
                            print(book)
                    elif user_choice == "4":
                        books = view_books(book_dic)
                        for book, status in books.items():
                            print(f"{book}: {'Tersedia' if status == 1 else 'Dipinjam'}")

                    elif user_choice == "5":
                        break
                    else:
                        print("Menu tidak valid.")
            else:
                print("Password salah.")

        elif choice == "2":
            username = input("Masukkan username admin: ")
            password = input("Masukkan password admin: ")

            if username == admin_username and password == admin_password:
                while True:
                    print("\nMenu Admin:")
                    print("1. Tambah Buku")
                    print("2. Lihat Daftar Buku")
                    print("3. Update Status Buku")
                    print("4. Hapus Buku")
                    print("5. Cari Buku")
                    print("6. Edit Buku")
                    print("7. Kembali ke Menu Utama")

                    admin_choice = input("Pilih menu: ")

                    if admin_choice == "1":
                        book_name = input("Masukkan nama buku yang ingin ditambahkan: ")
                        add_book(book_name, book_dic)
                    elif admin_choice == "2":
                        books = view_books(book_dic)
                        for book, status in books.items():
                            print(f"{book}: {'Tersedia' if status == 1 else 'Dipinjam'}")
                    elif admin_choice == "3":
                        book_name = input("Masukkan nama buku yang ingin diupdate: ")
                        new_status = int(input("Masukkan status buku (1: Tersedia, 0: Dipinjam): "))
                        update_book(book_name, new_status, book_dic)
                    elif admin_choice == "4":
                        book_name = input("Masukkan nama buku yang ingin dihapus: ")
                        delete_book(book_name, book_dic)
                    elif admin_choice == "5":
                        search_term = input("Masukkan kata kunci pencarian: ")
                        found_books = find_book(search_term, book_dic)
                        print("Hasil pencarian:")
                        for book in found_books:
                            print(book)
                    elif admin_choice == "6":
                        book_name = input("Masukkan nama buku yang ingin diubah: ")
                        new_book_name = input("Masukkan nama baru untuk buku: ")
                        edit_book(book_name, new_book_name, book_dic)
                    elif admin_choice == "7":
                        break
                    else:
                        print("Menu tidak valid.")
            else:
                print("Username atau password admin salah.")

        elif choice == "3":
            print("Terima kasih")
            break

        else:
            print("Menu tidak valid.")

if __name__ == "__main__":
    main()
