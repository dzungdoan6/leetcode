def isValid(s: str) -> bool:
    stack = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')' and len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        elif s[i] == '}' and len(stack) > 0 and stack[-1] == '{':
            stack.pop()
        elif s[i] == ']' and len(stack) > 0 and stack[-1] == '[':
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    return False

s = "()"
print(isValid(s))

s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))

s = "["
print(isValid(s))

s = "]"
print(isValid(s))