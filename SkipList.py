import random
class Node:
    def __init__(self, value, level):
        self.value = value
        self.next = [None] * (level + 1)

class SkipList:
    def __init__(self, maximum_level, Prob):
        self.maximum_level = maximum_level
        self.prob = Prob
        self.header = self.CreateNode(self.maximum_level, -1)
        self.level = 0

    def CreateNode(self, level, value):
        new_node = Node(value, level)
        return new_node

    def random_level(self):
        level = 0
        while random.random() < self.prob and level < self.maximum_level:
            level = level + 1
        return level

    def insert(self, value):
        Array = [None] * (self.maximum_level + 1)
        x = self.header
        for i in range(self.level, -1, -1):
            while x.next[i] and x.next[i].value < value:
                x = x.next[i]
            Array[i] = x
        x = x.next[0]
        if x == None or x.value != value:
            RandomLevel = self.random_level()
            if RandomLevel > self.level:
                for i in range(self.level + 1, RandomLevel + 1):
                    Array[i] = self.header
                self.level = RandomLevel
            n = self.CreateNode(RandomLevel, value)
            for i in range(RandomLevel + 1):
                n.next[i] = Array[i].next[i]
                Array[i].next[i] = n

            print("Successfully inserted key {}".format(value))

    def deleteElement(self, value):

        Array = [None] * (self.maximum_level + 1)
        x = self.header
        for i in range(self.level, -1, -1):
            while x.next[i] and x.next[i].value < value:
                x = x.next[i]
            Array[i] = x
        x = x.next[0]
        if x != None and x.value == value:
            for i in range(self.level + 1):
                if Array[i].next[i] != x:
                    break
                Array[i].next[i] = x.next[i]

            while (self.level > 0 and self.header.next[self.level] == None):
                self.level -= 1
            print("Deleted Element {}".format(value))

    def searchElement(self, value):
        x = self.header
        for i in range(self.level, -1, -1):
            while (x.next[i] and x.next[i].value < value):
                x = x.next[i]
        x = x.next[0]
        if x and x.value == value:
            print("Found Value: ", value)

    def displayList(self):
        print("\n*****Skip List******")
        x = self.header
        for lvl in range(self.level + 1):
            print("Level {}: ".format(lvl), end=" ")
            node = x.next[lvl]
            while (node != None):
                print(node.value, end=" ")
                node = node.next[lvl]
            print("")

def main():
    lst = SkipList(3, 0.5)
    lst.insert(3)
    lst.insert(6)
    lst.insert(7)
    lst.insert(9)
    lst.insert(12)
    lst.insert(19)
    lst.insert(17)
    lst.searchElement(19)
    lst.deleteElement(3)
    lst.displayList()
main()
