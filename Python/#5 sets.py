# Python sets

def main():
    sets = set('New text')
    my_set1 = {1, 2, 3, 4, 5} # Инициализация множества
    my_set2 = set('Hello world') # Создания множества из итерируемого объекта 
                                    # {'r', 'o', 'e', 'h', 'd', 'w', 'l', ' '}
    my_set3 = {x for x in range(10)} # Генератор множеств

    sets.add('END')   

    sets.difference(my_set2) # Возвр. множество элементов sets, которые не входят во множество my_set2
    
    sets.intersection(my_set2) # Возвр. множество элементов sets, которые входят во множество my_set2

    sets.update(my_set2) # Обновляет множество
    sets.union(my_set2) # Возвращает объедененное множество


    sets.difference_update(my_set2) # При использовании _update Лишние элементы удаляются
    
    # More: https://devman.org/qna/11/chem-otlichajutsja-list-tuple-i-set-zachem-oni-nuzhny/
   
    

if __name__ == '__main__':
    main()