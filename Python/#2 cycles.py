# Python tutorial 

def main():

    List = [ 5, 6, 7, 8, 9]

    # Стандартный перебор элементов
    for i in List:
        print(i)
    else:       # Дополнительный блок выполняется после окончания цикла
        pass    # Не сработает при использовании break

    # Итерация с помощью range(start point, list, step)
    for i in range(1, len(List), 1):
        print(List[i])
    
    # Итерация с помощью enumerate(list, start point) 
    for i, value in enumerate(List):    # step by default = 0
        print(i, value)
    
    while True:
        # code
        break
        continue    # Переход на след. итерацию
        pass    # In Python programming, the pass statement is a null statement. 
                # The difference between a comment and a pass statement in Python 
                # is that while the interpreter ignores a comment entirely, pass is not ignored. 
                # However, nothing happens when the pass is executed.
    
    

if __name__ == '__main__':
    main()