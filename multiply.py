class Calculator:
    def sum(self, x: int, y:int) -> int:
        adding = x + y
        return adding
    def sub(self, x: int, y:int) -> int:
        minus = x - y
        return minus
    def mul(self, x: int, y:int) -> int:
        multiply = x * y
        return multiply
    def div(self, x: int, y:int) -> int:
        divide = x / y
        return divide

obj = Calculator()
value1 = int(input("Enter First Number: "))
value2 = int(input("Enter Second Number: "))



print(obj.mul(value1, value2))

