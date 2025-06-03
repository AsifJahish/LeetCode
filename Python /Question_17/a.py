# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head  # Pointer to traverse the linked list

        while current and current.next:
            if current.val == current.next.val:  # If duplicate is found
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next node

        return head  # Return the modified linked list

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Example usage
head = create_linked_list([1, 1, 2])
solution = Solution()
new_head = solution.deleteDuplicates(head)
print_linked_list(new_head)  # Output: [1, 2]
