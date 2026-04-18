dishes = []
CATEGORIES = ["Перші страви", "Другі страви", "Салати", "Десерти", "Напої", "Інше"]

def show_menu():
    print("\n╔════════════════════════════════╗")
    print("║       🍽  МЕНЮ РЕСТОРАНУ        ║")
    print("╠════════════════════════════════╣")
    print("║  1. Додати страву              ║")
    print("║  2. Редагувати страву          ║")
    print("║  3. Видалити страву            ║")
    print("║  4. Загальна ціна              ║")
    print("║  5. Показати всі страви        ║")
    print("║  6. Страви по категоріях       ║")
    print("║  7. Ціна по категорії          ║")
    print("║  8. Сортування за ціною        ║")
    print("║  0. Вийти                      ║")
    print("╚════════════════════════════════╝")

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
            print("Введіть числове значення.")
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
                print("Невірний номер.")
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

def delete_dish():
    if not dishes:
        print("\nМеню порожнє - нічого видаляти.")
        return
    print("\n--- Видалення страви ---")
    print("  1. Видалити за назвою")
    print("  2. Видалити всі страви за категорією")
    del_choice = input("Оберіть: ").strip()
    if del_choice == "1":
        name = input("Назва страви для видалення: ").strip()
        dish = find_dish_by_name(name)
        if not dish:
            print(f"Страву '{name}' не знайдено.")
            return
        confirm = input(f"Видалити '{dish['name']}'? (так/ні): ").strip().lower()
        if confirm == "так":
            dishes.remove(dish)
            print(f"✓ Страву '{name}' видалено. Залишилось: {len(dishes)}")
        else:
            print("Видалення скасовано.")
    elif del_choice == "2":
        print("\nКатегорії:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"  {i}. {cat}")
        while True:
            try:
                cat_choice = int(input("Оберіть категорію: "))
                if 1 <= cat_choice <= len(CATEGORIES):
                    category = CATEGORIES[cat_choice - 1]
                    break
            except ValueError:
                pass
        to_delete = [d for d in dishes if d.get("category") == category]
        if not to_delete:
            print(f"У категорії '{category}' немає страв.")
            return
        confirm = input(f"Видалити {len(to_delete)} страв(и)? (так/ні): ").strip().lower()
        if confirm == "так":
            for d in to_delete:
                dishes.remove(d)
            print(f"✓ Видалено. Залишилось: {len(dishes)}")
        else:
            print("Скасовано.")

def show_dishes(dish_list=None, title="СПИСОК СТРАВ"):
    data = dish_list if dish_list is not None else dishes
    if not data:
        print("\nСписок порожній.")
        return
    print(f"\n--- {title} (усього: {len(data)}) ---")
    print("┌──────┬────────────────────┬──────────────────┬───────────┬──────────────┐")
    print("│  №   │ Назва              │ Опис             │ Ціна, грн │ Категорія    │")
    print("├──────┼────────────────────┼──────────────────┼───────────┼──────────────┤")
    for i, dish in enumerate(data, 1):
        name = dish["name"][:18].ljust(18)
        desc = dish["description"][:16].ljust(16)
        price = f"{dish['price']:.2f}".rjust(9)
        cat = dish.get("category", "—")[:12].ljust(12)
        print(f"│ {str(i).ljust(4)} │ {name} │ {desc} │ {price} │ {cat} │")
    print("└──────┴────────────────────┴──────────────────┴───────────┴──────────────┘")

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
            print(f"    • {d['name']:<20} {d['price']:>8.2f} грн   {d['description']}")

def total_price():
    if not dishes:
        print("\nМеню порожнє.")
        return
    total = sum(d["price"] for d in dishes)
    print(f"\n💰 Загальна вартість: {total:.2f} грн")
    print(f"   Кількість страв:   {len(dishes)}")
    print(f"   Середня ціна:      {total / len(dishes):.2f} грн")

def price_by_category():
    if not dishes:
        print("\nМеню порожнє.")
        return
    all_cats = sorted(set(d.get("category", "Інше") for d in dishes))
    print("\n--- ЦІНА ПО КАТЕГОРІЯХ ---")
    grand_total = 0
    for cat in all_cats:
        cat_dishes = [d for d in dishes if d.get("category", "Інше") == cat]
        cat_total = sum(d["price"] for d in cat_dishes)
        grand_total += cat_total
        print(f"  {cat:<20} {len(cat_dishes):>3} шт.  →  {cat_total:>9.2f} грн")
    print(f"  {'ВСЬОГО':<20} {len(dishes):>3} шт.  →  {grand_total:>9.2f} грн")

def sort_by_price():
    if not dishes:
        print("\nМеню порожнє.")
        return
    print("\n--- Сортування за ціною ---")
    print("  1. Від дешевих до дорогих")
    print("  2. Від дорогих до дешевих")
    sort_choice = input("Оберіть: ").strip()
    if sort_choice == "1":
        show_dishes(sorted(dishes, key=lambda d: d["price"]), "від дешевих до дорогих")
    elif sort_choice == "2":
        show_dishes(sorted(dishes, key=lambda d: d["price"], reverse=True), "від дорогих до дешевих")
    else:
        print("Невірний вибір.")

def main():
    print("Ласкаво просимо!")
    while True:
        show_menu()
        choice = input("Оберіть дію: ").strip()
        if choice == "1":
            add_dish()
        elif choice == "2":
            edit_dish()
        elif choice == "3":
            delete_dish()
        elif choice == "4":
            total_price()
        elif choice == "5":
            show_dishes()
        elif choice == "6":
            show_by_category()
        elif choice == "7":
            price_by_category()
        elif choice == "8":
            sort_by_price()
        elif choice == "0":
            print("\nДо побачення!")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()