class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is not None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __getitem__(self, index):
        current = self.__head
        for _ in range(index):
            if current is None or current.has_next():
                raise IndexError
            current = current.get_next()
        return current.value

    def __len__(self):
        return self.__len

    def add(self, value):
        self.__len += 1
        new_item = LinkedListItem(value)
        if not self.__head:
            self.__head = new_item
        else:
            self.__tail.set_next(new_item)
        self.__tail = new_item

    def first(self):
        return self.__head.value

    def last(self):
        return self.__tail.value


if __name__ == "__main__":
  items = LinkedList()
  items.add(10)
  items.add(11)
  items.add(12)
  items.add(13)
  items.add(20)
  print(items[1])
  print(items[2])
  print(items[100])
  print(items.first())
  print(items.last())
  print(len(items))