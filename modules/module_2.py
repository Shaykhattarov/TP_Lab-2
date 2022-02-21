import numpy as np


def generation(line):
    result_arr = np.array([], int)
    for i in range(1, len(line) - 1):
        if line[i - 1] == "0" and line[i] == "0" and line[i + 1] == "0":
            result_arr = np.append(result_arr, 0)
        elif line[i - 1] == "1" and line[i] == "1" and line[i + 1] == "0":
            result_arr = np.append(result_arr, 0)
        elif line[i - 1] == "1" and line[i] == "0" and line[i + 1] == "1":
            result_arr = np.append(result_arr, 0)
        elif line[i - 1] == "1" and line[i] == "0" and line[i + 1] == "0":
            result_arr = np.append(result_arr, 1)
        elif line[i - 1] == "0" and line[i] == "1" and line[i + 1] == "1":
            result_arr = np.append(result_arr, 1)
        elif line[i - 1] == "0" and line[i] == "1" and line[i + 1] == "0":
            result_arr = np.append(result_arr, 1)
        elif line[i - 1] == "0" and line[i] == "0" and line[i + 1] == "1":
            result_arr = np.append(result_arr, 1)
        elif line[i - 1] == "1" and line[i] == "1" and line[i + 1] == "1":
            result_arr = np.append(result_arr, 0)
        else:
            pass

    return result_arr


def main():
    print("Модуль_2 - Работаем!")
    #line = input().split()
    line_str = "1001000101111100000101111001011011101101101111110111110000000000000011000001011001100011111101001001"
    #line = [char for char in line_str]
    line = np.array([char for char in line_str])
    for i in range(3):
        print(generation(line))
