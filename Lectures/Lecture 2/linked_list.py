
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        node = self.head
        my_str = ""

        while node is not None:
            my_str += f"{node.data} -> "
            node = node.next

        my_str += "None"
        return my_str

    def count(self):
        node = self.head
        n = 0

        while node is not None:
            # Lägga på 1 på vår räknare
            n += 1
            # Gå vidare till nästa node
            node = node.next

        return n

    def sum(self):
        node = self.head
        s = 0

        while node is not None:
            s += node.data
            node = node.next

        return s

    def append(self, data):
        new_node = Node(data)

        if self.head is None or self.tail is None:
            # List was empty
            self.head = new_node
            self.tail = new_node
        else:
            # List is not empty, just add the node to the end
            self.tail.next = new_node  # Add new node after existing tail
            self.tail = new_node  # Move "tail" pointer to our new node

    def prepend(self, data):
        pass
        # 1. Skapa en ny nod
        # (1.5. Är listan tom? Sätt head och tail till den nya noden. Annars fortsätt.)
        # 2. Sätt den nya nodens "next" till self.head
        # 3. Flytta self.head till den nya noden

    def insert(self, data, after_data):
        pass
        # 1. Skapa en ny nod
        # (1.5. Är listan tom? Sätt head och tail till den nya noden. Annars fortsätt.)
        # 2. Hitta rätt ställe i listan
        # 3. Sätt den nya nodens "next" till nästa nod
        # 4. Sätt nuvarande nodens "next" till nya noden


if __name__ == '__main__':
    llist = LinkedList()
    print(llist)

    llist.append(1)
    print(llist)

    llist.append(2)
    print(llist)

    llist.append(3)
    print(llist)

    node = llist.head
    # Börja på första noden och gå till next, tills vi kommer till slutet
    while node is not None:
        # Skriva ut vad noden innehåller
        print(node.data)

        # Gå vidare till nästa nod
        node = node.next

    print("LList length: " + str(llist.count()))
    assert llist.count() == 3

    print("LList sum: " + str(llist.sum()))
    assert llist.sum() == 6

    print("Append(4)")
    llist.append(4)
    print("LList length: " + str(llist.count()))
    print("LList sum: " + str(llist.sum()))
    print(llist)