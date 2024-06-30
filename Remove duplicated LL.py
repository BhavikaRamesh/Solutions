#Function to remove duplicates from sorted linked list.
def removeDuplicates(head):
    #code here
    if head is None:
        return
    curr = head
    while curr:
        if curr.next and curr.next.data == curr.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

#Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        if head is None:
            return
        curr = head
        visited = {}
        prev = None
        while curr:
            if curr.data in visited:
                prev.next = curr.next
            else:
                visited[curr.data] = True
                prev = curr
            curr = curr.next
        return head
