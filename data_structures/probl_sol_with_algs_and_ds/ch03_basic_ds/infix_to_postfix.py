"""Infix to postfix conversion."""
from stack import Stack


def infix_to_postfix(infix_string):
    """Convert infix to postfix expression."""
    operator_prec_weight = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # Create an empty stack called op_stack for keeping operators.
    op_stack = Stack()
    # Convert the input infix string to a list.
    token_list = infix_string.split()
    postfix_list = []
    # Scan the token list from left to right.
    for token in token_list:
        # If the token is an operand, append it to the end of output list.
        if token in operands:
            postfix_list.append(token)
        # If the token is a left paranthesis, push it to the op_stack.
        elif token == '(':
            op_stack.push(token)
        # If the token is a right parnethesis, pop the op_stack until the
        # corresponding left paranthesis is removed. Append each operator
        # to the end of output list.
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        # If the token is an operator, push it on the op_stack. However,
        # first remove any opertors already on the op_stack that have higher
        # or equal precendence and append them to the output list.
        else:
            while (not op_stack.is_empty()) and (
                operator_prec_weight[
                    op_stack.peek()] >= operator_prec_weight[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    # check the op_stack, if any operators still on the stack; remove them and
    # append them to the output list.
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


if __name__ == '__main__':
    infix_expr = "A * B + C * D"
    print(f'Conversion of Infix expr {infix_expr} to Postfix expr is',
        infix_to_postfix(infix_expr))
    infix_expr = '( A + B ) * C - ( D - E ) * ( F + G )'
    print(f'Conversion of Infix expr {infix_expr} to Postfix expr is',
        infix_to_postfix(infix_expr))
