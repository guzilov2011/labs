def min(arr1):  #минимальное значение
    minimal = arr1[0] #принимаем нулевой элемент массива за минимальный
    for i, el in enumerate(arr1): #для каждого элемента в массиве
        if el < minimal: #если элемент меньше минимального 
            minimal = el #то обновляем минимальное значение
    return minimal
arr1 = [1, 4, 88, 34, 39, 43, 45]
print(min(arr1))
print(sum(arr1) / len(arr1)) #среднее значение
