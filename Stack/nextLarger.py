class Stack(object):
    def __init__(self, limit=1000):
        self.stack = []
        self.limit = limit

    def push(self, item):
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from empty stack')

    def is_empty(self):
        return not bool(self.stack)


def nextLarger(a):
    n = len(a)
    result = [None]*n
    stack = Stack()
    stack.push(a[0])
    i = 1
    index = 0
    while i < n:
        top = stack.pop()
        if top < a[i]:
            result[index] = a[i]
            index -= 1
        else:
            stack.push(top)
            stack.push(a[i])
            index = i
            i += 1
        if stack.is_empty():
            stack.push(a[i])
            index = i
            i += 1


    for i in range(n):
        if not result[i]:
            result[i] = -1
    #result[-1] = -1

    return result

a = [10, 3, 12, 4, 2, 9, 13, 0, 8, 11, 1, 7, 5, 6]
print(nextLarger(a))