import random
import tkinter as tk
from tkinter import messagebox, scrolledtext


class RestaurantRandomizer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ресторанный рандомайзер")
        self.window.geometry("500x400")

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        tk.Label(self.window, text="🍽️ Ресторанный рандомайзер",
                 font=("Arial", 16, "bold")).pack(pady=10)

        # Поле для ввода ресторанов
        tk.Label(self.window, text="Введите рестораны (каждый с новой строки):").pack(anchor="w", padx=20)

        self.text_area = scrolledtext.ScrolledText(self.window, height=8, width=50)
        self.text_area.pack(padx=20, pady=5)

        # Кнопки
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)

        Black = "Black"
        tk.Button(button_frame, text="🎲 Выбрать случайно",
                  command=self.random_choice, bg="#4CAF50", fg=("%s" % Black)).pack(side="left", padx=5)

        tk.Button(button_frame, text="🧹 Очистить",
                  command=self.clear_text, bg="#f44336", fg=Black).pack(side="left", padx=5)

        tk.Button(button_frame, text="❌ Выход",
                  command=self.window.quit, bg="#607D8B", fg=Black).pack(side="left", padx=5)

        # Поле результата
        self.result_label = tk.Label(self.window, text="",
                                     font=("Arial", 14, "bold"), fg="#2196F3")
        self.result_label.pack(pady=20)

        # Пример ресторанов
        self.insert_example()

    def insert_example(self):
        example_restaurants = [
            "Плаза",
            "Айва",
            "Тайская кафешка",
            "Хинкальная",
            "Бургерная",
            "Караоке",
            "Тейсти",
            "Голодаем без обеда",
        ]
        self.text_area.insert("1.0", "\n".join(example_restaurants))

    def random_choice(self):
        text = self.text_area.get("1.0", tk.END).strip()
        restaurants = [r.strip() for r in text.split("\n") if r.strip()]

        if not restaurants:
            messagebox.showwarning("Внимание", "Список ресторанов пуст!")
            return

        chosen = random.choice(restaurants)
        self.result_label.config(text=f"🎉 Сегодня идём в: {chosen}!")

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        self.result_label.config(text="")

    def run(self):
        self.window.mainloop()


# Запуск программы
if __name__ == "__main__":
    app = RestaurantRandomizer()
    app.run()