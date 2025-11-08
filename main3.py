import re
user_data={}
while True:
    fio=input("введите имя фамилию отчество")
    pattern =re.compile(r"^[А-Я][а-яё]*\s+[А-Я][а-яё]*\s+[А-Я][а-яё]*$")
    if pattern.match(fio):
        print("ваше имя фамилия отчество добавлено")
        user_data['фио'] =fio
        break
    else:
        print("ведите нормальное фио")
while True:
    phone_pattern = re.compile(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$')
    phone = input("введите номер телефона")
    if phone_pattern.match(phone):
        user_data['телефон'] =phone
        break
    else:
        print("вы вели неправильный номер")
while True:
    email_patter = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    email_user = input("введите почту")
    if email_patter.match(email_user):
        user_data['email']=email_user
        break
    else:
        print("вы вели неправильную почту")

