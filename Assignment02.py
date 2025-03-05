# Analysis of Algorithms (CSCI 323)
# Winter 2025
# Assignment 2 - Sorting Algorithms
# Brandon Marsh

# Acknowledgements:
# I worked with the class

import matplotlib.pyplot as plt
import pandas as pd
import random
import time

def random_list(size):
    return [random.randint(1,1000000) for i in range(size)]

def native_sort(arr,n):
    arr.sort()

def bubble_sort_v1(arr,n):
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):


            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def bubble_sort_v0(arr,n):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Python program for implementation of Selection
# Sort

def selection_sort(arr, n):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def binary_insertion_sort(arr,n):
    for i in range(1,n):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

# Python program for implementation of Cocktail Sort


def cocktail_sort(arr,n):
    swapped = True
    start = 0
    end = n-1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end-1
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1


def shell_sort(arr, n):
    gap = n // 2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i = i - gap
            j += 1
        gap = gap // 2

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort_rec(arr,n,left,right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_rec(arr,n, left, mid)
        merge_sort_rec(arr,n, mid + 1, right)
        merge(arr, left, mid, right)


def merge_sort(arr,n):
    merge_sort_rec(arr,n,0,n-1)


def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        heapify(arr, n, largest)


def heap_sort(arr,n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]



MIN_MERGE = 32
def tim_sort_calcMinRun(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort_range(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def tim_sort(arr,n):
    minRun = tim_sort_calcMinRun(n)
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion_sort(arr, n)
    size = minRun
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size = 2 * size


def quick_sort_rec(arr,n, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_rec(arr,n, low, pi - 1)
        quick_sort_rec(arr,n, pi + 1, high)

def quick_sort(arr,n):
    quick_sort_rec(arr,n,0,n - 1)

def insertion_quick_sort_rec(arr, n, low, high):
    if high-low < 10:
        insertion_sort_range(arr,low,high)
    else:
        pi = partition(arr,low,high)
        quick_sort_rec(arr,n, low, pi - 1)
        quick_sort_rec(arr, n, pi + 1, high)

def insertion_quick_sort(arr, n):
    insertion_quick_sort_rec(arr,n,0,n - 1)


def counting_sort_radix(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr,n):
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        counting_sort_radix(arr, exp)
        exp *= 10


def pigeonhole_sort(arr,n):
    my_min = min(arr)
    my_max = max(arr)
    size = my_max - my_min + 1
    holes = [0] * size
    for x in arr:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + my_min
            i += 1


def stooge_sort_rec(arr, l, h):
    if l >= h:
        return
    if arr[l] > arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t
    if h - l + 1 > 2:
        t = (int)((h - l + 1) / 3)
        stooge_sort_rec(arr, l, (h - t))
        stooge_sort_rec(arr, l + t, (h))
        stooge_sort_rec(arr, l, (h - t))
 
def stooge_sort(arr,n):
    stooge_sort_rec(arr, 0, n-1)



def bucket_sort(arr,n):
    buckets = [[] for _ in range(n)]
    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)
    for bucket in buckets:
        insertion_sort(bucket,len(bucket))
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1


def bingo_sort(arr,n):
    bingo = min(arr)
    largest = max(arr)
    nextBingo = largest
    nextPos = 0
    while bingo < nextBingo:
        startPos = nextPos
        for i in range(startPos,n):
            if arr[i] == bingo:
                arr[i], arr[nextPos] = arr[nextPos], arr[i]
                nextPos += 1
            elif arr[i] < nextBingo:
                nextBingo = arr[i]
        bingo = nextBingo
        nextBingo = largest


def get_next_gap(gap):
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
def comb_sort(arr,n):
    gap = n
    swapped = True
    while gap !=1 or swapped == 1:
        gap = get_next_gap(gap)
        swapped = False
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True


def cycle_sort(array,n):
    writes = 0
    for cycleStart in range(0, len(array) - 1):
        item = array[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, len(array)):
            if array[i] < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == array[pos]:
            pos += 1
        array[pos], item = item, array[pos]
        writes += 1
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, len(array)):
                if array[i] < item:
                    pos += 1
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            writes += 1

    return writes


def gnome_sort(arr, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if arr[index] >= arr[index - 1]:
            index = index + 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1
    return arr

def plot_times(dict_algs, sizes, trials, algs, file_name):
    alg_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for alg in algs:
        alg_num += 1
        d = dict_algs[alg.__name__]
        x_axis = [j + 0.05 * alg_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]
        plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=alg.__name__)
    plt.legend()
    plt.title("Runtime of search algorithms")
    plt.xlabel("Number of elements")
    plt.ylabel("Time for " + str(trials) + " 100 trials (ms)")
    plt.savefig(file_name)
    plt.show()

def print_times(dict_algs,filename):
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_algs).T
    print(df)
    with open(filename, "w") as f:
        f.write(df.to_string())


def run_algs(algs, sizes, trials):
    dict_algs = {}
    for alg in algs:
        dict_algs[alg.__name__] = {}
    for size in sizes:
        for alg in algs:
            dict_algs[alg.__name__][size] = 0
        for trial in range(1, trials + 1):
            arr_orig = random_list(size)
            for alg in algs:
                arr = arr_orig.copy()
                start_time = time.time()
                alg(arr, size)
                end_time = time.time()
                net_time = end_time - start_time
                if not is_sorted(arr):
                    print(alg.__name__, "wrong order", arr)
                dict_algs[alg.__name__][size] += 1000 * net_time
    return dict_algs

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def main():
    assn = "Assignment02"
    sizes = [10, 50, 100]
    algs = [native_sort,bubble_sort_v0,bubble_sort_v1,selection_sort,insertion_sort,cocktail_sort,shell_sort,merge_sort,quick_sort,insertion_quick_sort,heap_sort,tim_sort,radix_sort,pigeonhole_sort,stooge_sort,bingo_sort,comb_sort,cycle_sort,gnome_sort]
    trials = 10
    dict_algs = run_algs(algs, sizes, trials)
    print_times(dict_algs,assn + ".txt")
    plot_times(dict_algs, sizes, trials, algs, assn + ".png")



# [3] Define a function main() which will be the springboard for the execution of all other code in this assignment.

if __name__ == '__main__':
    main()
