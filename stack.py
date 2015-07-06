
class Stack():
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = []

    def push(self, ele):
        if self.isfull():
            raise Exception("out of range")
        else:
            self.stack.append(ele)
            self.top += 1

    def isfull(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            raise Exception("no element")
        else:
            self.top -= 1
            return self.stack.pop()

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def returnFristEle(self):
        return self.stack[self.top]

    def returnStack(self):
        return self.stack

if __name__ == '__main__':
    s = Stack(1)

    for i in xrange(3):
        s.push(i)
    print s.stack, s.top


