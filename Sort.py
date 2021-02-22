# Selection Sort
def selection_sort(array):
    for i in range(len(array)):
        min_index = i  # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
            array[i], array[min_index] = array[min_index], array[i]  # swap

    print("selection sort: ", array)


# Insertion Sort
def insertion_sort(array):
    for i in range(1, len(array)):  # N - 1 만큼 반복
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    print("insertion sort: ", array)


if __name__ == '__main__':
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    selection_sort(array)
    insertion_sort(array)
    
