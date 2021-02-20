# How to write or read from file
import json

def main():
    dic = {
            'name': 'Vadim',
            'age': 18,
            'working': True
           }
           
    dic_json = json.dumps(dic)  # To json

    # 'r+' - read text and append
    # 'w+' - delete text and write new
    # 'a+' - read text and append


    with open('data.json', 'a+') as file:
        
        file.read()
        file.write(dic_json)



if __name__ == '__main__':
    main()