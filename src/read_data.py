import json


def read_file():
    with open('sales_data.json', encoding='utf-8') as file:
        # print(file.read())
        data = file.read()
        json_data = json.loads(data)
        return json_data