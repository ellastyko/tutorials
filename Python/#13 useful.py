# Here I`ll show you some useful funcs 

# map // zip
def map_example(i):
    return i+5

def main():
    ###  zip  ### 
    numbers = [1, 2, 3]
    letters = ['a', 'b', 'c', 'd']
    zipped = zip(numbers, letters) # Объеденяет в список элементы имеющие один номер в списке
    print(list(zipped)) # [(1, 'a'), (2, 'b'), (3, 'c')]


    ###  map  ###
    nums = [5, 6, 7]
    res = map(map_example, nums) # Вызывает функцию для каждого элемента списка
    print(list(res)) # numbers = [1, 2, 3]
    


if __name__ == '__main__':
    main()