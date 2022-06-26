# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        
        current_l1 = l1
        current_l2 = l2
        
        return_nd = ListNode();
        return_nd_current = return_nd;
        
        while True:
            
            digit = 0
            
            if current_l1 != None:
                digit += current_l1.val
                current_l1 = current_l1.next
            
            if current_l2 != None:
                digit += current_l2.val
                current_l2 = current_l2.next
            
            digit += carry_over
            
            if digit >= 10:
                carry_over = 1
            else:
                carry_over = 0
                
            if digit == 0 and carry_over == 0:
                if current_l1 == None and current_l2 == None:
                    if return_nd.next == None:
                        return_nd_current.next = ListNode(digit % 10)
                    else:
                        break

            return_nd_current.next = ListNode(digit % 10)
            return_nd_current = return_nd_current.next
            
        return return_nd.next
