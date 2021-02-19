# Python Basics

def main():
    
    # Types of data
       
    type(True)      # bool 
    type(1)         # int
    type(1.3)       # float
    type('string')  # str 
    type(3j)        # *complex



    ## *complex ##
    
    c = complex(5, 3)
    # or
    k = 5 + 3j

    print(k.real) # 5
    print(k.imag) # 3



    #init and input / output

    name, age = 'vadik', 15
    print(f'Hello {name}, your age {age}')

    # output using .format

    month, year = input("Enter month: "), int(input("Enter year: "))
    print('Hello {}, your age {}' .format(month, year))



# Сработает если файл не является импортируемым модулем
if __name__ == '__main__':
    main()