# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
    
        tempList = self.merge(lists[0], lists[1]) 
        

        return  self.mergeKLists([tempList] +  lists[2: ] )


    def merge(self,list1, list2):
        tempNode  = ListNode(-1)
        tail = tempNode

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next
        
        tail.next = list1 if list1 else list2

        return tempNode.next
        


        
        
        