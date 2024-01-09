from ex1.user import User
from ex1.contact import Contact

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

