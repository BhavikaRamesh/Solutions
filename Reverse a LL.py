class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        next = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
