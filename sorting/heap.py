import heapq


def heap_sort(a):
    h = []
    for elem in a:
        heapq.heappush(h, elem)
    return [heapq.heappop(h) for _ in range(len(h))]


print(heap_sort([53, 12, 15, 0, 4, 97, 22]))
