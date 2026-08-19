def longest_valid_parentheses(s):
    stack = [-1]
    start = 0
    max_len = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()

            if not stack:
                stack.append(i)
            else:
                length = i - stack[-1]
                if length > max_len:
                    max_len = length
                    start = stack[-1] + 1

    return s[start:start + max_len]

s = input("Enter parentheses string: ")
print("Longest Valid Parentheses:" ,longest_valid_parentheses(s))