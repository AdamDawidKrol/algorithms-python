def maxHeapify(table, i, size=-1):
    left = 2*i
    right = 2*i + 1
    largest = i
    result = table
    if size == -1:
        size=len(table)
    if left < size:
        if table[left] > table[i]:
            largest = left
    if right < size:
        if table[right] > table[largest]:
            largest = right
    if largest != i:
        pom = table[i]
        table[i] = table[largest]
        table[largest] = pom
        result = maxHeapify(table, largest, size)
    return result

def buildMaxHeap(table):
    result = table
    for i in range(int(len(table)/2),0,-1):
        result = maxHeapify(table, i)
    return result

def heapsort(table):
    size = len(table)
    for i in range(len(table)-1, 1, -1):
        temp = table[i]
        table[i] = table[1]
        table[1] = temp
        size = size - 1
        table = maxHeapify(table, 1, size)
    return table


if __name__ == "__main__":
    #table = [10, 1, 8, 2, 3, 4, 5]
    #table = maxHeapify(table, 1)
    #print(table)
    #table = [0, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    #table = maxHeapify(table, 2)
    #print(table)

    table = [0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = buildMaxHeap(table)
    print(heap)

    sortedTable = heapsort(table)
    print(sortedTable)


