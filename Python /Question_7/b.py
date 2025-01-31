class ListNode(object):
    def __init__(self, val =0, next=None):
        self.val= val
        self.next= next

class Solution(object):
    def mergeTwoLists(self, list1, list2):

        
        if not list1:
            return list2
        if not list2:
            return list1
        

        if list1.val< list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next= self.mergeTwoLists(list1, list2.next)

            return list2



def list_to_linked_list(elements):
    dummy = ListNode()
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# Helper function to convert a linked list back to a Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

list1 = list_to_linked_list([1, 2, 4])
list2 = list_to_linked_list([1, 3, 4])

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

print(linked_list_to_list(merged_list))