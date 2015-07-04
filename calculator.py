#python
#coding=utf-8
from stack import Stack


class PlusOperator():
    def __init__(self):
        self.type = '+'
        self.priority = 1


class ReductionOperator():
    def __init__(self):
        self.type = '-'
        self.priority = 1


class MultiplicationOperator():
    def __init__(self):
        self.type = '*'
        self.priority = 2


class DivsionOperator():
    def __init__(self):
        self.type = '/'
        self.priority = 2


class RailExpress():
    def __init__(self, express):
        self.fontExpress = express
        self.railExpress = []
        self.size = len(express)
        self.stack = Stack(self.size)
        self.plus = PlusOperator()
        self.reduction = ReductionOperator()
        self.mul = MultiplicationOperator()
        self.divsion = DivsionOperator()

        self.operator = {'+': self.plus, '-':  self.reduction, '*': self.mul, '/': self.divsion}
        self.makeRailExpress()

    def makeRailExpress(self):
        for i in xrange(self.size):
            if (self.fontExpress[i] >= '0') and (self.fontExpress[i] <= '9'):
                self.railExpress.append(self.fontExpress[i])
            else:
                if self.stack.isEmpty():
                    self.stack.push(self.operator[self.fontExpress[i]])
                else:
                    ele = self.fontExpress[i]
                    self.compareOperator(ele)

        while(not self.stack.isEmpty()):
            ele = self.stack.pop()
            self.railExpress.append(ele.type)

    def compareOperator(self, operator):
        top = self.stack.top
        operatorDic = {'+': 1, '-': 1, '*': 2, '/': 2}

        if (operatorDic[operator] - self.stack.stack[top].priority < 1):
            while (operatorDic[operator] - self.stack.stack[top].priority < 1):
                ele = self.stack.pop()
                self.railExpress.append(ele.type)
        else:
            self.stack.push(self.operator[operator])


if __name__ == '__main__':
    express = raw_input('输入表达式：')
    rail = RailExpress(express)

    print rail.railExpress
