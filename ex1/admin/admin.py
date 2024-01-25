from ex1.user import User


class Admin(User):
    def __init__(self, firstname):
        super().__init__(firstname)

    def add_contact_from_to_user(self, to_user, contact, tag):
        if tag in to_user.phone_books[tag]:
            to_user.phone_book[tag].add_contact(contact)
        else:
            raise ValueError(f"Нет телефонной книги {tag} для пользователя {to_user}")

    def delete_contact_from_to_user(self, user, tag, contact):
        if tag in user.phone_books[tag]:
            user.phone_books[tag].delete_contact(contact)
        else:
            raise ValueError(f"Нет телефонной книги {tag} для пользователя {user}")


