def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return i + 1, A


def quicksort(A, p, r):
    (q, A) = partition(A, p, r)
    if q-1 > p:
        A = quicksort(A, p, q - 1)
    if q+1 < r:
        A = quicksort(A, q + 1, r)
    return A


if __name__ == "__main__":
    table = [0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    table = quicksort(table, 0, 10)
    print(table)
