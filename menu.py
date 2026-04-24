dishes = []
CATEGORIES = ["Перші страви", "Другі страви", "Салати", "Десерти", "Напої", "Інше"]

def show_menu():
    print("\n╔══════════════════════════════╗")
    print("║       МЕНЮ РЕСТОРАНУ         ║")
    print("╠══════════════════════════════╣")
    print("║ 1. Додати страву             ║")
    print("║ 2. Редагувати страву         ║")
    print("║ 3. Видалити страву           ║")
    print("║ 4. Показати загальну ціну    ║")
    print("║ 5. Показати всі страви       ║")
    print("║ 6. Показати страви по катег. ║")
    print("║ 0. Вийти                     ║")
    print("╚══════════════════════════════╝")
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
    print("\nКатегорії:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    while True:
        try:
            cat_choice = int(input("Оберіть категорію (номер): "))
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1]
                break
            else:
                print("Невірний номер категорії.")
        except ValueError:
            print("Введіть число.")
    dishes.append({"name": name, "description": description, "price": price, "category": category})
    print(f"✓ Страву '{name}' успішно додано!")

def find_dish_by_name(name):
    for dish in dishes:
        if dish["name"].lower() == name.lower():
            return dish
    return None

def edit_dish():
    if not dishes:
        print("\nМеню порожнє.")
        return
    name = input("\nНазва страви для редагування: ").strip()
    dish = find_dish_by_name(name)
    if not dish:
        print(f"Помилка: страву '{name}' не знайдено.")
        return
    print(f"\nРедагування: {dish['name']}")
    print("  1. Ціну  2. Опис  3. Категорію")
    edit_choice = input("Що змінити: ").strip()
    if edit_choice == "1":
        while True:
            try:
                new_price = float(input("Нова ціна: "))
                if new_price < 0:
                    print("Від'ємна ціна неприпустима.")
                else:
                    dish["price"] = new_price
                    print("✓ Ціну оновлено!")
                    break
            except ValueError:
                print("Введіть число.")
    elif edit_choice == "2":
        dish["description"] = input("Новий опис: ").strip()
        print("✓ Опис оновлено!")
    elif edit_choice == "3":
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"  {i}. {cat}")
        while True:
            try:
                c = int(input("Нова категорія: "))
                if 1 <= c <= len(CATEGORIES):
                    dish["category"] = CATEGORIES[c - 1]
                    print("✓ Категорію оновлено!")
                    break
            except ValueError:
                pass
    else:
        print("Невірний вибір.")

def show_dishes():
    if not dishes:
        print("\nМеню порожнє.")
        return
    print(f"\n--- СПИСОК СТРАВ (усього: {len(dishes)}) ---")
    print("┌──────┬──────────────────┬──────────────┬───────────┬───────────┐")
    print("│  №   │ Назва            │ Опис         │ Ціна, грн │ Категорія │")
    print("├──────┼──────────────────┼──────────────┼───────────┼───────────┤")
    for i, dish in enumerate(dishes, 1):
        name = dish["name"][:16].ljust(16)
        desc = dish["description"][:12].ljust(12)
        price = f"{dish['price']:.2f}".rjust(9)
        cat = dish.get("category", "—")[:9].ljust(9)
        print(f"│ {str(i).ljust(4)} │ {name} │ {desc} │ {price} │ {cat} │")
    print("└──────┴──────────────────┴──────────────┴───────────┴───────────┘")

def show_by_category():
    if not dishes:
        print("\nМеню порожнє.")
        return
    all_cats = sorted(set(d.get("category", "Інше") for d in dishes))
    print("\n--- СТРАВИ ПО КАТЕГОРІЯХ ---")
    for cat in all_cats:
        cat_dishes = [d for d in dishes if d.get("category", "Інше") == cat]
        print(f"\n  [{cat}] ({len(cat_dishes)} шт.)")
        for d in cat_dishes:
            print(f"    • {d['name']} — {d['price']:.2f} грн  ({d['description']})")

def main():
    while True:
        show_menu()
        choice = input("Оберіть дію: ").strip()
        if choice == "1":
            add_dish()
        elif choice == "2":
            edit_dish()
        elif choice == "3":
            print("[Видалення страви - у розробці]")
        elif choice == "4":
            print("[Загальна ціна - у розробці]")
        elif choice == "5":
            show_dishes()
        elif choice == "6":
            show_by_category()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()
