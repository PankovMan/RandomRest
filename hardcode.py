import random

def restaurant_randomizer(restaurants):
    """Рандомайзер для выбора ресторана"""
    if not restaurants:
        return "Список ресторанов пуст!"
    return f"Сегодня идём в: {random.choice(restaurants)}!"

# Список ресторанов можно изменить под свои предпочтения
restaurant_list = [
    "Итальянский ресторан",
    "Японское кафе",
    "Грузинская кухня",
    "Бургерная",
    "Пиццерия",
    "Суши-бар",
    "Стейк-хаус",
]

# Запуск рандомайзера
print(restaurant_randomizer(restaurant_list))