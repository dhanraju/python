"""Postfix expression evaluation."""

from stack import Stack


def postfix_eval(postfix_expr):
    """Postfix evaluation."""
    # Create an empty stack called op_stack for keeping operators.
    op_stack = Stack()
    postfix_list = []
    digits = "0123456789"
    # Convert the input postfix expression string to a list.
    token_list = postfix_expr.split()
    # Scan the token list from right to left.
    for token in token_list:
        if token in digits:
            op_stack.push(int(token))
        else:
            operand2 = op_stack.pop()
            operand1 = op_stack.pop()
            result = do_math(token, operand1, operand2)
            op_stack.push(result)
    return op_stack.pop()

def do_math(operation, op1, op2):
    """Perform math operations."""
    if operation == "*":
        return op1 * op2
    if operation == "/":
        return op1 / op2
    if operation == "+":
        return op1 + op2
    return op1 - op2


if __name__ == '__main__':
    postfix_str = '7 8 + 3 2 + /'
    print(f'Postfix evaluation of postfix expr {postfix_str} is',
        postfix_eval(postfix_str))
