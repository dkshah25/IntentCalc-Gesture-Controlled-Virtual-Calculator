class CalculatorEngine:
    def __init__(self):
        self.expr = ""

    def input(self, val):
        self.expr += val

    def clear(self):
        self.expr = ""

    def backspace(self):
        self.expr = self.expr[:-1]

    def evaluate(self):
        try:
            return str(self._compute(self.expr))
        except:
            return "Error"

    def _compute(self, exp):
        def precedence(op):
            return 1 if op in "+-" else 2

        def apply(a, b, op):
            return {
                '+': a + b,
                '-': a - b,
                '*': a * b,
                '/': a / b
            }[op]

        nums, ops = [], []
        i = 0

        while i < len(exp):
            if exp[i].isdigit() or exp[i] == '.':
                num = ""
                while i < len(exp) and (exp[i].isdigit() or exp[i] == '.'):
                    num += exp[i]
                    i += 1
                nums.append(float(num))
                continue

            while ops and precedence(ops[-1]) >= precedence(exp[i]):
                b, a = nums.pop(), nums.pop()
                nums.append(apply(a, b, ops.pop()))
            ops.append(exp[i])
            i += 1

        while ops:
            b, a = nums.pop(), nums.pop()
            nums.append(apply(a, b, ops.pop()))

        return nums[0]
