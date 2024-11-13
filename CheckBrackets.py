from Stack import stack

def checkBrackets(statement):
    s = stack(100)
    for ch in statement:
        if (ch in '({[' ):
            s.push(ch)
        elif (ch in ')}]'):
            if s.isEmpty():
                return False
            data = s.pop()
            if (ch == ')' and data != '(') or \
            (ch == '}' and data != '{') or \
            (ch == ']' and data != '['):
                return False

    return s.isEmpty()

if __name__ == "__main__":

    s1 = "{ A[(i=1)] = 0;"
    s2 = "if((i==0) && (j==0)"
    s3 = "A[ (i+1 ] ) = 0;"
    s4 = "[{()()}]"

    print(s1, "-->", checkBrackets(s1))
    print(s2, "-->", checkBrackets(s2))
    print(s3, "-->", checkBrackets(s3))
    print(s4, "-->", checkBrackets(s4))

    filename =  "stack.py"
    with open(filename, "r", encoding="utf-8") as infile:
        str = infile.read()
        print("소스파일 : ", filename, "-->", checkBrackets(str))
