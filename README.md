# 401-data-structures-and-algorithms
Repo for 401 Code Challenges

Adam Owada

# Table of Contents



Code Challenge 1
### Reverse an Array
Write a function called reverseArray that takes in a list and returns the list in reverse order.

### Challenge
```
Input	                                    Output
[1, 2, 3, 4, 5, 6]	                      [6, 5, 4, 3, 2, 1]
[89, 2354, 3546, 23, 10, -923, 823, -12]	[-12, 823, -923, 10, 23, 3546, 2354, 89]
```

### Approach & Efficiency
Used a for loop with range to append elements from the list argument into an empty list in reverse order and return new list.

### Solution
![code challenge 1 whiteboard](assets/array-reverse-1.png)
![code challenge 1 whiteboard](assets/array-reverse-2.png)


Code Challenge 2
### Insert Shift Array
Write a function called insertShiftArray that takes in a list and a value to be added, and returns the list with the value in the middle.

### Challenge
```
Input	                Output
[2,4,6,8], 5	        [2,4,5,6,8]
[4,8,15,23,42], 16	  [4,8,15,16,23,42]
```

### Approach & Efficiency
Used math.ceil to find proper index, and list.insert to insert into the list.

### Solution
![code challenge 2 whiteboard](assets/array-shift.png)


Code Challenge 5
### Linked List Implementation
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

### Challenge
```
Define a method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
Define a method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
Define a method called __str__ which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
```

### Approach & Efficiency
Used classes and OOP to solve this challenge. LinkedList instance method insert() changes the value of the head and makes current head the new nodes .next. Method includes() uses a while loop to check each node. If none of the node.value equals the passed in value, returns false. Returns true if one of the nodes .value equals the passed in value. Method __str__ is a python string method visually representing all of the nodes in the linked list, in order, with an arrow pointing to the next node and its value. 

### Solution
No whiteboard requirement for this challenge. 