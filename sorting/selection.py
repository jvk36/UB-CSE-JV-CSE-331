def selection_sort(a):
    for i in range(0, len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        a[min], a[i] = a[i], a[min]


a = [53, 12, 15, 0, 4, 97, 22]
print(a)
selection_sort(a)
print(a)
