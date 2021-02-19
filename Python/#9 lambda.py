# Lambda functions

def main():
    # Lambda - короткие однострочные функции (синт. сахар)
    a = lambda i, j:  i + j
    b = lambda i:  i ** i

    a(3, 4) # 7
    b(3) # 27



if __name__ == '__main__':
    main()