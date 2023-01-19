#!/usr/bin/env python3

def counting_sort(A):
    """Sort assuming items have nonneg keys"""
    u = 1 + max([x for x in A]) #modify x to x.key if A not a Python list
    D = [0] * u
    for x in A:
        D[x] += 1
    for k in range(1,u):
        D[k] += D[k-1]
    print(D)
    for x in list(reversed(A)):
        A[D[x] - 1] = x
        D[x] -= 1

def quickSort(arr, low, high):
    ''' Python implementation of QuickSort using Hoare's
    partition scheme.

     This function takes middle element as pivot, and places
      all the elements smaller than the pivot on the left side
      and all the elements greater than the pivot on
      the right side. It returns the index of the last element
      on the smaller side '''

    def partition(arr, low, high):
        ''' The main function that implements QuickSort.
        Args:
            arr --> Array to be sorted,
            low --> Starting index,
            high --> Ending index '''
        pivot = arr[(low+high)//2]
        i = low - 1
        j = high + 1

        while (True):

            # Find leftmost element greater than
            # or equal to pivot
            i += 1
            while (arr[i] < pivot):
                i += 1

            # Find rightmost element smaller than
            # or equal to pivot
            j -= 1
            while (arr[j] > pivot):
                j -= 1

            # If two pointers met.
            if (i >= j):
                return j

            arr[i], arr[j] = arr[j], arr[i]

    if (low < high):

        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi)
        quickSort(arr, pi + 1, high)

### Tests
def test_counting():
    testA = [3,1,6,2,1,5]
    counting_sort(testA)
    assert testA == sorted(testA)
