from src.read_data import read_file


def unique_products():

    data = read_file()
    i = 0
    unique_list = []

    while i < len(data):
        lines = data[i]['lines']
        j = 0
        while j < len(lines):
            if lines[j]['product'] in unique_list:
                j += 1
                pass
            else:
                unique_list.append(lines[j]['product'])
                j += 1
        i += 1
    uniques = len(unique_list)
    return uniques