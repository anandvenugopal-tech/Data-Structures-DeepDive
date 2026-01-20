class Sort:
    def __init__(self, nums):
        self.nums = nums
    def insertion_sort(self):
        for i in range(1, len(self.nums)):
            current = self.nums[i]
            j = i - 1
            while j >= 0 and self.nums[j] > current:
                self.nums[j + 1] = self.nums[j]
                j = j - 1
            self.nums[j + 1] = current
        return self.nums

    def bubble_sort(self):
        n = len(self.nums)
        for i in range(n):
            for j in range(1, n - i):
                if self.nums[j] < self.nums[j - 1]:
                    self.nums[j], self.nums[j - 1] = self.nums[j - 1], self.nums[j]
        return self.nums




s = Sort([32, 1, 15])
print(s.insertion_sort())
print(s.bubble_sort())




