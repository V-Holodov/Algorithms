def solution(node, idx):
    """Удаляет элемент из списка, принимая вершину и индекс этого элемента."""
    head = node
    if idx == 0:
        head = node.next_item
        del node
    else:
        while idx - 1:
            node = node.next_item
            idx -= 1
        node_del = node.next_item
        node_next = node_del.next_item
        node.next_item = node_next
        del node_del
    return head