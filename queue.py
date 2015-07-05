__author__ = 'Administrator'


class Queue():
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.top = -1

    def push(self, ele):
        if not self.isFull():
            self.queue.append(ele)
            self.top += 1

        else:
            raise Exception("out of range")

    def isFull(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.size == self.top:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            raise Exception("no element")
        else:
            ele = self.queue.pop(0)
        return ele


if __name__ == '__main__':
    queue = Queue(10)

    for i in xrange(5):
        queue.push(i)

    print queue.pop(), queue.queue