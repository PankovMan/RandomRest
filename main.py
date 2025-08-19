import random


def restaurant_randomizer():
    """Рандомайзер с возможностью ввода списка"""
    print("Введите список ресторанов (через запятую):")
    user_input = input("> ")

    restaurants = [r.strip() for r in user_input.split(",") if r.strip()]

    if not restaurants:
        return "Вы не ввели ни одного ресторана!"

    return f"Сегодня идём в: {random.choice(restaurants)}!"


# Запуск
print(restaurant_randomizer())