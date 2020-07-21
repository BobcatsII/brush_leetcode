# 简单解法
# 把见过的节点丢集合里，下次再遇见就是环的开始
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = {None}
        while head not in s:
            s.add(head)
            head = head.next
        return head


# 快慢指针法
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None
        while head is not slow:
            head = head.next
            slow = slow.next
        return head

# 设环的起始节点为 E，快慢指针从 head 出发，快指针速度为 2，设相交节点为 X，head 到 E 的距离为 H，E 到 X 的距离为 D，环的长度为 L，
# 那么有：快指针走过的距离等于慢指针走过的距离加快指针多走的距离（多走了 n 圈的 L） 2(H + D) = H + D + nL，
# 因此可以推出 H = nL - D，这意味着如果我们让俩个慢指针一个从 head 出发，一个从 X 出发的话，他们一定会在节点 E 相遇。
#
#				  _____
#				 /     \
#		 head___________E       \
#				\       /
#				 X_____/ 
