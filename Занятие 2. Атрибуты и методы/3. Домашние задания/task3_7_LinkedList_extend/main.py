from typing import Iterable, Optional, Any

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def __len__(self):
        return self.len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index-1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index-1)
            del_node = prev_node.next
            next_node = del_node.__next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert(self, index: int, value: Any) -> None:

        if index >= self.len:
            new_node = Node(value)
            tail = self.step_by_step_on_nodes(self.len-1)
            tail.next = new_node
            new_node.next = None
        elif index == 0:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(value)
            prev_node = self.step_by_step_on_nodes(index-1)
            new_node.next = prev_node.next
            prev_node.next = new_node

        self.len += 1

    def count(self, value: Any):
        count = 0
        for linked_list_value in self:
            if linked_list_value == value:
                count += 1
        return count

    def extend(self, iterable):
        for append_value in iterable:
            new_node = Node(append_value)
            last_node = self.step_by_step_on_nodes(self.len - 1)

            self.linked_nodes(last_node, new_node)
            self.len += 1



if __name__ == "__main__":

    linked_list = LinkedList([1, 2, 3])
    linked_list.extend([1, 2, 3])
    print(linked_list)
