from ex1.phonebook import PhoneBook


class User:

    def __init__(self, firstname):
        self.firstname = firstname
        self.friends = []
        self.phone_books = {}

    def add_contact(self, contact, tag):
        if tag not in self.phone_books:
            raise ValueError("Данный тэг не найден")
        self.phone_books[tag].add_contact(contact)

    def delete_friends(self, firstname):
        if firstname in self.friends:
            self.friends.remove(firstname)
            raise ValueError(f"{firstname} удален из списка друзей")
        raise ValueError("Такого друга не существует")

    def add_friends(self, user):
        if user not in self.friends:
            self.friends.append(user)
            print(f"Пользователь {user.firstname} добавлен в друзья")
        else:
            raise ValueError("Вы уже дружите")

    def add_phone_book(self, tag):
        if tag not in self.phone_books:
            self.phone_books[tag] = PhoneBook(tag)
        else:
            raise ValueError(f"Данная телефонная книга {tag} уже существует")

    def share_phone_books(self, user, tag):
        if user not in self.friends:
            raise ValueError(f"C {user} вы не друзья")
        if tag not in self.phone_books:
            raise ValueError(f"Телефонная книга с тегом {tag} не существует")
        user.phone_books[tag] = self.phone_books[tag]
