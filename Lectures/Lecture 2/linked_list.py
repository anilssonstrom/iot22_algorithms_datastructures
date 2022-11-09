
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
        # 1. Skapa en ny nod
        new_node = Node(data)

        # 2. Sätt den nya nodens "next" till self.head
        new_node.next = self.head

        # 3. Flytta self.head till den nya noden
        self.head = new_node

        # 4. Om listan är tom: Uppdatera tail
        if self.tail is None:
            self.tail = new_node

    def insert(self, data, after_data):
        # 1. Skapa en ny nod
        new_node = Node(data)

        # Är listan tom?
        if self.head is None:
            raise IndexError("can't insert into an empty list")

        # 2. Hitta rätt ställe i listan
        current = self.head
        while current.data != after_data:
            current = current.next
            if current is None:
                raise IndexError(f"{after_data=} not found in list")

        # 3. Sätt den nya nodens "next" till nästa nod
        new_node.next = current.next
        # 4. Sätt nuvarande nodens "next" till nya noden
        current.next = new_node

    def remove_first_node(self):
        # (1. Om listan är tom: Ge IndexError)
        if self.head is None:
            raise IndexError("list is empty")

        self.head = self.head.next

        if self.head is None:
            self.tail = None

        # 2. Skapa en tillfällig pekare "current"
        # current = self.head

        # 3. Flytta "self.head" till nästa nod
        # self.head = current.next

    def remove_last_node(self):
        # (1. Om listan är tom: Ge IndexError)
        if self.head is None:
            raise IndexError("list is empty")

        # 2. Skapa två tillfälliga pekare "current" och "previous"
        current = self.head
        previous = self.head

        # 3. Stega tills "current" är sista noden (current.next är None)
        while current is not None:
            if current.next is None:
                if current == self.head:
                    self.head = None
                    self.tail = None
                else:
                    # 4. Sätt previous.next = None
                    previous.next = None
                    self.tail = previous

            previous = current
            current = current.next

    def remove_node(self, data):
        if self.head is None:
            raise IndexError("list is empty")

        # Börja med att stega från listans start
        current = self.head
        previous = self.head

        while current is not None:
            # Om detta är noden vi letar efter...
            if current.data == data:
                # Om vi är i starten av listan
                if current == self.head:
                    # Flytta head ett steg åt höger
                    self.head = current.next
                else:
                    # Vi är inte i starten av listan: Flytta förra elementets next ett steg åt höger
                    previous.next = current.next

                # Tog vi bort det sista elementet?
                if self.head is None:
                    self.tail = None
                elif current == self.tail:
                    # Flytta tail ett steg åt vänster
                    self.tail = previous

                # Vi har tagit bort första matchande noden. Avsluta metoden.
                return

            # Vi har inte hittat det vi var ute efter: Flytta båda pekarna
            previous = current
            current = current.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.prepend(25)
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.prepend(99)
    print(llist)

    llist.insert(data=63, after_data=25)
    print(llist)

    llist.remove_first_node()
    print(llist)

    llist.remove_last_node()
    llist.remove_last_node()
    llist.remove_last_node()
    llist.remove_last_node()
    llist.remove_last_node()
    print(llist)

    llist.append(25)
    llist.append(25)
    llist.append(25)
    print(llist)

    llist.remove_node(25)
    print(llist)
