try:
    names = []
    subj = []
    with open('num3.txt', 'r') as file:
        for lines in file:
            imy, yroki = lines.strip().split(":")
            names.append(imy)
            subj.append(yroki)
            print(names)
            print(subj)
    itog = []
    nagmi = input("введите название предмета,по которому пойдет поиск:(Math,Science,Art,History)")
    for name, listik in zip(names,subj):
        if nagmi in listik:
            itog.append(name)
    print(itog)
except FileNotFoundError:
    print("файл не найден")
