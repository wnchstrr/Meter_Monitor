def show_menu():
    """Показывает меню"""
    print("0. Выход")
    print("1. Добавить показания")
    print("2. Удалить показания")
    print("3. Показать все показания")
    print("4. Фильтр по периоду")
    print("5. Показать график")


def get_choice():
    """Принимает выбор пользователя"""
    return input("Выберите пункт из меню: ")


def show_readings(readings: list[Reading]) -> None:
    if not readings:
        print("Показаний нет.")
        return
    for index, reading in enumerate(readings, start=1):
        print(f"{index}. [{reading.meter_type}, {reading.value}, {reading.date}]")
