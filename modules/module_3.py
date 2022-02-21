import numpy as np
import os
import json


def get_files_size(dir_path):
    data = dict()
    try:
        filenames = os.listdir(dir_path)
        for filename in filenames:
            filesize = str(os.stat(f'{dir_path}/{filename}').st_size / 1024)
            data[filename] = f'{filesize} Kbyte'
    except Exception as err:
        print(err)
        return dict(result=None, error=err.errno)
    except FileNotFoundError as err:
        print(err)
        return dict(result=None, error=err.errno)
    except OSError as err:
        print(err)
        return dict(result=None, error=err.errno)
    else:
        return dict(result=data, error=None)


def sort_csv_by_name(data):
    sorted_names = np.argsort(data[:, 1], kind='quicksort')
    data = data[sorted_names]
    return data


def sort_csv_by_int(data):
    sorted_old = np.argsort(data[:, 3], kind='quicksort')
    data = data[sorted_old]
    return data


def filter_csv_by_sep(data):
    print("Введите число больше которого должен быть возраст:", end=" ")
    border = float(input())
    arr = []
    for row in data:
        if float(row[3]) >= border:
            arr.append(row)
    result = np.array(arr)
    return result


def get_CSV_files(csv_filename):
    print("На поиск файла в системе требуется время. "
          "Для успешного поиска файла нужно указать правильную примерную стартовую директорию.")
    print("Укажите стартовую директорию:", end=" ")
    start_dir = input()
    try:
        filepath = find_filepath(start_dir=start_dir, filename=csv_filename)
        if filepath == "":
            raise FileNotFoundError
    except FileNotFoundError as err:
        print(err)
        return dict(result=None, error=err.errno)

    try:
        table = np.genfromtxt(filepath, delimiter=";", dtype='>U8', skip_header=1, encoding=None)
        sort_name = sort_csv_by_name(table).tolist()
        sort_int = sort_csv_by_int(table).tolist()
        sort_req = filter_csv_by_sep(table).tolist()
        data = dict(namesort=sort_name, oldsort=sort_int, paramsort=sort_req)
        return dict(result=data, error=None)
    except NameError as err:
        print(err)
        return dict(result=None, error=err.errno)
    except OSError as err:
        print(err)
        return dict(result=None, error=err.errno)


def find_filepath(start_dir, filename):
    filepath = ""
    for root, dir, filenames in os.walk(start_dir):
        for file in filenames:
            if file == filename:
                print(filepath)
                filepath = str(os.path.join(root, file))
                break
    return filepath


def main():
    result = dict()

    print("1.Введите путь к директории:", end=" ")
    dir_path = input()
    data = get_files_size(dir_path)
    if data['error'] is None:
        result["Task 1"] = data['result']
    else:
        result["Task 1"] = 'Error'

    print("2.Введите имя csv-файла:", end=" ")
    filename = input()
    data = get_CSV_files(filename)
    if data["error"] is None:
        result['Task 2'] = data['result']
    else:
        result["Task 2"] = 'Error'

    with open('data/result.json', "w", encoding='utf-8') as file:
        try:
            file.write(json.dumps(result, ensure_ascii=False))
        except TypeError as err:
            print(err)

    try:
        os.replace('data/result.json', 'result.json')
        os.remove(f'data/{filename}')
    except FileNotFoundError as err:
        exit(err)
    except OSError as err:
        exit(err)
    except Exception as err:
        exit(err)
