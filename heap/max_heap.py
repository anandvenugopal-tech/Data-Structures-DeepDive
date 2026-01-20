class MaxHeap:
    def __init__(self, array):
        self.build_heap(array)
    def build_heap(self, array):
        self.heap = array
        i = self.get_parent(len(self.heap) - 1)
        while i >= 0:
            self.shift_down(i)
            i = i - 1


    def shift_down(self, current_idx):
        end_idx = len(self.heap) - 1
        left_idx = self.get_left_child(current_idx)
        while left_idx <= end_idx:
            right_idx = self.get_right_child(current_idx)
            if left_idx <= right_idx and self.heap[left_idx] < self.heap[right_idx]:
                idx_to_shift = right_idx
            else:
                idx_to_shift = left_idx
            if self.heap[current_idx] < self.heap[idx_to_shift]:
                self.heap[current_idx], self.heap[idx_to_shift] = self.heap[idx_to_shift], self.heap[current_idx]
                current_idx = idx_to_shift
                left_idx = self.get_left_child(current_idx)
            else:
                return


    def shift_up(self, current_idx):
        parent_idx = self.get_parent(current_idx)
        while current_idx > 0 and self.heap[parent_idx] < self.heap[current_idx]:
            self.heap[parent_idx], self.heap[current_idx] = self.heap[current_idx], self.heap[parent_idx]
            current_idx = parent_idx
            parent_idx = self.get_parent(current_idx)


    def peak(self):
        return self.heap[0]

    def remove(self):
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        self.heap.pop(len(self.heap) - 1)
        self.shift_down(0)

    def insert(self, value):
        self.heap.append(value)
        self.shift_up(len(self.heap) - 1)

    def get_parent(self, i):
        return (i - 1) // 2
    def get_left_child(self, i):
        return (i * 2) + 1
    def get_right_child(self, i):
        return (i * 2) + 2

    def display(self):
        i = 0
        while i < len(self.heap):
            print(i, self.heap[i])
            i = i + 1


def main():
    array = [8, 5, 10, 3, 6, 9, 13]
    mh = MaxHeap(array)
    mh.display()

if __name__ == "__main__":
    main()