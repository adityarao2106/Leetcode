class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()  # Capitalized 'ListNode'
        cur = dummy

        carry = 0
        # Added 'or carry' to catch leftover carry values
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)  # Capitalized 'ListNode'

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next