import numpy as np

<<<<<<< Updated upstream
def main():
    pass
=======

def generation(line):
    line = np.insert(np.append(line, np.array([0, 0])), 0, np.array([0, 0]))
    result_arr = np.array([], int)
    for i in range(1, len(line) - 1):
        if line[i - 1] == "0" and line[i] == "0" and line[i + 1] == "0":
            result_arr = np.append(result_arr, "0")
        elif line[i - 1] == "1" and line[i] == "1" and line[i + 1] == "0":
            result_arr = np.append(result_arr, "0")
        elif line[i - 1] == "1" and line[i] == "0" and line[i + 1] == "1":
            result_arr = np.append(result_arr, "0")
        elif line[i - 1] == "1" and line[i] == "0" and line[i + 1] == "0":
            result_arr = np.append(result_arr, "1")
        elif line[i - 1] == "0" and line[i] == "1" and line[i + 1] == "1":
            result_arr = np.append(result_arr, "1")
        elif line[i - 1] == "0" and line[i] == "1" and line[i + 1] == "0":
            result_arr = np.append(result_arr, "1")
        elif line[i - 1] == "0" and line[i] == "0" and line[i + 1] == "1":
            result_arr = np.append(result_arr, "1")
        elif line[i - 1] == "1" and line[i] == "1" and line[i + 1] == "1":
            result_arr = np.append(result_arr, "0")
        else:
            pass
    return result_arr


def main():
    print("Модуль_2 - Работаем!")
    line = input().split()
    line = np.array([char for char in line])
    for i in range(10):
        line = generation(line)
        print(line)
>>>>>>> Stashed changes
