from traits.api import List, HasTraits, Str


class Model(HasTraits):
    result = Str("")
    one = Str("1")
    two = Str("2")
    three = Str("3")
    four = Str("4")
    five = Str("5")
    six = Str("6")
    seven = Str("7")
    eight = Str("8")
    nine = Str("9")
    zero = Str("0")
    leftBracket = Str('(')
    rightBracket = Str(')')
    mul = Str('*')
    divsion = Str('/')
    plus = Str('+')
    reduct = Str('-')
    equ = Str('=')
    point = Str('.')
    def __init__(self):
        self.isClear = False
