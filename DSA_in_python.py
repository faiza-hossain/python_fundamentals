#Implementing a linked list
class Node:
  def __init__(self, data):
    self.value = data
    # Leave the node initially without a next value
    self.next = None
class LinkedList:
  def __init__(self):
    # Set the head and the tail with null values
    self.head = None
    self.tail = None
    
#Inserting a node at the beginning of a linked list
def insert_at_beginning(self, data):
    # Create the new node
    new_node = node(data)
    # Check whether the linked list has a head node
    if self.head:
      # Point the next node of the new node to the head
      new_node.next = self.head
      self.head = new_node
    else:
      self.tail = new_node      
      self.head = new_node

#Removing the first node from a linked list
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def remove_at_beginning(self):
    # The "next" node of the head becomes the new head node
    self.head = self.head.next

#Practicing with Big O Notation
colors = ['green', 'yellow', 'blue', 'pink']

def linear(colors):
  # Iterate the elements of the list
  for i in colors:
    # Print the current element of the list
    print(i)	

linear(colors)

#Implementing a Stack with the push method
class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def push(self, data):
    # Create a node with the data
    new_node = Node(data)
    if self.top:
      new_node.next = self.top
    # Set the created node to the top node
    self.top = new_node
    # Increase the size of the stack by one
    self.size += 1

#Implementing the pop method for a stack
class Stack:
  def __init__(self):
    self.top = None
    self.size = 0
    
  def pop(self):
    # Check if there is a top element
    if self.top is None:
      return None
    else:
      popped_node = self.top
      # Decrement the size of the stack
      self.size -= 1
      # Update the new value for the top node
      self.top = self.top.next
      popped_node.next = None
      return popped_node.data 
    
#Using Python's LifoQueue
# Import the module to work with Python's LifoQueue
import queue

# Create an infinite LifoQueue
my_book_stack = queue.LifoQueue(maxsize=0)

# Add an element to the stack
my_book_stack.put("Don Quixote")

# Remove an element from the stack
my_book_stack.get('Don Quixote')

# Implementing a queue for printer tasks
class PrinterTasks:
  def __init__(self):
    self.queue = Queue()
      
  def add_document(self, document):
    # Add the document to the queue
    self.queue.enqueue(document)
      
  def print_documents(self):
    # Iterate over the queue while it has elements
    while self.queue.has_elements():
      # Remove the document from the queue
      print("Printing", self.queue.dequeue())

printer_tasks = PrinterTasks()
# Add some documents to print
printer_tasks.add_document("Document 1")
printer_tasks.add_document("Document 2")
printer_tasks.add_document("Document 3")
# Print all the documents in the queue
printer_tasks.print_documents()

#Python's SimpleQueue
import queue

# Create the queue
my_orders_queue = queue.SimpleQueue()

# Add an element to the queue
my_orders_queue.put("samosas")

# Remove an element from the queue
my_orders_queue.get()

#Dictionary
for key, value in my_menu.items():
  print(f"The price of the {key} is {value}.")

# Iterate the elements of the menu
for dish, values in my_menu.items():
  # Print whether the dish must be served cold or hot
  print(f"{dish.title()} is best served {values['best_served']}.")

#Tree implementation

class TreeNode:
  
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left_child = left
    self.right_child = right

node1 = TreeNode("B")
node2 = TreeNode("C")
root_node = TreeNode("A",node1, node2)

#Graph implementation
class Graph:
  def __init__(self):
    self.vertices={}
  def add_vertex(self,vertex):
    self.vertices[vertex]=[]
  def add_edge(self,source,target):
    self.vertices[source].append(target)

#weighted graph
class WeightedGraph:
  def __init__(self):
    self.vertices = {}
  
  def add_vertex(self, vertex):
    # Set the data for the vertex
    self.vertices[vertex] = []
    
  def add_edge(self, source, target, weight):
    # Set the weight
    self.vertices[source].append([target, weight])
my_graph = WeightedGraph()

# Create the vertices
my_graph.add_vertex('Paris')
my_graph.add_vertex('Toulouse')
my_graph.add_vertex('Biarritz')

# Create the edges
my_graph.add_edge('Paris', 'Toulouse', 678)
my_graph.add_edge("Toulouse", 'Biarritz', 312)
my_graph.add_edge("Biarritz", 'Paris', 783)

#Recursion
def fibonacci(n):
  # Define the base case
  if n <= 1:
    return n
  else:
    # Call recursively to fibonacci
    return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(6))

cache = [None]*(100)

def fibonacci(n): 
    if n <= 1:
        return n
    
    # Check if the value exists
    if not cache[n]:
        # Save the result in cache
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return cache[n]
    

print(fibonacci(6))

#tower of hanoi
def hanoi(num_disks, from_rod, to_rod, aux_rod):
  if num_disks <= 0:
    hanoi(num_disks, from_rod, aux_rod, to_rod)
    print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
    hanoi(num_disks, aux_rod, to_rod, from_rod)   

num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)

#Implementing binary search
def binary_search(ordered_list, search_value):
  first = 0
  last = len(ordered_list) - 1
  
  while first <= last:
    middle = (first + last)//2
    # Check whether the search value equals the value in the middle
    if ordered_list[middle] == search_value:
      return True
    # Check whether the search value is smaller than the value in the middle
    elif search_value < ordered_list[middle]:
      # Set last to the value of middle minus one
      last=middle-1
    else:
      first = middle + 1
  return False
  
print(binary_search([1,5,8,9,15,20,70,72], 5))

#Binary search using recursion
def binary_search_recursive(ordered_list, search_value):
  # Define the base case
  if len(ordered_list) == 0:
    return False
  else:
    middle = len(ordered_list)//2
    # Check whether the search value equals the value in the middle
    if search_value == ordered_list[middle]:
        return True
    elif search_value < ordered_list[middle]:
        # Call recursively with the left half of the list
        return binary_search_recursive(ordered_list[:middle], search_value)
    else:
        # Call recursively with the right half of the list
        return binary_search_recursive(ordered_list[middle+1:],search_value)
  
print(binary_search_recursive([1,5,8,9,15,20,70,72], 5))

#Inserting a node into a binary search tree
class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, data):
    new_node = TreeNode(data)
    # Check if the BST is empty
    if self.root == None:
      self.root = new_node
      return
    else:
      current_node = self.root
      while True:
        # Check if the data to insert is smaller than the current node's data
        if data < current_node.data:
          if current_node.left_child == None:
            current_node.left_child = new_node
            return 
          else:
            current_node = current_node.left_child
        # Check if the data to insert is greater than the current node's data
        elif data > current_node.data:
          if current_node.right_child == None:
            current_node.right_child = new_node
            return
          else:
            current_node = current_node.right_child

bst = CreateTree()
bst.insert("Pride and Prejudice")
print(search(bst, "Pride and Prejudice"))

#Finding the minimum node of a BST
class BinarySearchTree:
  def __init__(self):
    self.root = None

  def find_min(self):
    # Set current_node as the root
    current_node = self.root
    # Iterate over the nodes of the appropriate subtree
    while current_node.left_child:
      # Update current_node
      current_node = current_node.left_child
    return current_node.data
  
bst = CreateTree()
print(bst.find_min())

#depthfirstsearch(dfs)
#inorder traversal
class BinarySearchTree:
  def __init__(self):
    self.root = None

  def in_order(self, current_node):
    # Check if current_node exists
    if current_node:
      # Call recursively with the appropriate half of the tree
      self.in_order(current_node.left_child)
      # Print the value of the current_node
      print(current_node.data)
      # Call recursively with the appropriate half of the tree
      self.in_order(current_node.right_child)
  
bst = CreateTree()
bst.in_order(bst.root)

#preorder traversal
import queue

class ExpressionTree:
  def __init__(self):
    self.root = None

  def pre_order(self, current_node):
    # Check if current_node exists
    if current_node:
      # Print the value of the current_node
      print(current_node.data)
      # Call pre_order recursively on the appropriate half of the tree
      self.pre_order(current_node.left_child)
      self.pre_order(current_node.right_child)

          
et = CreateExpressionTree()
et.pre_order(et.root)

#dfsforgraph
def dfs(visited_vertices, graph, current_vertex):
    # Check if current_vertex hasn't been visited yet
    if current_vertex not in visited_vertices:
        print(current_vertex)
        # Add current_vertex to visited_vertices
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            # Call recursively with the appropriate values
            dfs(visited_vertices, graph, adjacent_vertex)
            
dfs(set(), graph, '0')

#breadthfirstsearch(bfs)
import queue

def bfs(graph, initial_vertex, search_value):
  visited_vertices = []
  bfs_queue = queue.SimpleQueue()
  visited_vertices.append(initial_vertex)
  bfs_queue.put(initial_vertex)

  while not bfs_queue.empty():
    current_vertex = bfs_queue.get()
    # Check if you found the search value
    if current_vertex==search_value:
      # Return True if you find the search value
      return True    
    for adjacent_vertex in graph[current_vertex]:
      # Check if the adjacent vertex has been visited
      if adjacent_vertex not in visited_vertices:
        visited_vertices.append(adjacent_vertex)
        bfs_queue.put(adjacent_vertex)
  # Return False if you didn't find the search value
  return False

print(bfs(graph, '4', '8'))

#bubblesort
def bubble_sort(my_list):
  list_length = len(my_list)
  is_sorted = False
  while not is_sorted:
    is_sorted = True
    for i in range(list_length-1):
      if my_list[i] > my_list[i+1]:
        my_list[i] , my_list[i+1] = my_list[i+1] , my_list[i]
        is_sorted = False
    list_length -= 1
  return my_list

print(bubble_sort([5, 7, 9, 1, 4, 2]))

#selectionsort
def selection_sort(my_list):
  list_length = len(my_list)
  for i in range(list_length - 1):
    # Set lowest to the element of the list located at index i
    lowest = my_list[i]
    index = i
    # Iterate again over the list starting on the next position of the i variable
    for j in range(i+1, list_length):
      # Compare whether the element of the list located at index j is smaller than lowest
      if my_list[j]<lowest:
        index = j
        lowest = my_list[j]
    my_list[i] , my_list[index] = my_list[index] , my_list[i]
  return my_list

my_list = [6, 2, 9, 7, 4, 8] 
selection_sort(my_list)
print(my_list)

#insertionsort

#mergesort
def merge_sort(my_list):
    if len(my_list) > 1: 
        mid = len(my_list)//2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
 
        i = j = k = 0
 
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]                
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1
 
        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1

my_list = [35,22,90,4,50,20,30,40,1]
merge_sort(my_list)
print(my_list)