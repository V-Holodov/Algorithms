def solution(node):
    """Разворачивает двусвязный список и возвращает голову нового списка"""
    while node.next:
        node.prev, node.next = node.next, node.prev
        node = node.prev
    node.prev, node.next = node.next, node.prev
    return node