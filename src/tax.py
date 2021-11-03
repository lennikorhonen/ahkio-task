from src.read_data import read_file


def vat():

    data = read_file()
    i = 0
    vat_list = []

    while i < len(data):
        lines = data[i]['lines']
        j = 0
        while j < len(lines):
            vat_list.append(round((lines[j]['vat_percentage']/100) * lines[j]['unit_price_without_vat'], 3))
            j += 1
        i += 1

    vat_sum = sum(vat_list) 
    return vat_sum
