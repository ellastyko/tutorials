# Python Basics

def main():
   
    # Types of data
       
    type(True)      # bool 
    type(1)         # int
    type(1.3)       # float
    type('string')  # str 
    type(3j)        # *complex



    ## *complex ##
    
    c1 = complex(5, 3)
    # or
    c2 = 5 + 3j

    print(c1.real) # 5
    print(c1.imag) # 3



    ###  init and input / output  ###
    name, age = 'vadik', 15
    print(f'Hello {name}, your age {age}')

    # output using .format
    month, year = input("Enter month: "), int(input("Enter year: "))
    print('Hello {}, your age {}' .format(month, year))



    ###  if else  ###
    a, b = 3, '3'
    if a is not b: # Мы не можем сравнить цифру и строку
        pass       # поэтому используем данный операнд
    elif a == b:
        pass
    elif a != 3 or b != '3':
        pass
    elif a == 3 and b is '3':
        pass
    else: 
        pass






# Сработает если файл не является импортируемым модулем
if __name__ == '__main__':
    main()