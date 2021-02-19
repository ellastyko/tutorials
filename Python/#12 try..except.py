
def main():

    ###  Try...except  ###

    try:
        a = input("Введите первое число: ")
        b = input("Введите второе число: ")
        print("Результат: ", int(a)/int(b))
    except ValueError:
        print("Пожалуйста, вводите только числа")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except:
        print("Undefined Error")
    else:
        print("It`s ok")  # Выполняется при положительном результате
    finally:
        print("finally") # finally - Выполняется внезависимости от результата
    


if __name__ == '__main__':
    main()