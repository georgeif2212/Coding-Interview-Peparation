class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printList(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")


def removeNode(head, value):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy

    while curr and curr.next:
        if curr.next.val == value:
            curr.next = (
                curr.next.next
            )  # * Elimina el nodo conectando al siguiente siguiente
            break  # si solo quieres eliminar una vez
        curr = curr.next

    return dummy.next


def insertNodeAtPosition(head, pos, val):
    new_node = ListNode(val)

    # Caso especial: insertar al inicio (posición 0)
    if pos == 0:
        new_node.next = head
        return new_node

    curr = head
    index = 0

    # Recorremos hasta llegar al nodo anterior a la posición
    while curr and index < pos - 1:
        curr = curr.next
        index += 1

    # Si estamos en una posición válida (dentro del rango de la lista)
    if curr:
        new_node.next = curr.next
        curr.next = new_node

    return head


# Crear manualmente una lista
n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

printList(n1)
removeNode(n1, 2)
insertNodeAtPosition(n1, 8, 6)
printList(n1)

print(n3)
printList(n4)
