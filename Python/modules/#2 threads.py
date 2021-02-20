import threading
 
def update_total(name, age):

    threading.current_thread() # Cмотрим, какой поток вызвал функцию
    threading.active_count() # Получаем экземпляры класса Thread (Количество потоков ??)
    threading.enumerate() # Получаем список работающих потоков
    print(f'Hello {name}, your age {age}')


def main():

    for i in range(5):
        my_thread = threading.Thread(target=update_total, args=('Vadik', 18,))  
        # my_thread.setName('Thr') # Даем потоку имя
        # my_thread.getName() # Thread-1
        my_thread.start() # Начинает работу потока

    my_thread.join() # Ждет пока поток закончит работу   




if __name__ == '__main__':
    main()