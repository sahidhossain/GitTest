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


criteria = input("Enter What you want to do? +_/*")

if criteria == '+':
    print(obj.sum(value1, value2))
elif criteria == '-':
    print(obj.sub(value1, value2))
elif criteria == '*':
    print(obj.mul(value1,value1))
elif criteria == '/':
    print(obj.div(value1, value2))
else:
    print("Wrong Input")