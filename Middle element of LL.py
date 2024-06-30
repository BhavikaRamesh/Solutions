class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        if head is None:
            return
        counter = 0
        current = head
        while current:
            current = current.next
            counter += 1
        current = head
        for i in range(counter // 2):
            current = current.next
        return current.data
