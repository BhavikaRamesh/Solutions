class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        if head is None or head.next is None:
            return
        slow = head
        fast = head
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
