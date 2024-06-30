class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		
	def insertAtBeginning(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
			return
		else:
			newNode.next = self.head
			self.head = newNode
			
	def insertAtEnd(self, data):
		newNode = Node(data)
		if self.head == None:
			self.head = newNode
			return
		currentNode = self.head
		while currentNode.next:
			currentNode = currentNode.next
		currentNode.next = newNode
		
	def insertAtGivenIndex(self, data, index):
		newNode = Node(data)
		currentNode = self.head
		idxCounter = 0
		while currentNode is not None and idxCounter < index - 1:
			currentNode = currentNode.next
			idxCounter += 1
		newNode.next = currentNode.next
		currentNode.next = newNode
		
	def updateNode(self, newValue, index):
		currentNode = self.head
		idxCounter = 0
		while currentNode is not None and idxCounter < index - 1:
			currentNode = currentNode.next
			idxCounter += 1
		currentNode.data = newValue
		
	def deleteFirstNode(self):
		if self.head == None:
			return
		self.head = self.head.next
		
	def deleteLastNode(self):
		if self.head == None:
			return
		currentNode = self.head
		while currentNode.next.next:
			currentNode = currentNode.next
		currentNode.next = None
		
	def deleteAtGivenIndex(self, index):
		if self.head == None:
			return
		currentNode = self.head
		idxCounter = 0
		while currentNode is not None and idxCounter < index - 1:
			currentNode = currentNode.next
			idxCounter += 1
		currentNode.next = currentNode.next.next
		
	def deleteAtGivenData(self, value):
		currentNode = self.head
		if currentNode.data == value:
			self.deleteFirstNode()
			return
		while currentNode is not None and currentNode.next.data != value:
			currentNode = currentNode.next
		currentNode.next = currentNode.next.next
		
	def printLinkedList(self):
		currentNode = self.head
		while currentNode:
			print(currentNode.data, end = ' ')
			currentNode = currentNode.next
			
	def lengthOfLinkedList(self):
		if self.head == None:
			return 0
		currentNode = self.head
		length = 0
		while currentNode:
			length += 1
			currentNode = currentNode.next
		return length
		

ll = LinkedList()
ll.insertAtBeginning(1)
ll.insertAtBeginning(5)
ll.insertAtBeginning(4)
ll.insertAtBeginning(2)
ll.insertAtBeginning(3)
ll.printLinkedList()
print()
ll.deleteFirstNode()
ll.printLinkedList()
print()
ll.deleteLastNode()
ll.printLinkedList()
print()
# ll.insertAtGivenIndex(7, 1)
# ll.printLinkedList()
# print()
ll.deleteAtGivenIndex(2)
ll.printLinkedList()
print()
ll.insertAtGivenIndex(7, 1)
ll.printLinkedList()
print()
ll.insertAtGivenIndex(8, 2)
ll.printLinkedList()
print()
ll.insertAtGivenIndex(7, 3)
ll.printLinkedList()
print()
ll.deleteAtGivenData(7)
ll.printLinkedList()
print()
print(ll.lengthOfLinkedList())
