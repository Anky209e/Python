class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def _left_child(self, index):
        return (2 * index) + 1

    def _right_child(self, index):
        return (2 * index) + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _sink_down(self, index):
        max_index = index

        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[
                max_index
            ]:
                max_index = left_index
            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[
                max_index
            ]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value


if __name__ == "__main__":
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]

    def find_kth_smallest(nums, k):
        kth_heap = MaxHeap()
        for i in nums:
            kth_heap.insert(i)
            if len(kth_heap.heap) > k:
                kth_heap.remove()

        print(kth_heap.remove())

    def stream_max(nums):
        max_heap = MaxHeap()
        result = []
        for num in nums:
            max_heap.insert(num)
            result.append(max_heap.heap[0])
        return result

    find_kth_smallest(nums, 7)
