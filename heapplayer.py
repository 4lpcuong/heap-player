import sys
import argparse
from colorama import Fore, Style, init
from tabulate import tabulate


init()


def build_max_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_min_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)
def extract_max(arr):
    if len(arr) == 0:
        return None
    max_item = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    max_heapify(arr, len(arr), 0)
    return max_item

def extract_min(arr):
    if len(arr) == 0:
        return None
    min_item = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    min_heapify(arr, len(arr), 0)
    return min_item

def main(args):
    heap_steps = []

    if args.max:
        numbers = args.max
        build_heap = build_max_heap
        heap_type = "Max Heap"
    elif args.min:
        numbers = args.min
        build_heap = build_min_heap
        heap_type = "Min Heap"
    else:
        print(Fore.RED + "No valid heap type specified." + Style.RESET_ALL)
        sys.exit(1)

    current_heap = []
    for num in numbers:
        current_heap.append(num)  # Thêm phần tử mới vào cuối heap
        build_heap(current_heap, len(current_heap))  # Điều chỉnh heap sau mỗi lần thêm
        heap_steps.append(list(current_heap))  # Lưu trạng thái của heap sau mỗi bước

    print(Fore.GREEN + f"\nBuilding a {heap_type}:" + Style.RESET_ALL)
    print(tabulate(enumerate(heap_steps, 1), headers=["Step", "Heap"], tablefmt="fancy_grid"))


    # Xử lý extract heap
    if args.extract:
        if heap_type == "Max Heap":
            extracted = extract_max(current_heap)
        elif heap_type == "Min Heap":
            extracted = extract_min(current_heap)
        print(Fore.YELLOW + f"\nExtracted element: {extracted}" + Style.RESET_ALL)
        heap_steps.append(list(current_heap))
        print(tabulate(enumerate(heap_steps, 1), headers=["Step", "Heap"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a max or min heap from a list of numbers.")
    parser.add_argument("-M", "--max", nargs='+', type=int, help="Build a max heap from the given numbers.")
    parser.add_argument("-m", "--min", nargs='+', type=int, help="Build a min heap from the given numbers.")
    parser.add_argument("-e", "--extract", action="store_true", help="Extract the top element from the heap after building it.")
    args = parser.parse_args()
    main(args)

