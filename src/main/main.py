import numpy as np


class Arr:

    def __init__(self, array):
        self.array = array

    def fillArr(self, length):
        self.array = np.random.randint(0, 100, length)

    def bubleSort(self):
        n = len(self.array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        return self.array

    def printArr(self):
        print(self.array)


