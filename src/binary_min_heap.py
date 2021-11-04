class BinaryMinHeap:
    def __init__(self):
        self.tam = 0
        self._list = []

    def insert(self, value):
        self._list.append(value)
        self.tam = self.tam + 1

        self.heapfy_up()
        return

    def heapfy_up(self):
        if self.tam - 1 == 0:
            return

        parent_index = self.parent_index(self.tam - 1)
        current_index = self.tam - 1

        while (self._check_index(current_index) and self._check_index(parent_index)) and (self._list[current_index] < self._list[parent_index]):
            self._list[current_index], self._list[parent_index] = self._list[parent_index], self._list[current_index]
            current_index, parent_index = parent_index, self.parent_index(parent_index)

        return

    def _check_index(self, index):
        if index < self.tam and index >= 0:
            return True
        return False

    def pop(self):
        if self.tam - 1 == 0:
            self.tam = self.tam - 1
            return self._list.pop()

        old_root = self._list[0]
        self._list[0] = self._list.pop()
        self.tam = self.tam - 1

        self.heapfy_down(0)

        return old_root

    def heapfy_down(self, index):
        left = self.left_child_index(index)
        right = self.right_child_index(index)

        current = index

        while (self._check_index(current) and self._check_index(left) and self._check_index(right)) and (self._list[current] > self._list[left] or self._list[current] > self._list[right]):
            if self._list[left] < self._list[right]:
                self._list[current], self._list[left] = self._list[left], self._list[current]
                current, left, right = left, self.left_child_index(left), self.right_child_index(left)
            else: 
                self._list[current], self._list[right] = self._list[right], self._list[current]
                current, left, right = left, self.left_child_index(right), self.right_child_index(right)

    def left_child_index(self, index):
        return (2 * index) + 1

    def right_child_index(self, index):
        return (2 * index) + 2

    def parent_index(self, index):
        return (index - 1)//2