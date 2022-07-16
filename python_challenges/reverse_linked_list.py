"""
Reversed Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

"""

def reversedlinkedlist(head):

    """
    Iterative way of reversing a linked list

    1 -> 2 -> 3 -> 4 -> 5 -> null

    5 -> 4 -> 3 -> 2 -> 1 -> null

    Time Complexity O(N)
    Memory Complexity O(1)
    """

    prev = None
    current = head

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev

reversedlinkedlist([1,2,3,4,5])