import datetime
import time

def main():
    
    ### Module time ###
    time.time() # time in seconds
    
    t = time.localtime() # object
    print(t.tm_year)    # 2021
    print(t.tm_mon)     # 2 (febr)
    print(t.tm_mday)    # 20
    print(t.tm_wday)    # 5 (friday)
    print(t.tm_hour)    # hour
    print(t.tm_min)    # min
    print(t.tm_sec)    # sec
    print(t.tm_gmtoff) # +7200 seconds by greenwich

    ### Module datetime ###

    datetime.datetime.now() # Other way to get local time 
    date = datetime.datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)


    print(date)         # 2021-02-20 12:34:19.261922

    print(date.strftime("%Y")) # 2021
    print(date.strftime("%B")) # February
    print(date.strftime("%X")) # 12:34:53
    print(date.strftime("%H")) # 12
    print(date.strftime("%M")) # 34
    # More variants how to print date: https://www.w3schools.com/python/python_datetime.asp
    
    ### Difference ###
    # The first module using in counting                * type = <class 'int'>
    # The second one using to show date to user         * type = <class 'str'>



if __name__ == '__main__':
    main()