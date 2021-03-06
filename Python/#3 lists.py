# Python lists

def main():

    List = []
    # OR
    List2 = list()

    # Можно заполнять с помощью обычного цикла и использовать как обычный массив
    # Также можно использовать специальные функции

    # Добавить число в конец списка
    List.append(5) 
    List2.append('zac')

    # Сортирует числа и строки 
    List.sort()

    # Добавить список к списку
    List.extend(List2)

    # Вставить число в определенное место (позиция, значение)
    List.insert(1, 1337) 

    # Удалить n-ный элемент
    List.pop(0) 

    # Удалить элемент по значению
    List.remove(1337)

    # Проверка на наличие элемента в списке
    List.__contains__(1337)  # True
    # Или
    if 1337 in List:
        print('1337 in list')

    # В списке остаются только str элементы
    List.__str__()    

    # Инверсия элементов в списке
    List.reverse() 

    # Возвращает индекс элемента по значению на указанном участке
    List.index('zac', 0, len(List)) 

    print(List)

    

    # Очистить список
    List.clear()
    

if __name__ == '__main__':
    main()