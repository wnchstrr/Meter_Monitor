from meter_monitor.storage import JsonStorage
from meter_monitor.ui import get_choice, show_readings, show_menu
from datetime import date
from meter_monitor.models import Reading


def main():
    storage = JsonStorage("meter.json")
    readings = storage.load()
    while True:
        print()
        show_menu()
        answer = get_choice()
        if answer == "0":
            print("Благого дня!")
            break
        elif answer == "1":
            meter_type = input("Тип счётчика (электричество/вода/газ:)\n ")
            value = input("Показание: ")
            data_str = input("Дата (ГГГГ-ММ-ДД): ")
            reading = Reading(
                meter_type=meter_type,
                value=float(value),
                date=date.fromisoformat(data_str),
            )
            readings.append(reading)
            print("\nПоказания успешно добавлены")
            print(f"Текущие показания: {meter_type} = {value}\nДата: {data_str}")
            storage.save(readings)
        elif answer == "2":
            show_readings(readings)
            try:
                index = int(input("Выберите показания: ")) - 1
                readings.pop(index)
                storage.save(readings)
                print("\nПоказания удалены ✓")
            except ValueError:
                print("\nОшибка: введите число!")
            except IndexError:
                print("\nОшибка: показаний с таким номером нет!")
        elif answer == "3":
            show_readings(readings)
        elif answer == "4":
            print("В разработке")
        elif answer == "5":
            print("В разработке")


if __name__ == "__main__":
    main()
