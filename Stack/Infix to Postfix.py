# https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/

def isOperator(c):
    operators = ['+', '-', '*', '/', '^']
    if c in operators:
        return True
    return False

def leftorright(c):
    left = ['+', '-', '*', '/']
    right = ['^']
    if c in left:
        return 'left'
    return 'right'

def prefer(c):
    operator = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    return operator[c]


def InfixtoPostfix(infix):
    stack = []
    postfix = []

    for c in infix:
        if c.isdigit():
            postfix.append(c)
        if c == '(':
            stack.append(c)
        if c == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        if isOperator(c):
            if leftorright(c) == 'right':
                while stack and isOperator(stack[-1]) and prefer(c) - prefer(stack[-1]) < 0 :
                    postfix.append(stack.pop())
            else:
                while stack and isOperator(stack[-1]) and prefer(c) - prefer(stack[-1]) <= 0:
                    postfix.append(stack.pop())
            stack.append(c)

    while stack:
        postfix.append(stack.pop())

    return postfix


def EvaluationPostfix(postfix):
    stack = []
    for c in postfix:
        if c.isdigit():
            stack.append(c)
        if isOperator(c):
            lis = []
            lis.append(stack.pop())
            lis.append('**' if c == '^' else c)
            lis.append(stack.pop())
            expression = ''.join(lis[::-1])
            result = eval(expression)
            stack.append(str(result))
    return stack[0]

infix  = ['(', '5', '+', '(', '(', '9', '-', '8', ')', '*', '(', '7', '-', '1', ')', ')', ')', '*', '7']
posfix = InfixtoPostfix(infix)
print(EvaluationPostfix(posfix))
