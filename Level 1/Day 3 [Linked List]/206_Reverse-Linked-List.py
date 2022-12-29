"""
PROBLEM:
    Given the head of a singly linked list, reverse the list, and return the reversed list.

 

EXAMPLE 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]

EXAMPLE 2:
    Input: head = [1,2]
    Output: [2,1]

EXAMPLE 3:
    Input: head = []
    Output: []
 

CONSTRAINTS:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        pointer = head
        linkedList = []
        while pointer is not None:
            linkedList.append(pointer.val)
            pointer = pointer.next
        
        linkedList.reverse()

        pointer = head
        index = 0
        while (pointer is not None) and (index < len(linkedList)):
            pointer.val = linkedList[index]
            pointer = pointer.next
            index = index + 1

        return head


if __name__ == "__main__":
    solution = Solution()

    # CASE 1
    print("================================== CASE 1 ==================================")
    linkedList1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    list1 = linkedList1
    l1 = []
    while list1 is not None:
        l1.append(list1.val)
        list1 = list1.next
    print(f"Linked List = {l1}")

    result = solution.reverseList(linkedList1)
    answer = []
    while result is not None:
        answer.append(result.val)
        result = result.next
    print(f"Solution    = {answer}")


    print()
    # CASE 2
    print("================================== CASE 2 ==================================")
    linkedList2 = ListNode(1, ListNode(2))
    list2 = linkedList2
    l2 = []
    while list2 is not None:
        l2.append(list2.val)
        list2 = list2.next
    print(f"Linked List = {l2}")

    result = solution.reverseList(linkedList2)
    answer = []
    while result is not None:
        answer.append(result.val)
        result = result.next
    print(f"Solution    = {answer}")


    print()
    # CASE 3
    print("================================== CASE 3 ==================================")
    linkedList3 = None
    list3 = linkedList3
    l3 = []
    while list3 is not None:
        l3.append(list3.val)
        list3 = list3.next
    print(f"Linked List = {l3}")

    result = solution.reverseList(linkedList3)
    answer = []
    while result is not None:
        answer.append(result.val)
        result = result.next
    print(f"Solution    = {answer}")

    print()
