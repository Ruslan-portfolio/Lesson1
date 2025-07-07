from adress import Address
from mail import Mailing

to_address = Address("123456", "Москва", "Ленина", "10", "25")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "30")

# Создаем почтовое отправление
mail = Mailing(to_address, from_address, 500, "RU123456789")

# Печатаем информацию
print(f"Отправление {mail.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment} в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment}. Стоимость {mail.cost} рублей.")