import numpy as np
import os


def get_files_size(dir_path):
    files_size = []
    try:
        for dirpath, dirnames, filenames in os.walk(dir_path):
            for file in filenames:
                file_dir = dir_path + "/" + file
                files_size.append(file + " - " + str(os.stat(file_dir).st_size / 1024) + " Кбайт")
        if not files_size:
            raise Exception("В данной директории нет файлов или её не существует!")
    except NotImplementedError as err:
        return err
    except OSError as err:
        return err
    except WindowsError as err:
        return err
    except Exception as err:
        return err
    else:
        return files_size


def insertion(data):
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def sort_csv_by_name(data):
    names_arr = np.array([])
    for row in data:
        names_arr = np.append(names_arr, row[1])
    sort_names = np.sort(names_arr)
    print(sort_names)


def get_CSV_files(dir_path):
    sort_result_name = np.array([])
    sort_result_int = np.array([])
    sort_result_req = np.array([])
    try:
        for dirpath, dirnames, filenames in os.walk(dir_path):
            for file in filenames:
                if file == "PET_DATA.csv":
                    file_dir = dir_path + "/" + file
                    csv_data = np.genfromtxt(file_dir, delimiter=";", dtype=None, names=True, encoding=None)
                    sort_csv_by_name(csv_data)
                    # sort_csv_by_int(csv_data)
                    # sort_csv_by_req(csv_data, kwarg)
    except NotImplementedError as err:
        return err


def main():
    dir_path = input()
    get_CSV_files(dir_path)
    res_arr = get_files_size(dir_path)
    if type(res_arr) != Exception:
        for arr in res_arr:
            print(arr)
    else:
        print(res_arr)
