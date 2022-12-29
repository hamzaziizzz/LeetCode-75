"""
PROBLEM:
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

EXAMPLE 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

EXAMPLE 2:
    Input: list1 = [], list2 = []
    Output: []

EXAMPLE 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

CONSTRAINTS:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2

        resultant = ListNode()
        pointer3 = resultant

        if (pointer1 is None) and (pointer2 is None):
            return None
        
        while (pointer1 is not None) and (pointer2 is not None):
            if pointer1.val <= pointer2.val:
                pointer3.val = pointer1.val
                pointer1 = pointer1.next
            elif pointer1.val > pointer2.val:
                pointer3.val = pointer2.val
                pointer2 = pointer2.next
            pointer3.next = ListNode()
            pointer3 = pointer3.next
        
        if pointer1 is None:
            while pointer2 is not None:
                pointer3.val = pointer2.val
                pointer2 = pointer2.next
                if pointer2 is None:
                    break
                pointer3.next = ListNode()
                pointer3 = pointer3.next

        if pointer2 is None:
            while pointer1 is not None:
                pointer3.val = pointer1.val
                pointer1 = pointer1.next
                if pointer1 is None:
                    break
                pointer3.next = ListNode()
                pointer3 = pointer3.next
                

        return resultant


if __name__ == "__main__":
    solution = Solution()

    # CASE 1
    print("================================== CASE 1 ==================================")
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    result = solution.mergeTwoLists(list1, list2)

    l1 = []
    while list1 is not None:
        l1.append(list1.val)
        list1 = list1.next
    print(f"list1 \t = {l1}")

    l2 = []
    while list2 is not None:
        l2.append(list2.val)
        list2 = list2.next
    print(f"list2 \t = {l2}")

    answer = []
    while result is not None:
        answer.append(result.val)
        result = result.next
    print(f"solution = {answer}")


    print()
    # CASE 2
    print("================================== CASE 2 ==================================")
    list1 = None
    list2 = None
    result = solution.mergeTwoLists(list1, list2)

    l1 = []
    while list1 is not None:
        l1.append(list1.val)
        list1 = list1.next
    print(f"list1 \t = {l1}")

    l2 = []
    while list2 is not None:
        l2.append(list2.val)
        list2 = list2.next
    print(f"list2 \t = {l2}")

    answer = []
    while result is not None:
        answer.append(result.val)
        result = result.next
    print(f"solution = {answer}")


    print()
    # CASE 3
    print("================================== CASE 3 ==================================")
    list1 = None
    list2 = ListNode()
    result = solution.mergeTwoLists(list1, list2)

    l1 = []
    while list1 is not None:
        l1.append(list1.val)
        list1 = list1.next
    print(f"list1 \t = {l1}")

    l2 = []
    while list2 is not None:
        l2.append(list2.val)
        list2 = list2.next
    print(f"list2 \t = {l2}")

    answer = []
    while result is not None:
        answer.append(result.val)
        result = result.next
    print(f"solution = {answer}")

    print()
