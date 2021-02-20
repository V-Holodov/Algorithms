def solution(node):
    """ Функция принимает вершину и печатает все элементы списка. """
    while node.next_item != None:
        print(node.value)
        node = node.next_item
    print(node.value)
