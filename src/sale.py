from src.read_data import read_file


def sale():

    data = read_file()
    i = 0
    sale_list = []

    while i < len(data):
        lines = data[i]['lines']
        j = 0
        while j < len(lines):
            if 'discount_percentage' in lines[j]:
                sale_list.append(round((lines[j]['discount_percentage']/100) * lines[j]['unit_price_without_vat'], 3))
                j += 1
            else:
                j += 1
        i += 1

    sale_sum = sum(sale_list) 
    return sale_sum