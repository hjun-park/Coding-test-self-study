class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_rst, l2_rst = 0, 0

        unit = 1
        while l1:
            l1_rst += l1.val * unit
            l1 = l1.next
            unit *= 10

        unit = 1
        while l2:
            l2_rst += l2.val * unit
            l2 = l2.next
            unit *= 10

        result = str(l1_rst + l2_rst)

        head = None
        linked_list = None

        # 헤드 정의
        head = ListNode(int(result[0]))
        linked_list = head

        # 이후 노드 붙이기
        for n in result[1:]:
            curNode = ListNode(int(n))  # 노드 생성
            curNode.next = linked_list  # 헤드 지정
            linked_list = curNode       # tail 지정

            # 이렇게도 가능함
            # curNode = ListNode(int(n), linked_list)  # (노드, 이어 붙일 대상)
            # linked_list = curNode

        return linked_list


s = Solution()
nodes = s.addTwoNumbers(ListNode(243), ListNode(564))

while nodes:
    print(nodes.val, end='')
    nodes = nodes.next
