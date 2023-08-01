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


class ListToListNode:

    def __init__(self, nodes) -> None:
        self.nodes = nodes

    def generate(self):
        if len(self.nodes) == 0:
            return None

        # 創建第一個節點
        head = ListNode(self.nodes[0])
        current = head

        for val in self.nodes[1:]:
            current.next = ListNode(val)
            current = current.next

        return current


def traverse(node):

    if node is None:
        return "None"
    else:
        print(node.next, end=' -> ')
        traverse(node.next)


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        for h in head:
            if h.val not in result:
                result.append(h.val)
        return ListToListNode(result)


listnode = ListToListNode([1, 1, 2, 3, 3]).generate()
traverse(listnode)
# s = Solution()
# a = s.deleteDuplicates(listnode)
# print(a)
