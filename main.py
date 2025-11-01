def select(input_func):
    def output_func():
        print("="*50)
        input_func()
        print("=" *50)

    return output_func


regular_menu={
    'пиццы':{
        'Маргарита':{'цена': 450, 'описание': 'томатный соус, моцарелла, базилик'},
        'Пепперони':{'цена': 550, 'описание': 'томатный соус, моцарелла, пепперони'},
        'Гавайская':{'цена': 500, 'описание': 'томатный соус, моцарелла, ветчина, ананасы'},
        'Четыре сыра':{'цена': 600, 'описание': 'моцарелла, горгонзола, пармезан, чеддер'}
    },
    'напитки': {
        'Кола':120,
        'Фанта':120,
        'Сок':100,
        'Вода':80
    }
}
adult_menu = {
    'пиццы': {
        'Маргарита':{'цена': 650, 'описание': 'томатный соус, моцарелла, базилик (большая порция)'},
        'Пепперони':{'цена': 750, 'описание': 'томатный соус, моцарелла, пепперони (двойная порция)'},
        'Гавайская':{'цена': 700, 'описание': 'томатный соус, моцарелла, ветчина, ананасы (большая порция)'},
        'Четыре сыра':{'цена': 800, 'описание': 'моцарелла, горгонзола, пармезан, чеддер (двойная порция)'},
        'Острая':{'цена': 750, 'описание': 'томатный соус, моцарелла, салями, перец чили'}
    },
    'напитки': {
        'Кола':150,
        'Фанта':150,
        'Сок':120,
        'Вода':100
    }
}

topping={
    'сыр':50,
    'ветчина':70,
    'грибы':60,
    'оливки':40,
    'перец':50,
    'ананасы':80,
    'пепперони':90
}

user_data = {}
order = []
total_amount = 0
current_menu = {}

print("=== Добро пожаловать в пиццерию 'pizza hut'! ===")
user_data['фио'] = input("Введите ваше ФИО ")
while True:
    try:
        age = int(input("Введите ваш возраст "))
        if age > 0 and age < 120:
            user_data['возраст'] = age
            break
        else:
            print("Пожалуйста, введите корректный возраст!")
    except ValueError:
        print("Пожалуйста, введите число!")
print(f"\n=== Приветствуем,{user_data['фио']}!===")

if user_data['возраст'] >= 18:
    print("Вам доступно взрослое меню с увеличенными порциями!")
    current_menu = adult_menu
else:
    print("Вам доступно стандартное меню.")
    current_menu = regular_menu

print("\nНАШЕ МЕНЮ")
print("\nПИЦЦЫ")
for pizza, info in current_menu['пиццы'].items():
    print(f"{pizza}: {info['цена']} руб. - {info['описание']}")

print("\nНАПИТКИ")
for drink, price in current_menu['напитки'].items():
    print(f"{drink}: {price} руб.")


print("\n=== ОФОРМЛЕНИЕ ЗАКАЗА ===")

while True:
    print("\n1 - Выбрать готовую пиццу")
    print("2 - Создать кастомную пиццу")
    print("3 - Выбрать напиток")
    print("4 - Завершить заказ")

    choice = input("Выберите что хотите сделать ")

    if choice == '1':
        print("\n--- ГОТОВЫЕ ПИЦЦЫ ---")
        pizzas = list(current_menu['пиццы'].keys())

        for i, pizza in enumerate(pizzas, 0):
            info = current_menu['пиццы'][pizza]
            print(f"{i} {pizza} - {info['цена']} руб ({info['описание']})")

        try:
            pizza_choice = int(input("\nВыберите номер пиццы: "))
            if 0 <= pizza_choice < len(pizzas):
                selected_pizza = pizzas[pizza_choice]
                price = current_menu['пиццы'][selected_pizza]['цена']

                order.append({
                    'название': selected_pizza,
                    'цена': price,
                    'тип': 'пицца'
                })
                total_amount += price
                print(f"{selected_pizza} добавлена в заказ!")
            else:
                print("Неверный номер!")
        except ValueError:
            print("Пожалуйста, введите число!")
    elif choice == '3':
        print("\n--- НАПИТКИ ---")
        drinks = list(current_menu['напитки'].keys())

        for i, drink in enumerate(drinks, 1):
            price = current_menu['напитки'][drink]
            print(f"{i}. {drink} - {price} руб.")

        try:
            drink_choice = int(input("\nВыберите номер напитка: ")) - 1
            if 0 <= drink_choice < len(drinks):
                selected_drink = drinks[drink_choice]
                price = current_menu['напитки'][selected_drink]

                order.append({
                    'название': selected_drink,
                    'цена': price,
                    'тип': 'напиток'
                })
                total_amount += price
                print(f"{selected_drink} добавлен в заказ!")
            else:
                print("Неверный номер!")
        except ValueError:
            print("Пожалуйста, введите число!")

    elif choice == '4':
        if not order:
            print("Ваш заказ пуст! Добавьте что-нибудь.")
        else:
            break
    else:
        print("Неверный выбор!")

@select
def chek():
    print("ВАШ ЧЕК")
for i, item in enumerate(order, 1):
    print(f"{i}. {item['название']}: {item['цена']} руб.")
@select
def result_finish():
    print(f"ИТОГО: {total_amount} руб.")
result_finish()

# Оплата
print("\n=== ОПЛАТА ===")

while True:
    print("1- заказ собой")
    print("2- здесь")
    try:
        issuing_an_order = int(input())
        if issuing_an_order == 1:
            print("ваш заказ приготовиться и мы вам его пренесем")
        else:
            print("пресядьте за стол и подождите заказ")
    except ValueError:
        print("Пожалуйста,введите число!")

    print("1 - Оплата картой")
    print("2 - Оплата наличными")

    payment_choice = input("Выберите способ оплаты: ")

    if payment_choice == '1':
        print("\nОПЛАТА КАРТОЙ")
        card_number = input("Введите пинкод : ")
        print("Оплата прошла успешно!")
        break

    elif payment_choice == '2':
        print("\nоплата наличными")
        try:
            cash = int(input(f"Введите сумму наличных (итого:{total_amount}руб): "))

            if cash >= total_amount:
                change = cash - total_amount
                print(f"Оплата принята! Ваша сдача: {change} руб.")
                break
            else:
                print("Недостаточно средств!")
        except ValueError:
            print("Пожалуйста,введите число!")
    else:
        print("Неверный выбор!")
@select
def order_finish():
    print("ЗАКАЗ ПРИНЯТ! Приятного аппетита!")
    print(f"Спасибо,{user_data['фио']}, что выбрали нашу пиццерию! pizza hut")
order_finish()