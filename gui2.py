import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    restaurants = []

    while True:
        clear_screen()
        print("=" * 40)
        print("        🍽️ РЕСТОРАННЫЙ РАНДОМАЙЗЕР")
        print("=" * 40)
        print("\nТекущий список ресторанов:")
        for i, rest in enumerate(restaurants, 1):
            print(f"{i}. {rest}")

        print("\nМеню:")
        print("1. Добавить ресторан")
        print("2. Удалить ресторан")
        print("3. Выбрать случайный ресторан")
        print("4. Очистить список")
        print("5. Выйти")

        choice = input("\nВыберите действие (1-5): ")

        if choice == "1":
            new_rest = input("Введите название ресторана: ").strip()
            if new_rest:
                restaurants.append(new_rest)
                print(f"Ресторан '{new_rest}' добавлен!")
            else:
                print("Название не может быть пустым!")
            input("\nНажмите Enter для продолжения...")

        elif choice == "2":
            if restaurants:
                try:
                    num = int(input("Номер ресторана для удаления: "))
                    if 1 <= num <= len(restaurants):
                        removed = restaurants.pop(num - 1)
                        print(f"Ресторан '{removed}' удален!")
                    else:
                        print("Неверный номер!")
                except ValueError:
                    print("Введите число!")
            else:
                print("Список пуст!")
            input("\nНажмите Enter для продолжения...")

        elif choice == "3":
            if restaurants:
                chosen = random.choice(restaurants)
                print(f"\n🎉 СЕГОДНЯ ИДЁМ В: {chosen.upper()}! 🎉")
            else:
                print("Список ресторанов пуст!")
            input("\nНажмите Enter для продолжения...")

        elif choice == "4":
            restaurants.clear()
            print("Список очищен!")
            input("\nНажмите Enter для продолжения...")

        elif choice == "5":
            print("До свидания!")
            break

        else:
            print("Неверный выбор!")
            input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    main()