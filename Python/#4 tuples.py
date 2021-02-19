# Python tuple(Cortege)

def main():

    # Варианты создания кортежа
    cortege1 = ()
    cortege2 = tuple("vadik")
    cortege3 = (1, 2, ['a','b'], 4, 5) # Инициализация кортежа
    cortege4 = tuple(2**x for x in [0, 1, 2, 3]) # Генератор кортежей
    
    
    cortege2.count('v') # Возвр. кол-во элементов с указанным значением
    cortege2.index('a') # Возвр. индекс указанного элемента


    

if __name__ == '__main__':
    main()