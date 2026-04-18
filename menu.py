dishes = []

def show_menu():
    print("\n===== МЕНЮ РЕСТОРАНУ =====")
    print("1. Додати страву")
    print("2. Редагувати страву")
    print("3. Видалити страву")
    print("4. Показати загальну ціну")
    print("0. Вийти")
    print("==========================")

def main():
    while True:
        show_menu()
        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            print("[Додавання страви — у розробці]")
        elif choice == "2":
            print("[Редагування страви — у розробці]")
        elif choice == "3":
            print("[Видалення страви — у розробці]")
        elif choice == "4":
            print("[Загальна ціна — у розробці]")
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()