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

    for i in range(1, len(numbers) + 1):
        current_heap = numbers[:i]
        build_heap(current_heap, i)
        heap_steps.append(list(current_heap))

    print(Fore.GREEN + f"\nBuilding a {heap_type}:" + Style.RESET_ALL)
    print(tabulate(enumerate(heap_steps, 1), headers=["Step", "Heap"], tablefmt="fancy_grid"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a max or min heap from a list of numbers.")
    parser.add_argument("-M", "--max", nargs='+', type=int, help="Build a max heap from the given numbers.")
    parser.add_argument("-m", "--min", nargs='+', type=int, help="Build a min heap from the given numbers.")

    args = parser.parse_args()
    main(args)
