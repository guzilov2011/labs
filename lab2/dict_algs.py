ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}

emps = [ivan, darja]


def filter_childrens(emps, age_limit):
    filtered = [] #пустой массив для отфильтрованных сотрудников
    for element in emps:
        children = element.get('children')
        for child in children:
            if child['age'] >= age_limit and element.get('name') not in filtered: #если возраст больше или равен предельному и имя сотрудника ещё не попало в массив
                filtered.append(element.get('name')) #добавляем имя сотрудника в массив

    return filtered


filtered_childrens = filter_childrens(emps, 18)
print('Filtered: ')
print(filtered_childrens)
