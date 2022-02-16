def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    if not brackets_row:
        return True
    else:
        count = 0
        for i in brackets_row:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

print(check_brackets("()("))