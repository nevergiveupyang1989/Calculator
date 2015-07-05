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


class LeftBracket():
    def __init__(self):
        self.type = '('
        self.priority = 9


class RightBracket():
    def __init__(self):
        self.type = ')'
        self.priority = 9


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
        self.left = LeftBracket()
        self.right = RightBracket()

        self.operator = {'+': self.plus, '-':  self.reduction, '*': self.mul, '/': self.divsion, '(': self.left, ')': self.right}
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

        while not (self.stack.isEmpty()):
            ele = self.stack.pop()
            self.railExpress.append(ele.type)

    def compareOperator(self, operator):
        operatorDic = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 9, ')': 9}

        if(operatorDic[operator]) - (self.stack.stack[self.stack.top].priority) == -1:
            while (operatorDic[operator]) - (self.stack.stack[self.stack.top].priority) == -1:
                ele = self.stack.pop()
                self.railExpress.append(ele.type)
                if self.stack.stack[self.stack.top - 1] == self.operator[operator]:
                    self.railExpress.append(operator)
                else:
                    self.stack.push(self.operator[operator])

        elif(operator is '('):
            self.stack.push(self.operator[operator])

        elif(operator is ')'):
            while 1:
                ele = self.stack.pop()
                if not isinstance(ele, LeftBracket):
                    self.railExpress.append(ele.type)
                else:
                    break
        else:
            self.stack.push(self.operator[operator])


class CheckExpress():
    def __init__(self, express):
        self.express = express

    def checkExpress(self):
        express = []
        count = -1

        for each in self.express:
            if (each >= '0') and (each <= '9'):
                length = len(express)
                if length == 0:
                    express.append(each)
                    count += 1

                elif (express[count] > '0') and (express[count] < '9'):
                    express[length - 1] = express[length - 1] + each
                else:
                    express.append(each)
                    count += 1
            else:
                express.append(each)
                count += 1

        return express


class Calculator():
    def __init__(self, express):
        self.express = express
        size = len(express)
        self.stack = Stack(size)
        self.result = None

        self.operatorRailExpress()

    def operatorRailExpress(self):
        for each in self.express:
            if (each >= '0') and (each <= '9'):
                self.stack.push(each)

            else:
                twoOperator = self.stack.pop()
                oneOperator = self.stack.pop()
                temp = self.calculator(oneOperator, twoOperator, each)

                self.stack.push(temp)

        self.result = self.stack.returnFristEle()

    def calculator(self, one, two, operator):
        operatorDict = {'+': self.plus, '-': self.reduction, '*': self.multiplicate, '/': self.devision}
        temp = operatorDict[operator](one, two)

        return temp

    def plus(self, one, two):
        return int(one)+int(two)

    def reduction(self, one, two):
        return int(one)-int(two)

    def multiplicate(self, one, two):
        return int(one)*int(two)

    def devision(self, one, two):
        return int(one)/int(two)

if __name__ == '__main__':
    express = raw_input('输入表达式：')
    express = CheckExpress(express).checkExpress()
    rail = RailExpress(express)

    calculate = Calculator(rail.railExpress)
    print calculate.result