## Skip List
In computer science, a skiplist is data structurehat allows search complexity as well as insertion complexity within an ordered sequence of elements. Thus it can get the best features of an array(for searching) while maintaining a linked like structure that allows insertion- which is not possible in an array. Fast search is made possible by maintaining a linked hierarchy of subsequences, with each successive subsequence skipping over fewer elements than the previous one.

## User Accessible Functions
Skip List has the following Functions:
 - ### Insert Function
	Operations that enables user to insert data.
- ### Delete Function
	Operations that enables user to delete data.
- ### Search Function
	Operations that enables user to Search data.

## Time Complexity
- ### Worst Case
	The worst case search time for a sorted linked list is O(n) as we can only linearly traverse the list and cannot skip nodes while       searching
- ### Average Case
	The Average case search time for a sorted linked list is O(logn) as we can only linearly traverse the list and skip nodes while       searching
## height of the skip list
- The height of a skip list is the height of the highest tower: What determines the height of a tower: The height of a tower is determined by the number of consecutive successful tosses (using a fair (50% success) coin)

  
##  How To Use:
 - Insert a number you wanna insert in the list by calling `insert()` function.
 - Then Call the function `Display()` inorder to print the list.
 - Call `deleteElement()` to Delete a node.
 - Then Call the function `Search()`inorder to search a particular node.
 - Inorder to obtain Randomized level we must call the function `RandomLevel()`
 
## Application of Skip List
 - Skip list are used in distributed applications. In distributed systems, the nodes of skip list represents the computer systems and pointers represent network connection

## How exactly is a skip list constructed from a series of linked lists?
 - A skip list is built in layers. The bottom layer is an ordinary ordered linked list. ... If the current element is greater than the target, or the search reaches the end of the linked list, the procedure is repeated after returning to the previous element and dropping down vertically to the next lower list.
