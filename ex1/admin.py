class Admin:
    @staticmethod
    def add_contact_to_phone_book(contact, phone_book):
        phone_book.add_contact(contact)

    @staticmethod
    def remove_contact_to_phone_book(contact, phone_book):
        phone_book.delete_contact(contact)

    @staticmethod
    def add_friends(user, friend):
        user.add_friends(friend)

    @staticmethod
    def add_phone_book(user, tag):
        user.add_phone_book(tag)

    @staticmethod
    def share_phone_books(user1, user2, tag):
        user1.share_phone_books(user2, tag)