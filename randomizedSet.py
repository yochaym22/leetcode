# https://leetcode.com/problems/insert-delete-getrandom-o1/description/?envType=study-plan-v2&envId=top-interview-150
# the test in leetcode is wrong, they should check if the returned value of random is one
# of the options and not only 2 as the expected output validate
from random import choice
class RandomizedSet:

    def __init__(self):
        self.data_set = {}
        self.elements = []
    def insert(self, val: int) -> bool:
        if val in self.data_set:
            return False
        else:
            self.data_set[val] = len(self.elements)
            self.elements.append(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.data_set:
            del self.data_set[val]
            self.elements[-1], self.elements[val] = self.elements[val], self.elements[-1]
            self.elements.pop()
            return True
        else:
            return False
    def getRandom(self) -> int:
        return choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())
