try:
    with open('cities.txt', 'r') as file:
        cities = []
        grades = []
        for line in file:
            city, grade = line.strip().split(":")
            grades.append(grade)
            cities.append(city)
            print(city)
            print(grade)
    slovar = dict(zip(cities, grades))
    print(slovar)
    nagmi = input("выберите 1,чтобы увидеть мин.колво.жит  ")
    minimum = []
    min_gorod = min(slovar.values())
    min_keys = [i for i, value in slovar.items() if value == min_gorod]
    minimum.append(min_keys)
    print(minimum)
    sortirovochka = {key: value for key, value in slovar.items() if value > min(slovar.values())}
    print(sortirovochka)
    sort_sortirovochka = {key:value for key, value in sorted(sortirovochka.items())}
    with open(' filtered_cities.txt', 'w') as file:
        for key, value in sort_sortirovochka.items():
            file.write(f'{key}:{value}\n')
except FileNotFoundError:
    print("файль не найден")