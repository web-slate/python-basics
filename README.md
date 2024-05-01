# Python Basics
Python Basics

# Data Structure in Python

| Standard Data Structure | Implementation Note or Python Equivalent      |
|-------------------------|----------------------------------------------|
| Array                   | Implemented as List in Python                |
| Stack                   | Can be implemented using a List with append and pop methods |
| Queue                   | Can be implemented using collections.deque   |
| Priority Queue          | Can be implemented using queue.PriorityQueue or heapq |
| Set                     | Implemented as Set in Python                 |
| Linked List             | No native type; can be implemented using classes with nodes |
| Doubly Linked List      | No native type; can be implemented with nodes having previous and next pointers |
| Circular Linked List    | No native type; can be implemented with nodes where the last node links to the first |
| Skip List               | No native type; can be implemented with multiple levels of linked lists for efficient search |
| Hash Map                | Implemented as Dictionary in Python          |
| Heap                    | `heapq` can be used for heap operations in Python |
| Trie                    | No native type; can be implemented with nodes containing a dictionary of children |
| Binary Tree             | No native type; can be implemented using classes with node references |
| Binary Search Tree      | No native type; can be implemented with ordered insertion and deletion in a binary tree structure |
| B-Tree                  | No native type; typically used in databases and file systems; can be implemented using classes with multiple child nodes |
| Red-Black Tree          | No native type; can be implemented with self-balancing properties during insertions and deletions |
| AVL Tree                | No native type; can be implemented with self-balancing properties based on node heights |
| Graph                   | No native type; can be implemented with adjacency lists or matrices |



![python-one-pic](https://github.com/web-slate/python-basics/assets/1652629/b7c0e938-1eab-4259-a098-3cc9cf8d17f2)


## Setup

### Setup Virtual Environment

```
python -m venv venv
```

### Activate Virtual Environment

| Operating System | Command to Activate Virtual Environment |
|------------------|----------------------------------------|
| Windows          | `venv\Scripts\activate`                |
| Mac/Linux        | `source venv/bin/activate`             |


### Install StylePy Module for styling command line output.

```
pip install -r requirements.txt
```