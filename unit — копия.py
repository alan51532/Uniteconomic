import tkinter as tk
# Создаем основное окно
root = tk.Tk()
# Устанавливаем заголовок окна
root.title("Мое окно")
# Устанавливаем размер окна
root.geometry("1350x300")  # Увеличиваем высоту окна для размещения всех полей
# Устанавливаем цвет фона
root.configure(bg='lightgreen')
# Создаем фрейм для верхнего ряда полей
frame_top = tk.Frame(root, bg='lightgreen')
frame_top.pack(pady=20)
# Создаем метки и поля ввода для верхнего ряда
labels_top = ["Дата и данные по партии", "единиц товара в грузе", "курс $ AliExpres", "цена по инвойсу $", "Полная сумма оплаты в руб"]
entries_top = []
for i in range(5):
    label = tk.Label(frame_top, text=labels_top[i], bg='lightgreen')  # Устанавливаем цвет фона меток
    label.grid(row=0, column=i, padx=5)  # Размещаем метки в сетке
    entry = tk.Entry(frame_top)
    entry.grid(row=1, column=i, padx=5)  # Размещаем поля ввода в сетке
    entries_top.append(entry)
# Создаем фрейм для нижнего ряда полей
frame_bottom = tk.Frame(root, bg='lightgreen')
frame_bottom.pack(pady=20)
# Создаем метки и поля ввода для нижнего ряда
labels_bottom = ["SKU", "цена за шт $", "шопинг общ $", "Доставка мск $", "ТТ до дома руб", "Поле 10", "Поле 11", "Поле 12"]
entries_bottom = []
for i in range(8):  # Изменяем диапазон на 8, так как убрали одно поле
    label = tk.Label(frame_bottom, text=labels_bottom[i], bg='lightgreen')  # Устанавливаем цвет фона меток
    label.grid(row=0, column=i, padx=5)  # Размещаем метки в сетке
    entry = tk.Entry(frame_bottom)
    entry.grid(row=1, column=i, padx=5)  # Размещаем поля ввода в сетке
    entries_bottom.append(entry)
# Функция для получения данных из полей ввода
def get_data():
    date_and_No = entries_top[0].get()  # № груза и дата
    number_of_SKUs = float(entries_top[1].get())  # единиц товара в грузе       
    dollars = float(entries_top[2].get())       # курс $
    invois_price = float(entries_top[3].get())  # цена по инвойсу вместе с шопинг $
    polnaya_summa = float(entries_top[4].get())  # общая сумма что была переведена за купоенный груз
    
    price_posredic = polnaya_summa - invois_price * dollars 
    sku = entries_bottom[0].get()        # SKU
    price_per_piece = float(entries_bottom[1].get())  # цена за шт $
    schonig = float(entries_bottom[2].get())    # шопинг общ $
    delivery = float(entries_bottom[3].get())   # Доставка мск $
    tt = float(entries_bottom[4].get())         # ТТ до дома руб
    force_majeure = entries_bottom[5].get()
    force_majeure1 = entries_bottom[6].get()
    force_majeure2 = entries_bottom[7].get()
    re = (price_per_piece + schonig / number_of_SKUs + delivery / number_of_SKUs) * dollars + tt / number_of_SKUs + price_posredic / number_of_SKUs
    re2 = round(re, 1)
    # Вывод данных в консоль
    print("Данные:")
    print(f"№ груза, SKU и дата: {date_and_No}")
    print(f"Курс доллара на Алиэкспресс: {dollars:.1f}")
    print(f"Количество мест в грузе: {number_of_SKUs:.1f}")
    print(f"SKU: {sku}")
    print(f"Цена за шт $: {price_per_piece:.1f}")
    print(f"Шопинг общ $: {schonig:.1f}")
    print(f"Доставка мск $: {delivery:.1f}")
    print(f"ТТ до дома руб: {tt:.1f}")
    print(f"Поле 10: {force_majeure}")
    print(f"Поле 11: {force_majeure1}")
    print(f"Поле 12: {force_majeure2}")
    print(f"Вы заплатили посреднику {price_posredic:.1f}")
    print(f"Итог: {re2:.1f}")
# Кнопка для получения данных
submit_button = tk.Button(root, text="Получить данные", command=get_data)
submit_button.pack(pady=20)
# Запускаем главный цикл приложения
root.mainloop()

