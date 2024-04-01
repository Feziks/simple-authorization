register_login = input("Придумайте логин: ")
register_password = input("Придумайте пароль: ")

count = 0
while count <= 3:
    login = input("Ведите логин: ")
    password = input("Введите пароль: ")
    count += 1
    if (login != register_login or password != register_password):
        print('Неправильный логин или пароль, осталось попыток :', 4-count)
    else:
        count =+ 3
        print('Добро пожаловать,',register_login)
        break