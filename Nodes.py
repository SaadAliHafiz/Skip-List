from SkipList import SkipList

lst = SkipList(3, 0.5)
lst.insert(3)
lst.insert(6)
lst.insert(7)
lst.insert(9)
lst.insert(12)
lst.insert(19)
lst.insert(17)
lst.displayList()
lst.searchElement(19)
lst.deleteElement(3)
lst.displayList()
