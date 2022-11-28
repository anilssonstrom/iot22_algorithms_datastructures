class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_reverse(self):
        """ Print the linked list in reverse """
        # Basfall
        if self.head is None:
            # I värsta fall är listan tom, så vi kan ha det som basfall
            return

        # Rekursera: Skapar en tillfällig ny LinkedList, med start på nästa nod
        else:
            temp_ll = LinkedList()
            temp_ll.head = self.head.next
            temp_ll.print_reverse()

        # Skriva ut
        print(self.head.data)


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    ll = LinkedList()

    ll.head = a
    a.next = b
    b.next = c
    c.next = d

    try:
        ll.print_reverse()
    except Exception as e:
        print("oops:", e)
