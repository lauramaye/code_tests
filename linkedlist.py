# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def deleteDuplicates(self, head):
        if head is None:        # ---> don't execute if head is None (or there are no items in the list)
            return None
        
        if head.next is None:   # ---> there's only one val in the list; no point doing more
            return head
        current_val = head.val  # ---> assign the first value of the list
        next_obj = head.next    # ----> otherwise, prepare the next value
        print(dir(head))        # ----> I had no idea what I was doing.   
        test = ListNode()       # ----> create a new LinkedList instance
        returned_list = test    # ----> create a pointer copy of that instance MOAR MEMORY KILL!!
        
        # ---- LOOP THROUGH LISTNODE AND ASSIGN NON-DUPLICATES TO RETURNED_LIST
        while next_obj is not None:     # ----> while there are items inside the head ListNode
            print(current_val,next_obj.val) # ----> test to see what the current value and next value are
            if current_val != next_obj.val: # ----> if current value is not equal to next val
                print("current value", current_val) # ---> testing
                returned_list.val = current_val # ----> assign curr val to the new instance
                returned_list.next = ListNode() # ----> create a new instance for next ListNode value
                returned_list = returned_list.next # ---> pointer to next ListNode value
            current_val = next_obj.val # ---> move to next value
            
            # --- it's possible we will miss the last value in the list...
            if next_obj.next is None: # ----> if after this round, we have no more values
                if next_obj.val != returned_list.val:  # ----> if the next_obj value is not in the last position added to returned_list
                    print("happened!") # ----> I absolutely had no idea what I was doing 
                    returned_list.val = next_obj.val # ---> append the returned_list with the last value in the head list

                
            next_obj = next_obj.next # ----> move to the next position in the head ListNode
            
        print(test)         
        return test

        