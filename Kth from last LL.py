def getKthFromLast(head, k):
    #code here
    counter = 1
    if head is None:
        return -1
    current = head
    while current.next:
        current = current.next
        counter += 1
    if k > counter:
        return -1
    m = counter - k + 1
    current = head
    for i in range(1, m):
        current = current.next
    return current.data
