class StackEmptyException(Exception):
    pass

class StackFullException(Exception):
    pass

class CustomStack:
    def __init__(self, limit_size):
        self.limit_size = limit_size
        self.elements = []

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.limit_size

    def push(self, item):
        if self.is_full():
            raise StackFullException("Não é possível adicionar em uma pilha cheia.")
        self.elements.append(item)

    def pop(self):
        if self.is_empty():
            raise StackEmptyException("Não é possível remover de uma pilha vazia.")
        return self.elements.pop()

    def peek(self):
        if self.is_empty():
            raise StackEmptyException("Não é possível espiar em uma pilha vazia.")
        return self.elements[-1]

class NumberAscOrder:
    @staticmethod
    def sort(stack):
        numbers = []
        while not stack.is_empty():
            numbers.append(stack.pop())
        numbers.sort()
        return numbers