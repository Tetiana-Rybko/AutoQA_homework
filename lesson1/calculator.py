from symtable import Class

class Calculator:
    def __init__(self):
        pass

    def sum(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
          raise ArithmeticError("На ноль делить нельзя")
        return a / b
    def pow(self, a, b):
        return a ** b
    def mod(self, a, b):
        return a % b
    def avg(self, nums):
        if len(nums) == 0:
            return 0
        s = sum(nums)
        return self.div(s, len(nums))