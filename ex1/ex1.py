class User:

    def __init__(self, firstname):
        self.firstname = firstname
        self.friends = []
        self.phone_books = {}

    def add_contact(self, contact, tag):
        if tag not in self.phone_books:
            print("Данный тэг не найден")
            return
        self.phone_books[tag].add_contact(contact)

    def delete_friends(self, firstname):
        if firstname in self.friends:
            self.friends.remove(firstname)
            print(f"{firstname} удален из списка друзей")
        print("Такого друга не существует")

    def add_friends(self, user):
        if user not in self.friends:
            self.friends.append(user)
            print(f"Пользователь {user.firstname} добавлен в друзья")
        else:
            print("Вы уже дружите")

    def add_phone_book(self, tag):
        if tag not in self.phone_books:
            self.phone_books[tag] = PhoneBook(tag)
        else:
            print(f"Данная телефонная книга {tag} уже существует")

    def share_phone_books(self, user, tag):
        if user not in self.friends:
            print(f"C {user} вы не друзья")
            return
        if tag not in self.phone_books:
            print(f"Телефонная книга с тегом {tag} не существует")
        user.phone_books[tag] = self.phone_books[tag]


class PhoneBook:
    def __init__(self, tag):
        self.tag = tag
        self.contacts = []

    def add_contact(self, contact):
        if contact in self.contacts:
            print("Данный контакт уже существует")
        self.contacts.append(contact)

    def delete_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
        print("Данный контакт не существует")

    def filter_user(self, user):
        return [contact for contact in self.contacts if contact.user == user]

    def filter_country_code(self, country_code):
        return [contact for contact in self.contacts if contact.country_code == country_code]


class Contact:
    def __init__(self, user, country_code, phone_number):
        self.user = user
        self.country_code = country_code
        self.phone_number = phone_number


class Admin:
    @staticmethod
    def add_contact_to_phone_book(contact, phone_book):
        phone_book.add_contact(contact)

    @staticmethod
    def remove_contact_to_phone_book(contact, phone_book):
        phone_book.delete_contact(contact)



user1 = User("Mekan")
user2 = User("Andrey")

# Добавляем друзей
user1.add_friends(user2)

# Создаем телефонные книжки
user1.add_phone_book('family')
user2.add_phone_book('work')

contact1 = Contact(user1, '1', '98764213')
contact2 = Contact(user2, '1', '32134123')

user1.add_contact(contact1, 'family')
user2.add_contact(contact2, 'work')

user1.share_phone_books(user2, 'family')

