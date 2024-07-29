try:
    names = []
    subj = []
    with open('num3.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:  
                imy, yroki = line.split(":")
                names.append(imy)
                subj.append(yroki)
                print(f'Names: {names}')
                print(f'Subjects: {subj}')

    itog = []
    nagmi = input("Введите название предмета, по которому пойдет поиск (Math, Science, Art, History): ").strip().lower()
    
    for name, listik in zip(names, subj):
        if nagmi in listik.lower():  
            itog.append(name)
    
    if itog:
        print(f'Результаты поиска: {itog}')
    else:
        print("Не найдено ни одного совпадения.")
    
except FileNotFoundError:
    print("Файл не найден")
