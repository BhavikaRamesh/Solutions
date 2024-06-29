# Insertion sort
# TC - O(N^2)
# SC - O(N)
def insertionSort(a):
	elem = 0
	for i in range(1, len(a)):
		elem = a[i]
		j = i - 1
		while j >= 0 and a[j] > elem:
			a[j], a[j + 1] = a[j + 1], a[j]
			j -= 1
		a[j + 1] = elem
	return a
print(insertionSort([23, 1, 10, 5, 2]))


# Selection sort
# TC - O(N^2)
# SC - O(1)
def selectionSort(a):
	for i in range(len(a) - 1):
		mini = i
		for j in range(i + 1, len(a)):
			if a[mini] > a[j]:
				mini = j
		a[i], a[mini] = a[mini], a[i]
	return a
print(selectionSort([23, 1, 10, 5, 2]))


# Bubble sort
# TC - O(N^2)
# SC - O(1)
def bubbleSort(a):
	for i in range(len(a)):
		swapped = False
		for j in range(len(a) - i - 1):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
				swapped = True
		if swapped == False:
			break
	return a
print(bubbleSort([23, 1, 10, 5, 2]))
