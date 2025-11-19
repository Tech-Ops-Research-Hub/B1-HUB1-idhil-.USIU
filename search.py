#Define a linked list and explain why search must be sequential.
#linked list is a linear data structure where each element (node) points to the next node in the sequence.
#Search must be sequential becausethere is no direct access to elements; you must traverse the list
#from the head node to find a specific value.therefore you cant jump from one node to another.

#State the time and space complexity of linked-list search and justify each.
#Time complexity is O(n) because in the worst case,you may have to traverse the entire list to find the value.
#Space complexity is O(1) because the search operation uses a constant amount of extra space regardless of the list size.


 #Describe the exact steps executed when searching for a value that is not in the list.
#start at the head node
#compare the node's data with the target value
#if equal search is successful
#otherwise move to the next node
#if next node is null search is unsuccessful.

 #Rewrite the search algorithm so it returns the node instead of a boolean.
def search_linked_list(head, target):
    current = head
    while current:
        if current.data == target:

 #Explain how search behaves in an empty list, a single-node list, and a list with duplicate values.

 #in an empty list, search immediately returns null since there are no nodes to check.
#in a single-node list search checks the only node and returns it if it matches or null if it doesn't.
#list with duplicate values search returns the first node that matches the target value..
