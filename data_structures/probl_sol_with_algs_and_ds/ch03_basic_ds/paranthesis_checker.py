"""Paranthesis checker."""
from stack import Stack


def paranthesis_checker(symbol_string):
    """Paranthesis checker."""
    s = Stack()
    is_balanced = True
    index = 0
    # Navigate character by character through the symbol_string.
    while index < len(symbol_string) and is_balanced:
        symbol = symbol_string[index]
        # Push the open paranthesis into the stack
        if symbol in "([{":
            s.push(symbol)
        elif symbol in ")]}":
            # Pop the corresponding open paranthesis for the close paranthesis.
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                # Make sure the most recent parenthesis matches the next close
                # symbol. If no open symbol on the stack to match a close
                # symbol, the string is not balanced.
                if not matches(top, symbol):
                    is_balanced = False
        index = index + 1
    # When all the symbols are processed, the stack should be empty for a balanced
    # paranthesis. Othewise, the paranthesis in the given string is not balanced.
    if is_balanced and s.is_empty():
        return True
    return False

def matches(open_paran, close_paran):
    """Checks the close paranthesis matches with the open paranthesis."""
    opens = "([{"
    closes = ")]}"
    return opens.index(open_paran) == closes.index(close_paran)


if __name__ == '__main__':
    st = '{{([][])}()}'
    print(f'Is {st} balanced?', paranthesis_checker(st))
    st = '[{()]'
    print(f'Is {st} balanced?', paranthesis_checker(st))
