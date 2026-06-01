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
        # elif answer == "2":
        #     show_tasks(todo_list.get_all_tasks())
        #     try:
        #         index = int(input("Введите номер задачи: ")) - 1
        #         todo_list.delete_task(index)
        #         print("\nЗадача успешно удалена ✓")
        #         todo_list.save()
        #     except ValueError:
        #         print("\nОшибка: введите число!")
        #     except IndexError:
        #         print("\nОшибка: задачи с таким номером нет!")
        # elif answer == "3":
        #     try:
        #         show_tasks(todo_list.get_all_tasks())
        #         index = int(input("Введите номер задачи: ")) - 1
        #         task = todo_list.tasks[index]
        #         task.mark_done()
        #         print(f"«{task.text}» ✓\nЗадача выполнена")
        #         todo_list.save()
        #     except ValueError:
        #         print("\nОшибка: введите число")
        #     except IndexError:
        #         print("\nОшибка: задачи с таким номером нет")
        # elif answer == "4":
        #     show_tasks(todo_list.tasks)
        # elif answer == "5":
        #     status = input("Показать выполненные? y/n: ")
        #     is_done = status == "y"
        #     show_tasks(todo_list.get_filtered_tasks(is_done))


if __name__ == "__main__":
    main()
