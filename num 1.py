try:
    with open('cities.txt', 'r') as file:
        cities = []
        grades = []
        for line in file:
            city, grade = line.strip().split(":")
            grades.append(int(grade))  
            cities.append(city)
            print(city)
            print(grade)
    
 
    slovar = dict(zip(cities, grades))
    print(slovar)
    
  
    nagmi = input("Выберите 1, чтобы увидеть мин. количество жителей: ")
    
   
    min_gorod = min(slovar.values())
    min_keys = [i for i, value in slovar.items() if value == min_gorod]
    print(f'Города с минимальным количеством жителей: {min_keys}')
    
 
    sortirovochka = {key: value for key, value in slovar.items() if value > min_gorod}
    print(f'Отфильтрованный словарь: {sortirovochka}')
    
    sort_sortirovochka = dict(sorted(sortirovochka.items()))
    

    with open('filtered_cities.txt', 'w') as file:
        for key, value in sort_sortirovochka.items():
            file.write(f'{key}:{value}\n')
except FileNotFoundError:
    print("Файл не найден")
