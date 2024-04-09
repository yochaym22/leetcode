def min_heapify(heap):
    length = len(heap)
    if length <= 1:
        return

    # Start from the last non-leaf node
    start_index = length // 2 - 1

    for i in range(start_index, -1, -1):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        min_index = i
        if left_child_index < length and heap[left_child_index] < heap[min_index]:
            min_index = left_child_index
        if right_child_index < length and heap[right_child_index] < heap[min_index]:
            min_index = right_child_index

        if min_index != i:
            heap[i], heap[min_index] = heap[min_index], heap[i]
            min_heapify(heap)  # Recursively heapify the subtree

    return heap


heap = [4, 10, 3, 5, 1]
min_heapify(heap)
print(heap)
