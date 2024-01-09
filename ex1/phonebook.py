class PhoneBook:
    def __init__(self, tag):
        self.tag = tag
        self.contacts = []

    def add_contact(self, contact):
        if contact in self.contacts:
            raise ValueError("Данный контакт уже существует")
        self.contacts.append(contact)

    def delete_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
        raise ValueError("Данный контакт не существует")

    def filter_user(self, user):
        return [contact for contact in self.contacts if contact.user == user]

    def filter_country_code(self, country_code):
        return [contact for contact in self.contacts if contact.country_code == country_code]