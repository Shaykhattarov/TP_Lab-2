from modules import module_1 as m1
from modules import module_2 as m2
from modules import module_3 as m3

if __name__ == "__main__":
    print("Ну шо? Надо работать! Какой модуль запустим?", end=" ")
    mod = input()
    if mod == "1":
        print("Первый так первый, лан че. Держи ответ: ")
        m1.main()
    if mod == "2":
        print("Ну значит второй, да?")
        m2.main()
    if mod == "3":
        m3.main()

