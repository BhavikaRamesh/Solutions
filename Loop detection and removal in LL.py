class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        if head is None or head.next is None:
            return
        fast = head
        slow = head
        while fast != None and slow != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                slow = head
                while slow.next != fast.next:
                    slow = slow.next
                    fast = fast.next
                fast.next = None
