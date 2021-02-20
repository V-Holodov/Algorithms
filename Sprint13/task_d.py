def solution(node, elem):
    """Ищет индекс поданного элемента"""
    i = 0
    while node:
        if node.value == elem:
            return i
            break
        else:
            node = node.next_item
            i += 1
    if node == None:
        return -1
