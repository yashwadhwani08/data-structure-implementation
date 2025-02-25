class Node:
    def __init__(self, data=None, next: "Node" = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Empty LL")
            return
        itr = self.head
        llstr = ""
        while itr is not None:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = Node(data, None)

    from typing import List

    def insert_values(self, data_list: List):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self) -> int:
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index: int):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count = 0
        while count < self.get_length():
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                return
            else:
                itr = itr.next
            count += 1
        raise Exception("data_after value is not in ll")

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception("The list is empty")

        itr = self.head
        count = 0
        while itr and count < self.get_length():
            if itr.data == data:
                if itr == self.head:
                    self.head = itr.next
                    return
            if itr.next and itr.next.data == data:
                itr.next = itr.next.next
                return
            count += 1

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.print()
    ll.insert_at_end(60)
    ll.insert_values(["ansh", "ekta"])
    ll.insert_at(0, "yash")
    ll.remove_at(ll.get_length() - 1)
    ll.print()
    ll.remove_by_value("ansh")
    ll.print()
    ll.remove_by_value("yash")
    print("---ll2----")
    ll2 = LinkedList()
    ll2.insert_values(["ekta", "anil"])
    ll2.remove_by_value("anil")
    ll2.remove_by_value("anil")
    ll2.remove_at(0)
    ll2.print()
