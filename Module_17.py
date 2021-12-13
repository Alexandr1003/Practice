`array = [i for i in range(1,100)] # 1,2,3,4,..
element = int(input("Введите число:"))

if element not in array:
    array.append(element)

def binary_search(array, element, left, right): 
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует
    middle = (right + left) // 2 # находимо середину
    if array[middle] == element: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif element < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else: # иначе в правой
        return binary_search(array, element, middle + 1, right)


def sort_array(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = sort_array(array)

print(array)

print(binary_search(array, element, 0, 99) + 1)
