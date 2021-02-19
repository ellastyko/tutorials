# Converting dictionaries to json
import json

def main():

    dic = {
            'name': 'Vadim',
            'age': 18,
            'working': True
           }

    dic_json = json.dumps(dic)  # To json

    json.loads(dic_json)    # Back to dictionary



if __name__ == '__main__':
    main()