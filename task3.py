seasons = ["Весна", "Лето", "Осень", "Зима"]
monthnumb = int(input("введите номер месяца: "))
if 3 <= monthnumb <= 5:
    print(seasons[0])
elif 6 <= monthnumb <= 8:
    print(seasons[1])
elif 9 <= monthnumb <= 11:
    print(seasons[2])
else:
    print(seasons[3])