class Node:
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
        cur_node = self.__head
        for _ in range(index):
            if cur_node is None or cur_node.has_next():
                raise IndexError
            cur_node = cur_node.get_next()
        return cur_node.value

    def __len__(self):
        return self.__len

    def first(self):
        return self.__head.value

    def last(self):
        return self.__tail.value

    def add(self, value, index = None):
        self.__len += 1
        new_node = Node(value)

        if index is None:
            if not self.__head:
                self.__head = new_node
            else:
                self.__tail.set_next(new_node)
            self.__tail = new_node
        else:
            if index < 0 or index > self.__len - 1:
                raise IndexError
            elif index == 0:
                cur_node = self.__head
                self.__head = new_node
                new_node.set_next(cur_node.get_next())
            else:
                cur_node = self.__head
                for _ in range(1, index):
                    cur_node = cur_node.get_next()
                new_node.set_next(cur_node.get_next())
                cur_node.set_next(new_node)
                cur_node = new_node
        return self

    def add_all(self, values, index = None):
		if index is None:
			for value in values:
				self.add(value, index)
		else:
			i = index
			for value in values:
				self.add(value, index = i)
				i += 1
		return 

    def remove_last_occurence(self, element):
        if element not in self:
            raise ValueError
        cur_node = self.__head
        index = 0
        delete_it = 0
        for _ in range(self.__len):
            if cur_node.value == element:
                delete_it = index
            cur_node = cur_node.get_next()
            index += 1
        self.pop(delete_it)

    def pop(self, index = None):
        if index is None or index == self.__len - 1:
            cur_node = self.__head
            while cur_node.get_next().has_next():
                cur_node = cur_node.get_next()
            pop_it = cur_node.get_next()
            self.__tail = cur_node
            cur_node.set_next(None)
            self.__len -= 1
        elif index > self.__len - 1:
            raise IndexError
            
        elif index == 0:
            pop_it = self.__head
            new_node = pop_it.get_next()
            self.__head = new_node
            self.__len -= 1
        else:
            cur_node = self.__head
            for _ in range(index - 1):
                cur_node = cur_node.get_next()
            pop_it = cur_node.get_next()
            new_node = pop_it.get_next()
            cur_node.set_next(new_node)
            self.__len -= 1
        return pop_it.value
