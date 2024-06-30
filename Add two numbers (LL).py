# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        # Add digits from both lists
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val > 9:
                carry = 1
                val = val % 10
            else:
                carry = 0
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        # Handle extra values in L1
        while l1:
            val = l1.val + carry
            if val > 9:
                carry = 1
                val = val % 10
            else:
                carry = 0
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
        # Handle extra values in L2
        while l2:
            val = l2.val + carry
            if val > 9:
                carry = 1
                val = val % 10
            else:
                carry = 0
            curr.next = ListNode(val)
            curr = curr.next
            l2 = l2.next
        # Check if there is final carry to add
        if carry == 1:
            curr.next = ListNode(1)
        return dummy.next
