def check_string(string):
    q = []
    for c in string:
        if c == "(":
            q.append(c)
        elif c == ")":
            if not q or q.pop() != "(":
                return "no"
        elif c == "[":
            q.append(c)
        elif c == "]":
            if not q or q.pop() != "[":
                return "no"
    if not q:
        return "yes"
    else:
        return "no"


while True:
    string = input()
    if string == ".":
        break
    string.strip()
    print(check_string(string))