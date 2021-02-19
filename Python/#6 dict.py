# Python dictionaries

def main():

    dic = {
            "name": "Vadim",
            "age": 18,
            "working": True
           }

    # Get value
    dic.get("name")  # Vadim
    dic['working']  # True

    # Change values
    dic['working'] = False
    dic.update({"name": "James", "age": 19})

    # Add new value
    dic.update({"job": "NURE"})

    # Delete values
    dic.pop("name")
    # If you want to delete dictionary use 'del dic'

    # Make copy (2 ways)
    dic_copy = dic.copy()
    dic_copy = dict(dic)

    # Insert dict-s in main dict.
    great_dict = {}
    great_dict.update({ 'dic_copy': dic_copy, 'dic': dic})

    # Emptify
    dic.clear()
    print(great_dict)
    
   
    

if __name__ == '__main__':
    main()