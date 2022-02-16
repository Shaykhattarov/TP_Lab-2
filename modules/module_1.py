import numpy as np


def max_energy_kcal(data):
    max_el = data[0]
    for row in data:
        if row[3] > max_el[3] or (row[3] == max_el[3] and str(max_el[1]) < str(row[1])):
            max_el = row
    return max_el


def max_sugar(data):
    max_el = data[0]
    for row in data:
        if max_el[9] == row[9]:
            continue
    if max_el[9] < row[9]:
        max_el = row
    return max_el


def max_protein(data):
    max_el = data[0]
    for row in data:
        if row[4] == max_el[4]:
            continue
        if row[4] > max_el[4]:
            max_el = row
    return max_el


def max_vitamin_c(data):
    max_el = data[0]
    for row in data:
        if row[20] > max_el[20]:
            max_el = row
    return max_el


def main():
    table = np.genfromtxt("./data/ABBREV.csv", delimiter=";", dtype=None, names=True, encoding="utf-8")

    max_kcal_array = max_energy_kcal(table)
    max_sugar_array = max_sugar(table)
    max_protein_array = max_protein(table)
    max_vitamin_c_array = max_vitamin_c(table)

    print("1. Самый каллорийный продукт: " + str(max_kcal_array[1]))
    print("2. Самый полезный по содержанию сахара продукт: " + str(max_sugar_array[1]))
    print("3. Самый протеино-накаченный продукт: " + str(max_protein_array[1]))
    print("4. Самый богатый витамином С продукт: " + str(max_vitamin_c_array[1]))
