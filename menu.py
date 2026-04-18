dishes = []

def show_menu():
    print("\n╔══════════════════════════╗")
    print("║    МЕНЮ РЕСТОРАНУ        ║")
    print("╠══════════════════════════╣")
    print("║ 1. Додати страву         ║")
    print("║ 2. Редагувати страву     ║")
    print("║ 3. Видалити страву       ║")
    print("║ 4. Показати загальну ціну║")
    print("║ 5. Показати всі страви   ║")
    print("║ 0. Вийти                 ║")
    print("╚══════════════════════════╝")

def add_dish():
    print("\n--- Додавання страви ---")
    name = input("Назва страви: ").strip()
    if not name:
        print("Помилка: назва не може бути порожньою.")
        return

    description = input("Опис страви: ").strip()

    while True:
        try:
            price = float(input("Ціна (грн): "))
            if price < 0:
                print("Помилка: ціна не може бути від'ємною.")
            else:
                break
        except ValueError:
            print("Помилка: введіть числове значення.")

    dish = {"name": name, "description": description, "price": price}
    dishes.append(dish)
    print(f"✓ Страву '{name}' успішно додано!")

def show_dishes():
    if not dishes:
        print("\nМеню порожнє. Додайте страви.")
        return
    print("\n┌─────────────────────────────────────────────────────┐")
    print("│                  СПИСОК СТРАВ                      │")
    print("├──────┬──────────────────┬──────────────┬───────────┤")
    print("│  №   │ Назва            │ Опис         │ Ціна, грн │")
    print("├──────┼──────────────────┼──────────────┼───────────┤")
    for i, dish in enumerate(dishes, 1):
        name = dish["name"][:16].ljust(16)
        desc = dish["description"][:12].ljust(12)
        price = f"{dish['price']:.2f}".rjust(9)
        print(f"│ {str(i).ljust(4)} │ {name} │ {desc} │ {price} │")
    print("└──────┴──────────────────┴──────────────┴───────────┘")

def main():
    while True:
        show_menu()
        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            add_dish()
        elif choice == "2":
            print("[Редагування страви - у розробці]")
        elif choice == "3":
            print("[Видалення страви - у розробці]")
        elif choice == "4":
            print("[Загальна ціна - у розробці]")
        elif choice == "5":
            show_dishes()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()