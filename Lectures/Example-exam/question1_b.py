""" En lättare variant: Implementera print_reverse() i Node-klassen. """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def print_reverse(self):
        """ Print the linked list in reverse """
        # Rekursera till slutet av listan
        if self.next is not None:
            self.next.print_reverse()

        print(self.data)


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')

    a.next = b
    b.next = c
    c.next = d

    try:
        a.print_reverse()
    except Exception as e:
        print("oops:", e)

    # d
    # c
    # b
    # a