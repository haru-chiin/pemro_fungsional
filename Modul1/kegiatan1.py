
def add(x, y):
    return x + y 
def minus (x, y):
    return x - y
def mult (x, y):
    return x * y
def div (x, y):
    if y == 0:
        return "tidak dapat dibagi dengan 0"
    return x / y

def tree(expression):
    if isinstance(expression, tuple):
        left_operand, operation, right_operand = expression
        if operation == '+':
            return add(tree(left_operand), tree(right_operand))
        elif operation == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operation == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operation == '/':
            return div(tree(left_operand), tree(right_operand))
    else:
        return expression
tes = ((2, '+', 3), '*', (5, '-', 1))
result = tree(tes)
print(result)

# TREE PERCOBAAN
# def tree(operation, x,y):
#     if operation == 'add':
#         return add(x,y)
#     elif operation == 'minus':
#         return minus(x,y)
#     elif operation == 'mult':
#         return mult(x,y)
#     elif operation == 'div':
#         return div(x,y)
#     else:
#         return "operasi ada yang salah" 
# hasil1 = tree('add',5 ,10)
# hasil2 = tree('mult',2,hasil1)
# hasil3 = tree('minus',hasil2,5)
# hasil4 = tree('div',hasil3,5)
# print(hasil1,hasil2,hasil3,hasil4)

