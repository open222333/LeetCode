from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkList:

    def __init__(self) -> None:
        self.linklist = None

    def generate_list(self, nodes: list) -> ListNode:
        """將串列依照順序 生成 鏈結串列

        Args:
            nodes (list): _description_

        Returns:
            ListNode: _description_
        """
        if len(nodes) == 0:
            return None

        # 創建第一個節點
        self.linklist = ListNode(nodes[0])
        current = self.linklist

        for val in nodes[1:]:
            current.next = ListNode(val)
            current = current.next
        return self.linklist

    def set_linklist(self, linklist):
        self.linklist = linklist

    def __traverse(self, listnode: ListNode):
        """遍歷 鏈結串列

        Args:
            listnode (ListNode): _description_
        """
        if listnode.next is None:
            print(listnode.val, end=' -> ')
            print("None")
        else:
            print(listnode.val, end=' -> ')
            self.__traverse(listnode.next)

    def print_linklist(self):
        """印出 鏈結串列
        """
        self.__traverse(self.linklist)


class Solution:

    '''自己解法'''

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


class Solution1:
    '''
    Set curr to the head and iterate till curr and curr.next is not None
    if curr node and curr.next have same value then just skip that node and set curr.next = curr.next.next else curr = curr.next and just return the head
    '''

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


class Solution2:
    '''
    We first deal with edge case of head being None rather than a ListNode
    Next we create a new variable curr to point at our current node, starting with the head node
    If curr.next is another node, we compare curr.val and curr.next.val
        If the values are the same, we must remove one from the linked list
            We keep the first node and remove the second by updating the first's .next (curr.next) to the next node's .next (curr.next.next)
        If the values differ, we move point curr to the next node
    We repeat the previous process until the current node does not point to another node, at which point we return head, the de-duplicated linked list
    '''

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


ll = LinkList()
ll.generate_list([1, 1, 2, 3, 3])
ll.print_linklist()
linklist = Solution().deleteDuplicates(ll.linklist)
ll.set_linklist(linklist)
ll.print_linklist()
