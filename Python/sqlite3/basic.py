### Database in Python ### 
import sqlite3
PATH = 'tutorials/Python/sqlite3/data.db'

def main():
    # Создаем соединение с нашей базой данных
    # В нашем примере у нас это просто файл базы
    db = sqlite3.connect(PATH)
    # Создаем курсор - это специальный объект который делает запросы и получает их результаты
    sql = db.cursor()
    

    # DB init
    try:
        sql.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, login TEXT, password TEXT, name TEXT)""")
        # Или если таблиц много используя отдельный sql файл
        # with open('tutorials/Python/sqlite3/script.sql', 'r') as fd:
        #     script = fd.read()
        #     sql.executescript(script)
    except:
        print('Can`t open db')
        return 1
    else:
        db.commit()

    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    name = input("Введите имя: ")
    status = input("Введите act: ")

    # Set data
    if status == "signup":
        sql.execute(f"SELECT login FROM users WHERE login='{login}'")
        if sql.fetchone() == None:
            print("Registration...")
            sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (None, login, password, name))
            db.commit()
            print("Successfull registration")
        else:
            print("This login isn`t available")
    # Check data
    elif status == "signin":
        sql.execute(f"SELECT login FROM users WHERE login='{login}'")
        if sql.fetchone() == None:
            print("This account doesn`t exist")
        else:
            print("Welcome in your account")
            for value in sql.execute(f"SELECT * FROM users WHERE login='{login}'"):
                print(value)
    # Get data from database
    elif status == "get":
        sql.execute(f"SELECT login FROM users WHERE login='{login}'")
        if sql.fetchone == None:
            print("This account doesn`t exist")
        else:
            sql.execute(f"SELECT * FROM users WHERE login='{login}'")
            mass = sql.fetchall()
            print(mass)
            # mass = sql.fetchone()
            # print(mass[0][0], mass[0][1], mass[0][2], mass[0][3])
    # Update name 
    elif status == "set":
        sql.execute(f"SELECT login FROM users WHERE login='{login}'")
        # If user isn`t exist
        if sql.fetchone == None:
            print("This account doesn`t exist")
        else:
            # Confortable way to print data
            [print(str(i)) for i in sql.execute(f"SELECT * FROM users WHERE login='{login}'")]
            print("Ready for update")

            sql.execute(f"UPDATE users SET name='{name}' WHERE login='{login}'")
            sql.execute(f"SELECT * FROM users WHERE login='{login}'")
            mass = sql.fetchall()
            print(mass)
            db.commit()
    else:
        pass

    # Не забываем закрыть соединение с базой данных
    sql.close()


if __name__ == '__main__':
    main()

# More: 
# https://habr.com/ru/post/321510/
# https://www.tutorialspoint.com/sqlite/sqlite_python.htm